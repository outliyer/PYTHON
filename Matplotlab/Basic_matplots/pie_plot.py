#to learn how to plot a pie chart
from matplotlib import pyplot as plt
import os
plt.style.use('seaborn-v0_8')
spits=[15,34,12,24,23]
labels=['egg','water','fruit','tea','lemon']
#to show % we have a string formate we should use
explode=[0,0,0,0,0.15]
kolours=['#dda0dd','#afeeee','#ffc0cb','#db7093','#eee8aa']
plt.pie(spits,labels=labels,colors=kolours,shadow=True,explode=explode,autopct='%1.1f%%')
plt.show()
