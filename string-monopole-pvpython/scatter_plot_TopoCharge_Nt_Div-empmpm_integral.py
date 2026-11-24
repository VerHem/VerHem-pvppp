import glob
import os
import re

import numpy as np
import matplotlib.pyplot as plt

csv_folder = '/home/heidi/Documents/VerHem-project/VerHem-Visualization-Images/'
categories = ['monopole', 'TopologicalTrivial', 'antimonopole', 'antiTopologicalTrivial']

# File names pattern: Div_empmpm_integrals-<category>-Radius<XX>xi0GL.csv
# 'Div_empmpm_integrals-(?P<category>.+)-Radius(?P<radius>[0-9.]+)xi0GL-Solution-13-8-MPI\.csv$' is a regex,
# through witch re.compile() generates reusble regex object "filename_pattern", which is used to match `category` & `radius` parameter.
filename_pattern = re.compile(r'Div_empmpm_integrals-(?P<category>.+)-Radius(?P<radius>[0-9.]+)xi0GL-Solution-13-8-MPI\.csv$')

normalization_factor = np.pi
# ---------------------------------------------------------------
# 1. Collect (radius, mean, std) for every csv file, per category
# ---------------------------------------------------------------
NtDataContainer = {}
for category in categories:
    NtDataContainer[category] = {'radius': [], 'mean': [], 'std': []}

csv_paths = glob.glob(os.path.join(csv_folder,
                                   'Div_empmpm_integrals-*-Radius*xi0GL-Solution-13-8-MPI.csv'))

for csv_path in csv_paths:
    # `match` now has `category` + `radius` catched
    ParamterMatch = filename_pattern.match(os.path.basename(csv_path))
    if ParamterMatch is None:
        continue

    category = ParamterMatch.group('category')
    radius = float(ParamterMatch.group('radius')) # cast radius to float
    if category not in NtDataContainer:
        continue

    # Load integration values; Column 3 is 'integral_div_empmpm'; skiprows=1 skips the header line
    integral_div = np.loadtxt(csv_path, delimiter=',', skiprows=1, usecols=3)
    integral_div_normlized = integral_div/normalization_factor

    NtDataContainer[category]['radius'].append(radius)
    NtDataContainer[category]['mean'].append(np.mean(integral_div_normlized))

    # ddof=1 gives the sample standard deviation (use ddof=0 for population STD)
    NtDataContainer[category]['std'].append(np.std(integral_div_normlized, ddof=1))

# ---------------------------------------------------------------
# 2. Sort each category by radius so that array index increase along radius
# ---------------------------------------------------------------
for category in categories:
    radius = np.array(NtDataContainer[category]['radius'])
    mean = np.array(NtDataContainer[category]['mean'])
    std = np.array(NtDataContainer[category]['std'])

    order = np.argsort(radius)
    NtDataContainer[category]['radius'] = radius[order]
    NtDataContainer[category]['mean'] = mean[order]
    NtDataContainer[category]['std'] = std[order]

# Explicit arrays for each category; element i corresponds to radius_*[i]
radius_monopole = NtDataContainer['monopole']['radius']
mean_monopole = NtDataContainer['monopole']['mean']
STD_monopole = NtDataContainer['monopole']['std']

radius_antimonopole = NtDataContainer['antimonopole']['radius']
mean_antimonopole = NtDataContainer['antimonopole']['mean']
STD_antimonopole = NtDataContainer['antimonopole']['std']

radius_TopologicalTrivial = NtDataContainer['TopologicalTrivial']['radius']
mean_TopologicalTrivial = NtDataContainer['TopologicalTrivial']['mean']
STD_TopologicalTrivial = NtDataContainer['TopologicalTrivial']['std']

radius_antiTopologicalTrivial = NtDataContainer['antiTopologicalTrivial']['radius']
mean_antiTopologicalTrivial = NtDataContainer['antiTopologicalTrivial']['mean']
STD_antiTopologicalTrivial = NtDataContainer['antiTopologicalTrivial']['std']


print('monopole radii (XX):', radius_monopole)
print('mean_monopole      :', mean_monopole)
print('STD_monopole       :', STD_monopole)

print('antimonopole radii (XX):', radius_antimonopole)
print('mean_antimonopole      :', mean_antimonopole)
print('STD_antimonopole       :', STD_antimonopole)

print('TopologicalTrivial radii (XX):', radius_TopologicalTrivial)
print('mean_TopologicalTrivial      :', mean_TopologicalTrivial)
print('STD_TopologicalTrivial       :', STD_TopologicalTrivial)

print('antiTopologicalTrivial radii (XX):', radius_antiTopologicalTrivial)
print('mean_antiTopologicalTrivial      :', mean_antiTopologicalTrivial)
print('STD_antiTopologicalTrivial       :', STD_antiTopologicalTrivial)

# ---------------------------------------------------------------
# 3. Scatter plot with STD as error bars, one group per category
# ---------------------------------------------------------------
fig_size  = (8, 5.5)     # figure size in inches (width, height)
fig_dpi   = 300          # resolution of the saved file
save_path = '/home/heidi/Documents/my-note-and-paper-manuscripts/my_paper_manuscripts/A-phase-string-monopole-overleaf/Nt.png'   # .png, .pdf or .svg; None = do not save

# plot box position inside the figure, as fractions of the figure (0 to 1)
box_left, box_right, box_bottom, box_top = 0.15, 0.97, 0.15, 0.98

label_fontsize = 28
tick_fontsize = 22
legend_fontsize = 16
marker_size_1 = 15
marker_size_2 = 12
MarkerEdgeWidth = 3.5

fig, ax = plt.subplots(figsize=(8, 6))

ax.errorbar(radius_monopole, mean_monopole, yerr=STD_monopole,
            fmt='o', markersize=marker_size_1, capsize=4, elinewidth=1.5,
            label=r'$\tilde{N}_{+1}$')
#ax.errorbar(radius_antimonopole, -mean_antimonopole, yerr=STD_antimonopole,
#            fmt='d', markersize=marker_size, capsize=4, elinewidth=1.5,
#            label=r'$-\tilde{N}_-$')
ax.errorbar(radius_antimonopole, -mean_antimonopole, yerr=STD_antimonopole,
            fmt='d', markersize=marker_size_2, capsize=4, elinewidth=1.5,
            markerfacecolor='none',
            markeredgewidth=MarkerEdgeWidth,
            label=r'$-\tilde{N}_{-1}$')

ax.errorbar(radius_TopologicalTrivial, -mean_TopologicalTrivial, yerr=STD_TopologicalTrivial,
            fmt='s', markersize=marker_size_1, capsize=4, elinewidth=1.5,
            label=r'$-\tilde{N}_{\Sigma_{T^1}}$')
ax.errorbar(radius_antiTopologicalTrivial, mean_antiTopologicalTrivial, yerr=STD_antiTopologicalTrivial,
            fmt='>', markersize=marker_size_2, capsize=4, elinewidth=1.5,
            markerfacecolor='none',
            markeredgewidth=MarkerEdgeWidth,
            label=r'$\tilde{N}_{\Sigma_{T^2}}$')


ax.set_ylim([0.55, 1.05])
ax.set_xlabel(r'$R_{\Sigma}/\xi^0_{GL}$', fontsize=label_fontsize)
ax.set_ylabel(r'$\tilde{N}$', fontsize=label_fontsize)
ax.tick_params(axis='both', labelsize=tick_fontsize)
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(fontsize=legend_fontsize, loc='lower right')
# fig.tight_layout()

fig.subplots_adjust(left=box_left, right=box_right, bottom=box_bottom, top=box_top)

fig.savefig(save_path, dpi=fig_dpi)
print('saved', save_path)    

plt.show()
