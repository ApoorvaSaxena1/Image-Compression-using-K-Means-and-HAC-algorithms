# Import modules

import numpy as np
from scipy import misc
import imageio
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
import numpy as np
from sklearn.utils import shuffle



def read_scene():
	data_x = imageio.imread('../../Data/umass_campus_100x100x3.jpg')

	return (data_x)

def HAC1():
	
	data_x = read_scene()
	print('X = ', data_x.shape)

	flattened_image = data_x.ravel().reshape(data_x.shape[0] * data_x.shape[1], data_x.shape[2])
	print('Flattened image = ', flattened_image.shape)
	
	arr1 = ['ward', 'complete', 'average']
	for i in range(len(arr1)):
		if 'ward' in arr1[i]:
			arr2 = ['euclidean']
		else:
			arr2 = ['euclidean', 'l1', 'l2', 'manhattan', 'cosine']
			
		for j in range(len(arr2)):
	
	
			flattened_image_sample = shuffle(flattened_image, random_state=0)[:1000]
			ac = AgglomerativeClustering(n_clusters=2, affinity=arr2[j], linkage=arr1[i]).fit(flattened_image_sample)
			

			img_arr = []
			
			img_arr = ac.fit_predict(flattened_image)
			print(arr2[j])
			print(arr1[i])  
			arr_val0=[0,0,0]
			arr_val1=[0,0,0]
			len0=0
			len1=0
			print(len(img_arr))
			for k in range(len(img_arr)):
				if img_arr[k]==0:
					arr_val0[0]=arr_val0[0]+flattened_image[k][0]
					arr_val0[1]=arr_val0[1]+flattened_image[k][1]
					arr_val0[2]=arr_val0[2]+flattened_image[k][2]
					len0=len0+1
				if img_arr[k]==1:
					arr_val1[0]=arr_val0[0]+flattened_image[k][0]
					arr_val1[1]=arr_val0[1]+flattened_image[k][1]
					arr_val1[2]=arr_val0[2]+flattened_image[k][2]
					len1=len1+1
			cluster_val0=[arr_val0[0]/float(len0),arr_val0[1]/float(len0),arr_val0[2]/float(len0)]
			cluster_val1=[arr_val1[0]/float(len1),arr_val1[1]/float(len1),arr_val1[2]/float(len1)]
			new_img=[]
			for k in range(len(img_arr)):
				if img_arr[k]==0:
					new_img.append(cluster_val0)
				if img_arr[k]==1:
					new_img.append(cluster_val1)
			ni=np.array(new_img)
			print('hac: '+str(arr1[i])+str(arr2[j]))
			reconstructed_image = ni.ravel().reshape(data_x.shape[0], data_x.shape[1], data_x.shape[2])
			print('Reconstructed image = ', reconstructed_image.shape)
			
			imageio.imsave('../Figures/hac'+str(arr1[i])+str(arr2[j])+'.jpg',reconstructed_image)
			
	return

		
			
