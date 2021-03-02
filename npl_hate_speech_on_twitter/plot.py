import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
color = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("twitter-out.txt","r").read()
    lines = pullData.split('\n')
    
    values = [0,0,0]
    name = ['Baixa precisão','Negativo','Positivo']
    
    x = 0
    y = 0
    z = 0

    for l in lines:
        if "1" in l:
            x += 1
            values[2] = x
        elif "0"in l:
            y += 1
            values[1] = y
        else:
            z += 1
            values[0] = z
    print(sum(values))
    print(values)
    ax1.clear()
    ax1.scatter(name, values)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
