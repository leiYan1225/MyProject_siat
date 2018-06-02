import numpy as np
import tensorflow as tf
import pandas as pd
import reader

DATA_PATH = "F:\datasets\PTB_data"
train_data, valid_data, test_data, _ = reader.ptb_raw_data(DATA_PATH)
print(np.shape(test_data))


