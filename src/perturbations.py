import numpy as np

def apply_perturbations(trajectory, config):
    perturbed = []
    for state in trajectory:
        pos, vel = state[:3], state[3:]
        acc_j2 = config.central_body.j2_acceleration(pos)
        acc_drag = config.central_body.drag_acceleration(pos, vel, config)
        total_acc = acc_j2 + acc_drag
        new_vel = vel + total_acc * config.dt
        new_pos = pos + new_vel * config.dt
        perturbed.append(np.concatenate((new_pos, new_vel)))
    return np.array(perturbed)

