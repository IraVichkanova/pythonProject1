import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

##Задание 1
x = [1, 2, 3, 4, 5, 6, 7]
y = [3.5, 3.8, 4.2, 4.5, 5, 5.5, 7]
plt.plot(x,y)
plt.show()

plt.scatter(x,y)
plt.show()

##Задание 2
t = np.linspace(0, 10, num=51, endpoint = True, retstep = False)
print(t)

f = np.cos(t)
print(f)

plt.plot(t,f)
plt.show()

plt.plot(t,f)
plt.title("График f(t)")
plt.xlabel("Значение t")
plt.ylabel("Значение f")
plt.xlim(0.5, 9.5)
plt.ylim(-2.5, 2.5)
plt.show()

##Задание 3
x = np.linspace(-3, 3, 51)
print(x)

y1 = x*2
y2 = 2*x+0.5
y3 = -3*x-1.5
y4 = np.sin(x)

print(y1)
print(y2)
print(y3)
print(y4)

fig, ax = plt.subplots(2, 2)
ax1, ax2, ax3, ax4 = ax.flatten()
ax1.plot(x,y1, color = 'orange')
ax2.plot(x,y2, color = 'purple')
ax3.plot(x,y3, color = 'red')
ax4.plot(x,y4, color = 'green')
ax1.set_title("График $y1$")
ax2.set_title("График $y2$")
ax3.set_title("График $y3$")
ax4.set_title("График $y4$")

ax1.set_xlim([-5, 5])
fig.set_size_inches(8, 6)
plt.subplots_adjust(wspace=0.3, hspace=0.3)
plt.show()

