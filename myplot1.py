
import matplotlib.pyplot as plt

import pandas as pd
data_file = './cox_etal_2013.txt'  #Data file
data = np.genfromtxt(data_file,delimiter=',')

f.image_filename = 'myplot1.png'

plt.plot(u)
plt.colorbar()
plt.xlabel('Time(years)')
plt.ylabel('Radius(km)')
