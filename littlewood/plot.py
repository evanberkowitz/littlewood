
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import colors


defaults = {
    'figsize'   : np.array([12,8]),
    'aspect'    : 1,
    'xlim'      : np.array([-2.88, 2.88]),
    'ylim'      : np.array([-2 , 2 ]),
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
    'bins'      : np.array([12,8]) * 2**6,

    # Points:
    'marker'    : ',', # comma means pixels
    'alpha'     : 1,
}

def setup_figure(fig, **options):

    opts = {**defaults, **options}

    if opts['tight_layout']:
        fig.tight_layout()
    plt.subplots_adjust(    left    =opts['adjust']['left'],
                            right   =opts['adjust']['right'],
                            top     =opts['adjust']['top'],
                            bottom  =opts['adjust']['bottom']
                        )

def setup_axis(ax, **options):
    opts = {**defaults, **options}
    ax.set_aspect(opts['aspect'])
    ax.set_xlim(opts['xlim'])
    ax.set_ylim(opts['ylim'])
    ax.get_xaxis().set_visible(opts['axisVisible'])
    ax.get_yaxis().set_visible(opts['axisVisible'])
    ax.set_facecolor('black')

def one_axis_figure(**options):
    opts = {**defaults, **options}
    fig, ax = plt.subplots(1,1, figsize=opts['figsize'])
    setup_figure(fig, **opts)
    setup_axis  (ax,  **opts)

    return fig, ax

def histogram(ax, roots, **options):
    opts = {**defaults, **options}
    degrees = roots.keys()
    flat = np.concatenate(list([roots[d].flatten() for d in degrees]))
    ax.hist2d(np.real(flat), np.imag(flat), bins=opts['bins'], norm=opts['norm'], cmap=opts['cmap'])

def points(ax, roots, **options):
    opts = {**defaults, **options}
    degrees = np.sort([k for k in roots.keys()])
    for z, d in enumerate(degrees):
        ax.plot(np.real(roots[d].flatten()), np.imag(roots[d].flatten()), linestyle='None',
                marker=opts['marker'],
                alpha=opts['alpha'],
                zorder=-z,
                )
