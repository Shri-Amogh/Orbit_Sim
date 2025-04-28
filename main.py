import src.visual2 as vs2
from src.orbit import propagate_orbit
from src.perturbations import apply_perturbations
from src.visualization import plot_3d_orbit
from src.sim_config import load_simulation_config

config = load_simulation_config(use_tle=True)
trajectory = propagate_orbit(config.initial_state, duration=config.duration, dt=config.dt, config=config)
perturbed_trajectory = apply_perturbations(trajectory, config)
plot_3d_orbit(perturbed_trajectory, config)
vs2.plot_3d_orbit(perturbed_trajectory)


