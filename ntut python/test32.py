import numpy as np

def test32(): 
    x = np.ones([2, 3]) 
    print(x)
    y = x.reshape([3, 2]) 
    print(y)
    z=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]])
    print(z[:,::-1]) 
    print(z[:,0])
    print(z[:,1])
    print(z[:,2:3])
    #np.ones([2, 3]) 設定 2x3 值均為 1
    # x.reshape([3, 2])將 2x3 改為 3x2 
    #z[:,0] 是取矩陣X的所有行的第0列的元素，
    #z[:,1] 是取所有行的第1列的元素。
    #z[:,m:n:s]即取矩陣X的所有行中的的第m到n-1列資料，含左不含右。
    # s 是 step, 空的就是全取，-1是倒轉
    #z[0,:]就是取矩陣X的第0行的所有元素，X[1,:]取矩陣X的第一行的所有元素。