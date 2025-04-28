
import numpy as np
from src.tle_tools import tle_to_state
from src.utils import CelestialBody

class SimConfig:
    def __init__(self, use_tle=False):

        self.central_body = CelestialBody(
            name='Earth',
            mu=398600.4418,  # km^3/s^2
            radius=6378.137,  # km
            j2=1.08263e-3,
            rho0=1.225,
            H=8500
        )
        # >>>>>>>>>>>>    Change the Planet's properties as needed     <<<<<<<<<<<<<<<<<<<<
        
        if use_tle:
            tle1 = "1 20580U 90037B   20030.43759598  .00000411  00000-0  17291-4 0  9991"
            tle2 = "2 20580  28.4697  62.9738 0002823  70.5027 289.6513 15.09176270210384"

            # >>>>>>>>>>>>>>>>>>   Paste TLE above as given     <<<<<<<<<<<<<<<<<<<<<<<<<<<




            
            self.initial_state = tle_to_state(tle1, tle2)
        else:
            self.initial_state = np.array([7000.0, 0.0, 0.0, 0.0, 7.5, 1.0])

        #                                  [ x,     y,     z,     vx,   vy,   vz ]
        #                                  [km]   [km]   [km]   [km/s][km/s][km/s]
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # Use the above format for a manual position and velocity 
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        self.duration = 86400  # seconds
        self.dt = 60  # seconds
        self.mass = 1000  # kg
        self.A = 10  # m^2
        self.Cd = 2.2

def load_simulation_config(use_tle=False):
    return SimConfig(use_tle=use_tle)
