# -*- coding:utf-8 -*-
"""
Author : Ronghong Ji
Time   : 2022/11/11
E-mail : jironghong1998@gmail.com
Desc.  :
"""

from re import X
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file='com'
matrix=np.loadtxt(file)
x_min=np.min(matrix[:,0])
x_max=np.max(matrix[:,0])
y_min=np.min(matrix[:,1])
y_max=np.max(matrix[:,1])
z_min=np.min(matrix[:,2])
z_max=np.max(matrix[:,2])
print("XYZ directions: "+ "\n" + "X direction: %5.3f %5.3f"%(x_min,x_max)+ "\n" +"Y direction: %5.3f %5.3f" %(y_min,y_max) \
+ "\n" + "Z direction: %5.3f %5.3f"%(z_min,z_max)+ "\n" )
number_of_species=input("please input the number of each species: ")
number_of_species=number_of_species.split()
number_of_species=[int(x) for x in number_of_species]
sum_species=sum(number_of_species)
frames=input("please input the number of frames: ")
frames=int(frames)
count=0

for i in range(frames):
    a_matrix=matrix[i*sum_species:i*sum_species+number_of_species[0]:,:]
    b_matrix=matrix[i*sum_species+number_of_species[0]:i*sum_species+number_of_species[0]+number_of_species[i]:,:]
    c_matrix=matrix[i*sum_species+number_of_species[0]+number_of_species[1]:(i+1)*sum_species:,:]

a_z = a_matrix[:,2]
b_z = b_matrix[:,2]
c_z = c_matrix[:,2]
start = -26
end = 26
interval = 1
V = (x_max - x_min)*(y_max - y_min)

# a类型
newlist_a = []
while start <= end:
    sub=[]
    
    for i in a_z:
        if (i<=start+interval) & (i>start):
            sub.append(i)
    if sub != []:
        density = len(sub)/V
        newlist_a.append(density)

    start=start+interval 

x = list(range(-26,26,1))
plt.plot(x,newlist_a)
plt.title("a")
plt.savefig('./a.jpg')
plt.show()

# b类型
newlist_b = []
while start <= end:
    sub=[]
    
    for i in b_z:
        if (i<=start+interval) & (i>start):
            sub.append(i)
    if sub != []:
        density = len(sub)/V
        newlist_b.append(density)

    start=start+interval 

x = list(np.arange(-26,26,1))
plt.plot(x,newlist_b)
plt.title("b")
plt.savefig('./b.jpg')
plt.show()

# c类型
newlist_c = []
while start <= end:
    sub=[]
    
    for i in c_z:
        if (i<=start+interval) & (i>start):
            sub.append(i)
    if sub != []:
        density = len(sub)/V
        newlist_c.append(density)

    start=start+interval 

x = list(np.arange(-26.5,26.5,1))
plt.plot(x,newlist_c)
plt.title("c")
plt.savefig('./c.jpg')
plt.show()