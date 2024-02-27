import trimesh
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection

def load_mesh(file_path):
    return trimesh.load(file_path)

def slice_at_height(mesh, slice_height):
    slice = mesh.section(plane_origin=[0, slice_height, 0], plane_normal=[0, 1, 0])
    return slice

def calculate_circumference(slice):
    if slice is None:
        return 0
    polyline = slice.to_planar()[0]
    return polyline.length

def visualize_slice_with_circumference(mesh, slice_height):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Display the mesh
    mesh.show(axes=ax)
    
    # Create the slice and calculate circumference
    slice = slice_at_height(mesh, slice_height)
    circumference = calculate_circumference(slice)
    
    print(f"Wrist Circumference: {circumference:.2f} meters")

    # Check if the slice exists
    if slice is not None:
        vertices = slice.vertices
        lines = [[vertices[i], vertices[i + 1]] for i in range(len(vertices) - 1)]
        if np.allclose(vertices[0], vertices[-1]):
            lines.append([vertices[-1], vertices[0]])
        lc = Line3DCollection(lines, colors='r', linewidths=2, linestyles=':')
        ax.add_collection3d(lc)
    
    plt.title(f"Slice at Height for Wrist Circumference: {slice_height:.2f} meters")
    plt.show()

if __name__ == "__main__":
    mesh_path = 'Realistic_White_Male_Low_Poly.obj'  # Update to your mesh file path
    mesh = load_mesh(mesh_path)
    
    # Estimating wrist slice height
    # This is a rough approximation and may need adjustment
    # Assuming the wrist is located at about 15% up from the lowest point of the hand
    # This estimation will greatly vary based on the pose of the model
    wrist_height = mesh.bounds[0][1] + (mesh.bounds[1][1] - mesh.bounds[0][1]) * 0.85  # Adjust based on your model
    visualize_slice_with_circumference(mesh, wrist_height)