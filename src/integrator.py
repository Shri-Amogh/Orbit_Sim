
import numpy as np

def rk4(f, y0, t):
    y = [y0]
    for i in range(1, len(t)):
        dt = t[i] - t[i - 1]
        k1 = f(y[-1], t[i-1])
        k2 = f(y[-1] + dt/2 * k1, t[i-1] + dt/2)
        k3 = f(y[-1] + dt/2 * k2, t[i-1] + dt/2)
        k4 = f(y[-1] + dt * k3, t[i-1] + dt)
        y.append(y[-1] + dt/6*(k1 + 2*k2 + 2*k3 + k4))
    return np.array(y)
