import math
import matplotlib.pyplot as plt
import numpy as np
n = 1000
X = np.random.uniform(-1,1,n)
Y = np.random.uniform(-1,1,n)

inc = X**2 + Y**2 <= 1
pi = inc.sum()/n*4
fig = plt.figure()

circle = np.linspace(0,2*np.pi,100)
ax = fig.add_subplot()
ax.fill(np.sin(circle), np.cos(circle))
# ax.plot(X,Y, "rx")
cols = ["red" if h else "blue" for h in inc]
ax.scatter(X,Y,marker="x", c=cols)
plt.show()