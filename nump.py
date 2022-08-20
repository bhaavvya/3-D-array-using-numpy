import numpy as np
arr_3d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr_3d.ndim)
print(arr_3d)
for i in np.nditer(arr_3d):
    print(i)