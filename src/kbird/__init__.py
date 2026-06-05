import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap
from contextlib import contextmanager

_stops = [0.0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1.0]
_red   = [0.2082, 0.0592, 0.0780, 0.0232, 0.1802, 0.5301, 0.8186, 0.9956, 0.9764]
_green = [0.1664, 0.3599, 0.5041, 0.6419, 0.7178, 0.7492, 0.7328, 0.7862, 0.9832]
_blue  = [0.5293, 0.8684, 0.8385, 0.7914, 0.6425, 0.4662, 0.3499, 0.1968, 0.0539]

_cdict = {
    'red':   [[_stops[i], _red[i], _red[i]] for i in range(len(_stops))],
    'green': [[_stops[i], _green[i], _green[i]] for i in range(len(_stops))],
    'blue':  [[_stops[i], _blue[i], _blue[i]] for i in range(len(_stops))]
}

kbird_cmap = LinearSegmentedColormap('kBird', _cdict)

def set():
    if 'kBird' not in mpl.colormaps:
        mpl.colormaps.register(kbird_cmap, name='kBird')
        mpl.colormaps.register(kbird_cmap, name='kbird')

    mpl.rcParams['image.cmap'] = 'kBird'


@contextmanager
def style():
    """Context manager to temporarily apply kBird defaults."""
    # Register if not already done
    if 'kBird' not in mpl.colormaps:
        mpl.colormaps.register(kbird_cmap, name='kBird')
        
    old_cmap = mpl.rcParams['image.cmap']
    mpl.rcParams['image.cmap'] = 'kBird'
    try:
        yield
    finally:
        # Restore original default afterward
        mpl.rcParams['image.cmap'] = old_cmap


__all__ = ['kbird', 'set']