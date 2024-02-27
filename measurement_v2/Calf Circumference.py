import trimesh
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection

def load_mesh(file_path):
    # Load the mesh from a file
    return trimesh.load(file_path)

def calculate_height(mesh):
    # Calculate the total height of the mesh
    return mesh.bounds[1][1] - mesh.bounds[0][1]

def calculate_leg_length(mesh):
    # Simplified leg length calculation based on the model's height
    total_height = calculate_height(mesh)
    leg_length = total_height * 0.45  # Assuming legs constitute roughly 45% of total height
    return leg_length

def slice_at_height(mesh, slice_height):
    # Create a horizontal slice of the mesh at a given height
    slice = mesh.section(plane_origin=[0, slice_height, 0], plane_normal=[0, 1, 0])
    return slice

def calculate_circumference(slice):
    # Calculate the circumference of the slice
    if slice is None:
        return 0
    polyline = slice.to_planar()[0]
    return polyline.length

def visualize_slice_with_circumference(mesh, slice_height):
    # Visualize the mesh and the slice used to calculate the circumference
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Display the mesh
    mesh.show(axes=ax)
    
    # Generate and visualize the slice
    slice = slice_at_height(mesh, slice_height)
    circumference = calculate_circumference(slice)
    
    print(f"Calf Circumference: {circumference:.2f} meters")
    
    if slice is not None:
        vertices = slice.vertices
        lines = [[vertices[i], vertices[i + 1]] for i in range(len(vertices) - 1)]
        if np.allclose(vertices[0], vertices[-1]):
            lines.append([vertices[-1], vertices[0]])
        lc = Line3DCollection(lines, colors='g', linewidths=2, linestyles=':')
        ax.add_collection3d(lc)
    
    plt.title(f"Slice at Height: {slice_height:.2f} meters")
    plt.show()

if __name__ == "__main__":
    mesh_path = 'Realistic_White_Male_Low_Poly.obj'  # Update to your mesh file path
    mesh = load_mesh(mesh_path)
    height = calculate_height(mesh)
    
    # Simplified estimation for calf height, adjust based on your model specifics
    ankle_height = mesh.bounds[0][1] + 0.1 * calculate_leg_length(mesh)  # Slightly above the lowest point
    calf_height = ankle_height + 0.25 * calculate_leg_length(mesh)  # Adjust based on anatomy
    
    visualize_slice_with_circumference(mesh, calf_height)
