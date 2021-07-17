import numpy as np
import matplotlib.pyplot as plt

plt.xkcd()

points = []
lines = []
n = sumX = sumY = sumXY = sumX2 = 0

def updateData(x,y):
    global n, sumX, sumY, sumXY, sumX2, m, b
    n += 1
    sumX += x
    sumY += y
    sumXY += x*y
    sumX2 += pow(x,2)

def linearRegression():
    global lines
    if n > 2:
        li = lines[0].pop(0)
        li.remove()
        lines.pop()

    if n > 1:
        m = ( (n*sumXY) - (sumX*sumY) ) / ( (n*sumX2) - pow(sumX,2) )
        b = (sumY - (m*sumX)) / n
        x = np.linspace(0,10,500)
        y = m*x + b
        line = plt.plot(x,y,'c', label='y={:.4f}x + {:.4f}'.format(m,b))
        plt.legend(loc='upper left')
        lines.append(line)

def onclick(event):
    print('({:.4f}, {:.4f})'.format(event.xdata,event.ydata))
    points.append([event.xdata, event.ydata])
    updateData(event.xdata, event.ydata)
    linearRegression()
    ax.plot(event.xdata, event.ydata,'o')
    plt.draw()

print('Points:')
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim((0, 10))
ax.set_ylim((0, 10))
plt.title('Linear Regression Model')
plt.xlabel('x-axis', color='#1C2833')
plt.ylabel('y-axis', color='#1C2833')
plt.gcf().canvas.mpl_connect('button_press_event', onclick)
plt.grid()
plt.show()
