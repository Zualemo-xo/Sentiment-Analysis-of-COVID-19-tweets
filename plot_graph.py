import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("twitter-out.txt","r").read()
    lines = pullData.split('\n')

    xar = []
    yar = []
    zar=[]

    x = 0
    y = 0
    z = 0

    for l in lines[:]:
        x += 1
        if "pos" in l:
            y += 1
        elif "neg" in l:
            #y -= 1
            z+=1

        xar.append(x)
        yar.append(y)
        zar.append(z)
        
    ax1.clear()
    ax1.plot(xar,yar,label="positive",)
    ax1.plot(xar,zar,label="negative")
    plt.xlabel('Total number of tweets')
    plt.ylabel('Respective count of each sentiment');
    plt.legend(loc='best')
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
