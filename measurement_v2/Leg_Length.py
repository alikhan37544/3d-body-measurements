import trimesh
import numpy as np

def load_mesh(file_path):
    return trimesh.load(file_path)

def calculate_leg_length(mesh):
    # Assuming the Y-axis represents the vertical direction in your model
    
    # Find the lowest point of the mesh, which could be the bottom of the foot
    lowest_point = mesh.bounds[0][1]
    
    # Estimating the top of the leg (hip joint) as a high point on the mesh
    # This is a simplification and may need adjustment based on the model's pose
    # Here, we assume the hip joint is around the top 10% of the Y-axis of the model
    hip_height_estimate = mesh.bounds[1][1] - (mesh.bounds[1][1] - mesh.bounds[0][1]) * 0.1

    leg_length = hip_height_estimate - lowest_point
    return leg_length

if __name__ == "__main__":
    mesh_path = 'Realistic_White_Male_Low_Poly.obj'  # Update to your mesh file path
    mesh = load_mesh(mesh_path)
    leg_length = calculate_leg_length(mesh)
    print(f"Leg Length: {leg_length:.2f} meters")
