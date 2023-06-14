
"""Parameters related to model training, dataset etc"""

# Training hyperparameters
INPUT_SIZE = 784
NUM_CLASSES = 10
LEARNING_RATE = 0.001
BATCH_SIZE = 64
MIN_EPOCHS = 1
MAX_EPOCHS = 3

# Dataset
DATA_DIR = "dataset/"
NUM_WORKERS = 4

# Computer
ACCELERATOR = "gpu"
DEVICES = [0]
PRECISION = 16