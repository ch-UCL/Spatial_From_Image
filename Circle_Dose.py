""" import numpy as np
import matplotlib.pyplot as plt

from skimage import measure
import skimage as ski


filename = 'Scalp_Test_preserve angles.png'
scalp = ski.io.imread(filename)
scalp = ski.color.rgb2gray(scalp)

contours = measure.find_contours(scalp)

# Display the image and plot all contours found
fig, ax = plt.subplots()
ax.imshow(scalp, cmap=plt.cm.gray)

for contour in contours:
    print(contour)
    ax.plot(contour[:, 1], contour[:, 0], linewidth=2)

ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])
plt.show()
 """




""" 
import matplotlib.pyplot as plt

from skimage import data, color, img_as_ubyte
from skimage.feature import canny
from skimage.transform import hough_ellipse
from skimage.draw import ellipse_perimeter
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from skimage import data
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, footprint_rectangle
from skimage.color import label2rgb
from skimage import measure
import skimage as ski


filename = 'Scalp_Test_Conformal.png'
scalp = ski.io.imread(filename)
scalp = ski.color.rgb2gray(scalp)
scalp_rgb = color.gray2rgb(img_as_ubyte(scalp))
image= scalp

thresh = threshold_otsu(image)
bw = closing(image, footprint_rectangle((3, 3)))

# remove artifacts connected to image border
cleared = clear_border(bw)

# label image regions
label_image = label(image)
# to make the background transparent, pass the value of `bg_label`,
# and leave `bg_color` as `None` and `kind` as `overlay`
image_label_overlay = label2rgb(label_image, image=image, bg_label=0)

fig, ax = plt.subplots(figsize=(10, 6))
ax.imshow(image_label_overlay)

for region in regionprops(label_image):
    # take regions with large enough areas
    if region.area >= 500:
        # draw rectangle around segmented coins
        minr, minc, maxr, maxc = region.bbox
        rect = mpatches.Rectangle(
            (minc, minr),
            maxc - minc,
            maxr - minr,
            fill=False,
            edgecolor='red',
            linewidth=2,
        )
        ax.add_patch(rect)

ax.set_axis_off()
plt.tight_layout()
plt.show()


import scikit-tda 
 """


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import skimage as ski

# Load the grayscale image
filename = 'Scalp_Test_preserve angles.png'
image = ski.io.imread(filename)
image = ski.color.rgb2gray(image)

# Create coordinate grids for X and Y axes
height, width = image.shape
x = np.arange(0, width)
y = np.arange(0, height)
X, Y = np.meshgrid(x, y)

# Z values are the pixel intensities (0-1 for grayscale)
Z = image

# Create 3D surface plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis')
# Plot projections of the contours for each dimension.  By choosing offsets
# that match the appropriate axes limits, the projected contours will sit on
# the 'walls' of the graph.
ax.contour(X, Y, Z, zdir='z', offset=-1, cmap='coolwarm')
ax.contour(X, Y, Z, zdir='x', offset=-100, cmap='coolwarm')
ax.contour(X, Y, Z, zdir='y', offset=-100, cmap='coolwarm')


ax.set_xlabel('X (pixels)')
ax.set_ylabel('Y (pixels)')
ax.set_zlabel('Intensity')
ax.set_title('3D Surface from Image Intensity')

# Add a colorbar

ax.set(xlim=(-100, width), ylim=(-100, height), zlim=(-0.5, 0.5),
       xlabel='X', ylabel='Y', zlabel='Z')

fig.colorbar(surf, ax=ax, label='Intensity')
plt.show()