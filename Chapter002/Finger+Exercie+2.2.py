import numpy as np

x = input("What's the value of x?  ")
y = input("What's the value of y?  ")
z = input("What's the value of z?  ")
print ('x =', x)
print ('y =', y)
print ('z =', z)

xyz = np.array([x,y,z])
odds = np.array([0,0,0])

size_xyz = len(xyz)

j = 0
for i in range (0,size_xyz):
    if int(xyz[i])%2 == 0:
        print (xyz[i],'is not odd')
    else:
        myvalue = int(xyz[i])
        #print('my value is',myvalue)
        odds[j] = myvalue
        #print(odds)
        print (xyz[i],'is odd')
        j = j+1
        
if j == 0:
    print ('none of the numbers were odd')
else:
    #print(odds)
    MaxOdd = max(odds)
    print('the greater odd is',MaxOdd)
