
#histogram of the rolling two dice at random
import matplotlib.pyplot as plt
import random
#returns the value of rolled two dies 
def dice_roll():
    return random.randint(1,12)+random.randint(1,12)
#collecting the data by rolling two dies 500 times
data=[dice_roll() for i in range (500)]
fig,ax=plt.subplots()
ax.hist(data,11)
plt.show()