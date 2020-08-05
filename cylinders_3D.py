import numpy as np
import scipy.interpolate
import matplotlib.pyplot as plt
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
#Up the speed of texture advection
f.speed = 5

#Animate
f.image_filename = 'myplot1.png'
f.plot_cylinders_3D(animate=False, save=True, time_idx=0)
