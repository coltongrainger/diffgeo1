from sage.manifolds.utilities import set_axes_labels

var('x s t')
sphereoid = x^4 + s^2 + t^2 - 1
sphere = x^2 + s^2 + t^2 - 1

hue = 4*(x^2 - x^4).function(x)
cm = colormaps.Greys_r

M=1
(implicit_plot3d(sphereoid, (x,-M, M), (s, -M, M), (t, -M, M), color='darkgrey', opacity=0.65)\
    + implicit_plot3d(sphere, (x,-M, M), (s, -M, M), (t, -M, M), color='black', opacity=0.7))\
    .show(viewer='tachyon')
    
for M in [1, 0.95, 0.9, 0.85, 0.8]:
    (implicit_plot3d(sphereoid, (x,-M, M), (s, -M, M), (t, -M, M), color=(hue, cm)) +\
        implicit_plot3d(sphere, (x,-M, M), (s, -M, M), (t, -M, M), color=(hue, cm)))\
    .show(viewer='tachyon')
