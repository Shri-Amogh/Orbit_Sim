import numpy as np

class CelestialBody:
    def __init__(self, name, mu, radius, j2, rho0, H):
        self.name = name
        self.mu = mu
        self.radius = radius
        self.j2 = j2
        self.rho0 = rho0
        self.H = H

    def j2_acceleration(self, pos):
        x, y, z = pos
        r = np.linalg.norm(pos)
        factor = 1.5 * self.j2 * self.mu * self.radius**2 / r**5
        ax = x * (5*z**2/r**2 - 1) * factor
        ay = y * (5*z**2/r**2 - 1) * factor
        az = z * (5*z**2/r**2 - 3) * factor
        return np.array([ax, ay, az])

    def drag_acceleration(self, pos, vel, config):
        r = np.linalg.norm(pos)
        h = r - self.radius
        rho = self.rho0 * np.exp(-h*1000 / self.H)
        Cd = config.Cd
        A = config.A
        m = config.mass
        v_rel = np.linalg.norm(vel)
        drag = -0.5 * Cd * A / m * rho * v_rel * vel
        return drag
    
    def get_axis_vector(self):
        
        if not hasattr(self, "obliquity"):
            self.obliquity = 0  # Default: no tilt
        angle_rad = np.radians(self.obliquity)
        return np.array([0, np.sin(angle_rad), np.cos(angle_rad)])

