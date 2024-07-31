solution = {
    'task_a': (
        [2],
        """"
import numpy as np
Dx = 0.1
x = np.arange(-2*np.pi,2*np.pi+Dx,Dx)
y = np.arange(-np.pi,2*np.pi+Dx,Dx)
(Xg, Yg) = np.meshgrid(x,y)

# compute f and g
f_xy = np.sin(Xg)*np.cos(Yg)
g_xy = np.cos(Xg)*np.sin(Yg)

# B2
# compute s and p
s = f_xy + g_xy
p = f_xy * g_xy
"
""")

}
