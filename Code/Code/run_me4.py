# Import modules

import numpy as np
from scipy import misc
import imageio

import numpy as np
from sklearn.utils import shuffle




def read_scene(file_name):
	data_x = imageio.imread(file_name)

	return (data_x)

def HAC3():
	
	
	
	data_x = read_scene('../../Data/umass_campus_100x100x3.jpg')
	print('X = ', data_x.shape)

	flattened_image = data_x.ravel().reshape(data_x.shape[0] * data_x.shape[1], data_x.shape[2])
	print('Flattened image = ', flattened_image.shape)
	n_clusters_arr=[2, 5, 10, 25,50, 75, 100, 200]
	
	
	for t in range(len(n_clusters_arr)):
	
		data_y=read_scene('../Figures/HAC' + str(n_clusters_arr[t]) + '.jpg')
		input_image=data_y.ravel().reshape(data_x.shape[0] * data_x.shape[1], data_x.shape[2])
		arr1=np.array(flattened_image)
		arr2=np.array(input_image)
		mse = ((arr1 - arr2) ** 2).mean(axis=None)
		print('HAC: '+str(n_clusters_arr[t]))
		print(mse)

		
	return