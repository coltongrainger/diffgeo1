var('u,v,w,y,z')
M = 0.7; K = 1; N = 2; H = 0.7
f_x = exp(u)*cos(v)
f_y = exp(u)*sin(v)
f_z = -exp(-u)
p = parametric_plot3d([f_x, f_y,f_z], (u, -M, M), (v, -K*pi, K*pi), opacity=0.8)
p += implicit_plot3d((x^2 + y^2 + z^2), (x,-N,N), (y,-N,N), (z,-N,N), opacity=0.5, contour=[H, 2*H, 3*H, 4*H,5*H,6*H],\
                     region=lambda x,y,z: x<=0 or y>=0 , color='aquamarine')
p.show(viewer='tachyon')

