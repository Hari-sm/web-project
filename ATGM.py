import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # gravitational acceleration (m/s^2)
drag_coefficient = 0.5  # Drag coefficient (a simplified constant)
mass = 50  # mass of the missile in kg
radius = 0.2  # radius of the missile (for calculating drag force)
air_density = 1.225  # air density at sea level (kg/m^3)

# Initial conditions
initial_speed = 300  # initial speed of the missile in m/s
launch_angle = 45  # launch angle in degrees
initial_height = 0  # initial height in meters
target_distance = 2000  # distance to the target (m)

# Time parameters
time_step = 0.1  # Time step for simulation (seconds)
time_max = 60  # Maximum simulation time (seconds)

# Convert angle to radians
theta = np.radians(launch_angle)

# Initial velocity components
vx = initial_speed * np.cos(theta)
vy = initial_speed * np.sin(theta)

# Initialize position and velocity
x = 0  # initial x position (m)
y = initial_height  # initial y position (m)

# List to store trajectory data
x_vals = [x]
y_vals = [y]

# Simulate the missile's flight path
time = np.arange(0, time_max, time_step)

for t in time:
    # Calculate the drag force (F_d = 0.5 * Cd * A * rho * v^2)
    velocity = np.sqrt(vx**2 + vy**2)
    drag_force = 0.5 * drag_coefficient * np.pi * (radius**2) * air_density * velocity**2
    
    # Compute acceleration due to gravity and drag
    ax = -drag_force * vx / (mass * velocity)  # acceleration in x (due to drag)
    ay = -g - drag_force * vy / (mass * velocity)  # acceleration in y (gravity + drag)
    
    # Update velocity components
    vx += ax * time_step
    vy += ay * time_step
    
    # Update position
    x += vx * time_step
    y += vy * time_step
    
    # Append the new position to the trajectory data
    x_vals.append(x)
    y_vals.append(y)
    
    # Stop if missile hits the ground
    if y <= 0:
        break

# Plot the trajectory
plt.figure(figsize=(10, 5))
plt.plot(x_vals, y_vals, label="Missile Trajectory")
plt.title("ATGM (Anti-Tank Guided Missile) Simulation")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.grid(True)
plt.legend()
plt.show()

# Output the final impact point
print(f"Missile impact point: x = {x_vals[-1]:.2f} m, y = {y_vals[-1]:.2f} m")