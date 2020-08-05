import matplotlib.pyplot as plt

import pandas as pd
data_file = './cox_etal_2013.txt'  #Data file
data = np.genfromtxt(data_file,delimiter=',')

f.image_filename = 'myplot4.png'
f.plot_cylinders_3D(animate=False, save=True, time_idx=0)
