import trimesh
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection

def load_mesh(file_path):
    return trimesh.load(file_path)

def calculate_height(mesh):
    return mesh.bounds[1][1] - mesh.bounds[0][1]

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
    
    # Create the slice
    slice = slice_at_height(mesh, slice_height)
    circumference = calculate_circumference(slice)
    
    # Print the circumference before plotting
    print(f"Bicep Circumference (before plot): {circumference:.2f} meters")

    # Check if the slice exists
    if slice is not None:
        # Extract the slice vertices and line segments
        vertices = slice.vertices
        # Create line segments from vertices for visualization
        lines = [[vertices[i], vertices[i + 1]] for i in range(len(vertices) - 1)]
        # Add the first and last vertex if the slice is closed
        if np.allclose(vertices[0], vertices[-1]):
            lines.append([vertices[-1], vertices[0]])
        lc = Line3DCollection(lines, colors='g', linewidths=2, linestyles=':')
        ax.add_collection3d(lc)
    
    plt.title(f"Slice at Height: {slice_height:.2f} meters")
    plt.xlabel('X axis (m)')
    plt.ylabel('Y axis (m)')
    ax.set_zlabel('Z axis (m)')
    plt.show()

# Example usage
if __name__ == "__main__":
    mesh_path = 'Realistic_White_Male_Low_Poly.obj'  # Update to your mesh file path
    mesh = load_mesh(mesh_path)
    height = calculate_height(mesh)
    
    # Estimate bicep slice height; adjust as needed
    bicep_height = mesh.bounds[1][1] - 0.3 * height  # Example: 30% down from the top
    visualize_slice_with_circumference(mesh, bicep_height)
