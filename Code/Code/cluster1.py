
#===============================================================================
# Cluster centroid value calculation
#===============================================================================

def get_cluster_arr(len_img_arr,img_arr,flattened_image,n_clusters):
    cluster_arr=[]
    print(img_arr)
    
    #len_arr=[]
    #arr_val=[]
    for i in range(n_clusters):
        len=0
        arr_entry=[0,0,0]
        cluster=[]
        for k in range(len_img_arr):
            if img_arr[k]==i:
                arr_entry[0]=arr_entry[0]+flattened_image[k][0]
                arr_entry[1]=arr_entry[1]+flattened_image[k][1]
                arr_entry[2]=arr_entry[2]+flattened_image[k][2]
                len=len+1
        cluster=[arr_entry[0]/float(len),arr_entry[1]/float(len),arr_entry[2]/float(len)]
        print('cluster')
        print(cluster)
        cluster_arr.append(cluster)
    return cluster_arr