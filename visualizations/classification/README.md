# Open3D-PointNet

[PointNet][pointnet] implementation and visualization with [Open3D][open3d],
an open-source library that supports rapid development of software that deals
with 3D data. As part of the Open3D ecosystem, this repository demonstrates how
Open3D can be used for ML/DL research projects.

This repository is forked from
[`fxia22`'s PyTorch implementation](https://github.com/fxia22/pointnet.pytorch).

![seg](misc/o3d_visualize.png)

# Changelog

1. Added CPU support for non-cuda-enabled devices.
2. Used Open3D point cloud loader for loading PointNet datasets (`datasets.py`).
3. Added example for PointNet inference with Open3D Jupyter visualization
   (`open3d_pointnet_inference.ipynb`).
4. Added example for native OpenGL visualization with Open3D (`open3d_visualize.py`).

# Setup

```bash
# Install Open3D, must be v0.4.0 or above for Jupyter support
pip install open3d-python

# Install PyTorch
# Follow: https://pytorch.org/

# Install other dependencies
pip install -r requirements.txt
```

Now, launch

```bash
jupyter notebook
```

and run `open3d_pointnet_inference.ipynb`. All datasets and pre-trained models
shall be downloaded automatically. If you run into issues downloading files,
please run `download.py` separately.

[open3d]: https://github.com/IntelVCL/Open3D
[pointnet]: https://arxiv.org/abs/1612.00593
