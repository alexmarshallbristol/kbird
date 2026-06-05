# kBird

`kBird` brings CERN's **kBird** colormap into `matplotlib`. It registers the colormap and sets it as your global default.

---

## How to use

### 1. Global default in matplotlib

To use `kBird`, simply import the library and call `set()`. 

```python

import kbird
kbird.set()

# All plots will use kBird instead of viridis
plt.imshow(Z) 
```

### 2. Using kBird inside a specific block

If you do not want to change your global `matplotlib` defaults and only want to use `kBird` for a single plot, you can use the `style()` context manager:

```python
import kbird
import matplotlib.pyplot as plt

# Only plots generated inside this block will use kBird
with kbird.style():
    plt.imshow(Z)
    plt.show()

# Any plot out here will fall back to your standard matplotlib default
plt.imshow(Z) 

```

### 3. Manual Colormap Access

If you prefer to pass the colormap explicitly to `matplotlib` functions, you can import the colormap object directly:

```python
import matplotlib.pyplot as plt
from kbird import kbird_cmap

plt.imshow(Z, cmap=kbird_cmap)

```

---

## License

This project is licensed under the MIT License.