# Import modules

import numpy as np
from scipy import misc
import imageio
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
import numpy as np
from sklearn.utils import shuffle
import run_me2
import run_me3
import run_me4
import run_me5

def read_scene():
	data_x = imageio.imread('../../Data/umass_campus.jpg')

	return (data_x)

if __name__ == '__main__':
	
	
	data_x = read_scene()
	print('X = ', data_x.shape)

	flattened_image = data_x.ravel().reshape(data_x.shape[0] * data_x.shape[1], data_x.shape[2])
	print('Flattened image = ', flattened_image.shape)
	
	
	
#===============================================================================
# Q1 : Code for K-means with varying values for n_clusters
#===============================================================================

			
	print('Implement k-means here ...')
	
	arr=[2, 5, 10, 25,50, 75, 100, 200]
	
	for n in range(len(arr)):
		kmeans = KMeans(n_clusters=arr[n], random_state=5, max_iter=100).fit(flattened_image)
 		
		print(kmeans.cluster_centers_)
		img_arr=kmeans.predict(flattened_image)
		centroid_arr=kmeans.cluster_centers_
		print(img_arr[0:10])
		print(centroid_arr[1])
		new_img=[]
		for i in range(len(img_arr)):
			new_img.append(centroid_arr[img_arr[i]])
  			
		
		for i in range(flattened_image.shape[0]):
			flattened_image[i:,]=kmeans.cluster_centers_[kmeans.predict(flattened_image[i:,])]
		ni=np.array(new_img)
		print('kmeans:'+str(arr[n]))
  	
		reconstructed_image = ni.ravel().reshape(data_x.shape[0], data_x.shape[1], data_x.shape[2])
		print('Reconstructed image = ', reconstructed_image.shape)
		imageio.imsave('../Figures/kmeans'+str(arr[n])+'.jpg',reconstructed_image)

#===============================================================================
# Code ends here
#===============================================================================

#===============================================================================
# Q2 : Code for HAC with varying values for affinity and linkage with 
# n_cluster=2
#===============================================================================
	run_me2.HAC1()
	
#===============================================================================
# Code ends here
#===============================================================================

#===============================================================================
# Q3 : Code for HAC with varying values of n_cluster
#===============================================================================
	run_me3.HAC2()
	
#===============================================================================
# Code ends here
#===============================================================================

#===============================================================================
# Q4(a) : Reconstruction Error for HAC with varying values of n_cluster
#===============================================================================
	run_me4.HAC3()
	
#===============================================================================
# Code ends here
#===============================================================================

#===============================================================================
# Q4(b) : Reconstruction Error for K-means with varying values of n_cluster
#===============================================================================
	run_me5.KMeans()
	
#===============================================================================
# Code ends here
#===============================================================================

