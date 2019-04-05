# Import modules

import numpy as np
from scipy import misc
import imageio
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
import numpy as np
from sklearn.utils import shuffle
import cluster1



def read_scene():
	data_x = imageio.imread('../../Data/umass_campus_100x100x3.jpg')

	return (data_x)

def HAC2():
	
	
	
	data_x = read_scene()
	print('X = ', data_x.shape)

	flattened_image = data_x.ravel().reshape(data_x.shape[0] * data_x.shape[1], data_x.shape[2])
	print('Flattened image = ', flattened_image.shape)
	n_clusters_arr=[2, 5, 10, 25,50, 75, 100, 200]
	
	for t in range(len(n_clusters_arr)):
	
		linkage_val='complete'
		affinity_val='euclidean'
		
		n_clusters_val=n_clusters_arr[t]
		flattened_image_sample = shuffle(flattened_image, random_state=0)[:1000]
		ac = AgglomerativeClustering(n_clusters=n_clusters_val, affinity=affinity_val, linkage=linkage_val).fit(flattened_image_sample)
				
	
		img_arr = []
				
		img_arr = ac.fit_predict(flattened_image)
	
	
		cluster_arr=cluster1.get_cluster_arr(len(img_arr),img_arr,flattened_image,n_clusters_val)
		new_img=[]
		for k in range(len(img_arr)):
			for m in range(n_clusters_val):
				if img_arr[k]==m:
					new_img.append(cluster_arr[m])
	
		ni=np.array(new_img)
		print('HAC : '+str(n_clusters_val))
		reconstructed_image = ni.ravel().reshape(data_x.shape[0], data_x.shape[1], data_x.shape[2])
		print('Reconstructed image = ', reconstructed_image.shape)
	
		imageio.imsave('../Figures/HAC'+str(n_clusters_val)+'.jpg',reconstructed_image)
	
	return

		
