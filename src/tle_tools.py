from skyfield.api import EarthSatellite, load
import numpy as np

def tle_to_state(tle_line1, tle_line2, epoch_time=None):
    ts = load.timescale()
    satellite = EarthSatellite(tle_line1, tle_line2, "TLE Sat", ts)
    t = ts.now() if epoch_time is None else ts.utc(*epoch_time)
    geocentric = satellite.at(t)

    pos = geocentric.position.km  # position in km
    vel = geocentric.velocity.km_per_s  # velocity in km/s
    return np.concatenate((pos, vel))
