
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import colors


defaults = {
    'figsize'   : np.array([6,6]),
    'aspect'    : 1,
    'xlim'      : np.array([-2.66, 2.66]),
    'ylim'      : np.array([-1.8 , 1.8 ]),
    'dpi'       : 300,
    'facecolor' : 'black',
    'axisVisible' : False,
    'tight_layout' : True,
    'adjust'    : {
        'left'  : 0.,
        'right' : 1.,
        'top'   : 1.,
        'bottom': 0.
    },
    # Histogram:
    'norm'      : colors.LogNorm(),
    'cmap'      : 'inferno',
    'bins'      : 128,
}

def _figureSetup(opts):

    fig = plt.figure(figsize=opts['figsize'])
    ax = fig.add_subplot(111)

    ax.set_aspect(opts['aspect'])
    ax.set_xlim(opts['xlim'])
    ax.set_ylim(opts['ylim'])
    ax.get_xaxis().set_visible(opts['axisVisible'])
    ax.get_yaxis().set_visible(opts['axisVisible'])
    ax.set_facecolor('black')
    if opts['tight_layout']:
        fig.tight_layout()
    plt.subplots_adjust(    left    =opts['adjust']['left'],
                            right   =opts['adjust']['right'],
                            top     =opts['adjust']['top'],
                            bottom  =opts['adjust']['bottom']
                        )
    return fig, ax

def histogram(roots, options=dict()):
    opts = defaults
    for k in options:
        opts[k] = options[k]

    fig, ax = _figureSetup(opts)

    degrees = roots.keys()
    flat = np.concatenate(list([roots[d].flatten() for d in degrees]))
    ax.hist2d(np.real(flat), np.imag(flat), bins=opts['bins'], norm=opts['norm'], cmap=opts['cmap'])

def points(roots, options=dict()):
    opts = defaults
    for k in options:
        opts[k] = options[k]

    fig, ax = _figureSetup(opts)
    degrees = np.sort([k for k in roots.keys()])
    for d in degrees[::-1]:
        ax.plot(np.real(roots[d].flatten()), np.imag(roots[d].flatten()), lineStyle='None', marker=',') # , means pixels
