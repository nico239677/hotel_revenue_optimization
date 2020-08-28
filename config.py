import os
import random
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Set Print Option
desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 42)

# constant
filename = ''
URL = ''
PATH_DB = os.path.join(os.getcwd()+'/Database', filename)
