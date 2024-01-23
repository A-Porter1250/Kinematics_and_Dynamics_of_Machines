import numpy as np
import matplotlib.pyplot as plt

# Function to calculate position vector of a point
def position_vector(length, angle):
    x = length * np.cos(angle)
    y = length * np.sin(angle)
    return np.array([x, y])

# Function to calculate velocity vector of a point
def velocity_vector(length, angular_velocity, angle):
    vx = -length * angular_velocity * np.sin(angle)
    vy = length * angular_velocity * np.cos(angle)
    return np.array([vx, vy])

# Function to calculate acceleration vector of a point
def acceleration_vector(length, angular_velocity, angular_acceleration, angle):
    ax = -length * angular_acceleration * np.sin(angle) - (length * angular_velocity**2) * np.cos(angle)
    ay = length * angular_acceleration * np.cos(angle) - (length * angular_velocity**2) * np.sin(angle)
    return np.array([ax, ay])

# Inverted slider-crank mechanism parameters
length_crank = 1.0
length_slider = 2.0
angular_velocity_crank = 2.0  # rad/s
angular_acceleration_crank = 0.0  # rad/s^2

# Analysis for a range of crank angles
num_points = 100
crank_angles = np.linspace(0, 2 * np.pi, num_points)

# Calculate position, velocity, and acceleration vectors for each crank angle
position_vectors = np.array([position_vector(length_crank, angle) for angle in crank_angles])
velocity_vectors = np.array([velocity_vector(length_crank, angular_velocity_crank, angle) for angle in crank_angles])
acceleration_vectors = np.array([acceleration_vector(length_crank, angular_velocity_crank, angular_acceleration_crank, angle) for angle in crank_angles])

# Plotting the results
plt.figure(figsize=(12, 8))

# Plot the mechanism
plt.plot([0, position_vectors[-1, 0]], [0, position_vectors[-1, 1]], 'k-', label='Slider-Crank Mechanism')
plt.plot(position_vectors[:, 0], position_vectors[:, 1], 'bo', label='Crank Positions')
plt.quiver(position_vectors[:, 0], position_vectors[:, 1], velocity_vectors[:, 0], velocity_vectors[:, 1], color='r', scale=10, label='Velocity Vectors')
plt.quiver(position_vectors[:, 0], position_vectors[:, 1], acceleration_vectors[:, 0], acceleration_vectors[:, 1], color='g', scale=50, label='Acceleration Vectors')

plt.title('Inverted Slider-Crank Mechanism Analysis')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()
