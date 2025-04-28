import numpy as np

def hohmann_transfer(r1, r2, mu):
    v1 = np.sqrt(mu / r1)
    v_transfer1 = np.sqrt(mu * (2/r1 - 1/((r1 + r2)/2)))
    delta_v1 = v_transfer1 - v1

    v2 = np.sqrt(mu / r2)
    v_transfer2 = np.sqrt(mu * (2/r2 - 1/((r1 + r2)/2)))
    delta_v2 = v2 - v_transfer2

    return delta_v1, delta_v2
