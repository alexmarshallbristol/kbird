import numpy as np
import matplotlib.pyplot as plt
import kbird # trigger auto-injection of the kBird colormap - makes it default

x = np.linspace(-3, 3, 256)
y = np.linspace(-3, 3, 256)
X, Y = np.meshgrid(x, y)
Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2)

plt.figure(figsize=(8, 6))

im = plt.imshow(Z, extent=[-3, 3, -3, 3], origin='lower')

plt.colorbar(im)

plt.title("Testing the Custom kBird Colormap")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.savefig("kbird_test_output.png", dpi=300, bbox_inches='tight')

plt.show()