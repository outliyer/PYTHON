import os 
from matplotlib import pyplot as plt
plt.style.use('seaborn-v0_8')
minutes = [1,2,3,4,5]
player_1=[2,2,3,3,2]
player_2=[2,1,1,2,4]
player_3=[3,2,3,3,4]
kolours=['#dda0dd','#afeeee','#ffc0cb']
label=['orange','blue','purple']
plt.stackplot(minutes,player_1,player_2,player_3,colors=kolours,labels=label)
plt.legend(loc=(0.035,0.83))#passing the cooridinates to shown in the figure
plt.show()
