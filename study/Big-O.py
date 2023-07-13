import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 10)

plt.plot(x, 2**x)
plt.plot(x, x**3)
plt.plot(x, x**2)
plt.plot(x, x)
plt.plot(x, x*np.log(x))
plt.show()
