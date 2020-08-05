#process_data.py
import numpy as np
import scipy.interpolate
import pickle as pkl
from taco_vis import FLOW
#Read in Cox et al. (2013) dataset
data_file = './cox_etal_2013.txt'  #Data file
data = np.genfromtxt(data_file,delimiter=',')
#Regrid the data down (too high resolution to be practically plotted as is)
r   , t      = np.linspace(0,1,data.shape[0]), np.linspace(0,1,data.shape[1])
time, radius = np.linspace(0,1,2000)         , np.linspace(0,1,16)
func = scipy.interpolate.RectBivariateSpline(r,t,data)
u = func(radius,time)
#Initialise FLOW class
f = FLOW(u)
# save intermediate results for later visualization
with open('processed_data.pkl', 'wb') as filehandle:
        pkl.dump(f, filehandle)
