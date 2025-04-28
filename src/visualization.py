### src/visualization.py
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot_3d_orbit(trajectory, config):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x, y, z = trajectory[:, 0], trajectory[:, 1], trajectory[:, 2]
    ax.plot(x, y, z, label='Satellite Orbit')

    # Draw central planet as a sphere
    u, v = np.mgrid[0:2*np.pi:50j, 0:np.pi:25j]
    planet_radius = config.central_body.radius
    planet_x = planet_radius * np.cos(u) * np.sin(v)
    planet_y = planet_radius * np.sin(u) * np.sin(v)
    planet_z = planet_radius * np.cos(v)
    ax.plot_surface(planet_x, planet_y, planet_z, color='b', alpha=0.6, label='Planet')

    ax.set_xlabel('X (km)')
    ax.set_ylabel('Y (km)')
    ax.set_zlabel('Z (km)')
    ax.set_title(f"Orbit around {config.central_body.name}")
    ax.legend()
    plt.show()
