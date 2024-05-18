#exploring matplotlib with random values x,y

import matplotlib.pyplot as plt
import os
#%matplotlib inline
x=[1,2,3,4,5]
y=[1,2,3,4,5]
fig,ax=plt.subplots()
ax.scatter(x,y)
ax.set_title("title")
plt.show()

