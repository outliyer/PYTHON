#to learn how to plot real time data from the python script
import random
import csv
from itertools import count
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
x_values=[]
y_values=[]
index=count()#generating the sequential values
#appending the values in the list
plt.style.use('seaborn-v0_8')

def animate(i):
   x_values.append(next(index))
   y_values.append(random.randint(0,5))
   plt.cla()
   plt.plot(x_values,y_values,label='random_plot')
   plt.legend()
ani=FuncAnimation(plt.gcf(),animate,interval=1000)
plt.tight_layout()
plt.show()