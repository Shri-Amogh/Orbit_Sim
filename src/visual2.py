from vpython import sphere, vector, color, arrow, scene, rate, label

def plot_3d_orbit(trajectory, central_body_radius=6378.137):
    # Create the scene
    scene.title = "Orbital Simulation"
    scene.width = 800
    scene.height = 600
    scene.background = color.black
    
    # Plot central body (e.g., Earth)
    central_body = sphere(pos=vector(0, 0, 0), radius=central_body_radius, color=color.white, opacity=0.1)
    north_pole = sphere(pos=vector(0, 0, central_body_radius * 1.05), radius=central_body_radius * 0.05, color=color.red)
    sim_time = 0
    clock = label(pos=vector(0, 1.2*central_body_radius, 0), text="Time: 0 s", xoffset=20, yoffset=20, height=16, color=color.white, box=False)


    # Or use an arrow pointing out the north
    north_arrow = arrow(pos=vector(0, 0, central_body_radius), axis=vector(0, 0, central_body_radius * 0.5), color=color.red)
    
    # Plot satellite trajectory
    # Create an initial satellite position
    satellite = sphere(pos=vector(trajectory[0, 0], trajectory[0, 1], trajectory[0, 2]), 
                       radius=200, color=color.yellow, make_trail=True)
    
    # Draw the orbit (a line)
    orbit_line = []
    for state in trajectory:
        pos = vector(state[0], state[1], state[2])
        orbit_line.append(pos)

    # Connect the trajectory points with a line
    for i in range(len(orbit_line) - 1):
        arrow(pos=orbit_line[i], axis=orbit_line[i + 1] - orbit_line[i], color=color.white)
    
    # Update satellite position on each iteration
    for i in range(1, len(trajectory)):
        rate(60)  # Speed of the animation
        satellite.pos = vector(trajectory[i, 0], trajectory[i, 1], trajectory[i, 2])
        #satellite.pos = vector(*trajectory[i, :3]) / 1000

        sim_time += 60
        hours = int(sim_time // 3600)
        minutes = int((sim_time % 3600) // 60)
        seconds = int(sim_time % 60)
        clock.text = f"Time: {hours:02d}:{minutes:02d}:{seconds:02d}"

