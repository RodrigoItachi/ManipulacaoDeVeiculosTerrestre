import os

os.environ["MPLCONFIGDIR"] = os.getcwd() + "/configs/"

import tensorflow as tf
from tensorflow.python.compiler.tensorrt import trt_convert as trt
from tensorflow import keras
import json
import numpy as np
from pathlib import Path

# Install pose estimation model https://github.com/NVIDIA-AI-IOT/trt_pose
import trt_pose.coco
import trt_pose.models
import torch
import torch2trt

MODELS_PATH = Path(".") / "ManipulacaoDeVeiculosTerrestre" / "models"

def install_pck():
    