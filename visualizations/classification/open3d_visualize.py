import os
import numpy as np
import open3d


class Visualizer:
    dataset_path = 'shapenetcore_partanno_segmentation_benchmark_v0'
    map_label_to_rgb = {
        1: [0, 255, 0],
        2: [0, 0, 255],
        3: [255, 0, 0],
        4: [255, 0, 255],  # purple
        5: [0, 255, 255],  # cyan
        6: [255, 255, 0],  # yellow
    }

    def __init__(self):
        pass

    def visualize(self, obj_category, obj_id):
        # Concat paths
        pts_path = os.path.join(Visualizer.dataset_path, obj_category,
                                'points', obj_id + '.pts')
        label_path = os.path.join(Visualizer.dataset_path, obj_category,
                                  'points_label', obj_id + '.seg')

        # Read point cloud
        point_cloud = open3d.read_point_cloud(pts_path, format='xyz')
        print(point_cloud)

        # Read label and map to color
        labels = np.loadtxt(label_path)
        colors = np.array(
            [Visualizer.map_label_to_rgb[label] for label in labels])
        point_cloud.colors = open3d.Vector3dVector(colors)
        open3d.draw_geometries([point_cloud])


if __name__ == '__main__':
    v = Visualizer()
    v.visualize('02691156', '1a04e3eab45ca15dd86060f189eb133')
