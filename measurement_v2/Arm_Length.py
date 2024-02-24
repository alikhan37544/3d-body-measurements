import trimesh
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def load_mesh(file_path):
    """Load a 3D mesh model from the specified file path."""
    return trimesh.load(file_path)

def calculate_arm_length(mesh):
    """Estimate the arm length of a 3D humanoid model."""
    # Assuming arms are positioned along the body
    # Calculate model height
    model_height = mesh.bounds[1][1] - mesh.bounds[0][1]
    
    # Estimate shoulder and wrist heights as percentages of total model height
    shoulder_height_percentage = 0.9
    wrist_height_percentage = 0.15
    
    shoulder_height = mesh.bounds[1][1] - model_height * shoulder_height_percentage
    wrist_height = mesh.bounds[1][1] - model_height * wrist_height_percentage

    # Find points near the estimated shoulder height and wrist height
    shoulder_points = mesh.vertices[(mesh.vertices[:, 1] < shoulder_height + 0.05) & (mesh.vertices[:, 1] > shoulder_height - 0.05)]
    wrist_points = mesh.vertices[(mesh.vertices[:, 1] < wrist_height + 0.05) & (mesh.vertices[:, 1] > wrist_height - 0.05)]
    
    if len(shoulder_points) == 0 or len(wrist_points) == 0:
        print("Could not find suitable points for shoulder or wrist.")
        return None
    
    # Use the most extreme points as the shoulder and wrist locations
    shoulder_point = shoulder_points[np.argmax(shoulder_points[:, 0])]
    wrist_point = wrist_points[np.argmin(wrist_points[:, 0])]
    
    # Calculate the Euclidean distance between these points as an approximation of arm length
    arm_length = np.linalg.norm(shoulder_point - wrist_point)
    return arm_length

def visualize_arm_length(mesh, arm_length):
    """Visualize the 3D model with a line representing the calculated arm length."""
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot the mesh
    mesh.show(axes=ax)
    
    # Annotations for arm length
    ax.text(0, 0, 0, f'Estimated Arm Length: {arm_length:.2f} meters', color='red')
    
    plt.show()

if __name__ == "__main__":
    mesh_path = 'Realistic_White_Male_Low_Poly.obj'  # Update this path to your .obj file location
    mesh = load_mesh(mesh_path)
    arm_length = calculate_arm_length(mesh)
    
    if arm_length is not None:
        print(f"Estimated Arm Length: {arm_length:.2f} meters")
        visualize_arm_length(mesh, arm_length)
    else:
        print("Failed to estimate arm length.")
