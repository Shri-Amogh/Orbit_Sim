import numpy as np
from src.integrator import rk4

def equations_of_motion(state, t, config):
    pos, vel = state[:3], state[3:]
    acc = -config.central_body.mu * pos / np.linalg.norm(pos)**3
    return np.concatenate((vel, acc))

def propagate_orbit(state0, duration, dt, config):
    times = np.arange(0, duration, dt)
    trajectory = rk4(lambda y, t: equations_of_motion(y, t, config), state0, times)
    return trajectory
