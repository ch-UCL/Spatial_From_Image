import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from matplotlib.colors import Normalize
import matplotlib.cm as cm
import matplotlib
import pandas as pd
import os
from scipy.interpolate import griddata
matplotlib.use('TkAgg')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['mathtext.fontset'] = 'stix'

output_folder = r'E:\3D'
excel_path = os.path.join(output_folder, '3DZHdata.xlsx')
df = pd.read_excel(excel_path)
x_flat = df['X_coordinate'].values
y_flat = df['Y_coordinate'].values
z_flat = df['Z_scaled_value'].values

grid_size = int(np.sqrt(len(x_flat)))
grid_x, grid_y = np.mgrid[min(x_flat):max(x_flat):complex(grid_size), min(y_flat):max(y_flat):complex(grid_size)]
grid_z = griddata((x_flat, y_flat), z_flat, (grid_x, grid_y), method='cubic')
X = grid_x
Y = grid_y
Z_scaled = grid_z

step = 5
X_sparse = X[::step, ::step]
Y_sparse = Y[::step, ::step]
Z_sparse = Z_scaled[::step, ::step]
x_sparse_flat = X_sparse.flatten()
y_sparse_flat = Y_sparse.flatten()
z_sparse_flat = Z_sparse.flatten()
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')
color_schemes = { ... }
selected_scheme_name = '14'
cmap_name = color_schemes[selected_scheme_name]
cmap = plt.get_cmap(cmap_name)


tri = mtri.Triangulation(x_sparse_flat, y_sparse_flat)
segments = np.array([...])
z_min_target = z_flat.min()
z_max_target = z_flat.max()
z_mid = np.array([...])
norm = Normalize(vmin=z_min_target, vmax=z_max_target)
colors = cmap(norm(z_mid))
line_collection = Line3DCollection(segments, colors=colors, linewidths=1.2)
ax.add_collection3d(line_collection)