import trimesh
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection

def load_mesh(file_path):
    # Load and return the mesh
    return trimesh.load(file_path)

def calculate_height(mesh):
    # Calculate and return the height of the mesh
    return mesh.bounds[1][1] - mesh.bounds[0][1]

def slice_at_height(mesh, slice_height):
    # Slice the mesh at a given height and return the slice
    slice = mesh.section(plane_origin=[0, slice_height, 0], plane_normal=[0, 1, 0])
    return slice

def calculate_circumference(slice):
    # Calculate and return the circumference of the slice
    if slice is None:
        return 0
    polyline = slice.to_planar()[0]
    return polyline.length

def visualize_slice_with_circumference(mesh, slice_height):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Display the mesh
    mesh.show(axes=ax)
    
    # Create and visualize the slice
    slice = slice_at_height(mesh, slice_height)
    circumference = calculate_circumference(slice)
    
    # Print the circumference
    print(f"Thigh Circumference: {circumference:.2f} meters")

    if slice is not None:
        vertices = slice.vertices
        lines = [[vertices[i], vertices[i + 1]] for i in range(len(vertices) - 1)]
        if np.allclose(vertices[0], vertices[-1]):
            lines.append([vertices[-1], vertices[0]])
        lc = Line3DCollection(lines, colors='r', linewidths=2, linestyles=':')
        ax.add_collection3d(lc)
    
    plt.title(f"Slice at Height: {slice_height:.2f} meters")
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    ax.set_zlabel('Z axis')
    plt.show()

if __name__ == "__main__":
    mesh_path = 'Realistic_White_Male_Low_Poly.obj'  # Update this path to your .obj file location
    mesh = load_mesh(mesh_path)
    height = calculate_height(mesh)
    
    # Estimate thigh slice height; this may need adjustment
    thigh_height = mesh.bounds[0][1] + 0.25 * height  # Adjust this factor based on your model
    visualize_slice_with_circumference(mesh, thigh_height)
