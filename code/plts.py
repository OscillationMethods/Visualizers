"""Plot functions for oscillation methods visualizers."""

import warnings
from itertools import repeat

import numpy as np

from fooof.plts.utils import add_shades
from neurodsp.plts.utils import check_ax

###################################################################################################
###################################################################################################

def plot_timeseries(signals, shade=None, colors=None, xlim=None, ylim=None,
                    offset=0, ax=None, **plt_kwargs):
    """Plot time series."""

    ax = check_ax(ax)

    if isinstance(signals, np.ndarray):
        signals = [signals]

    if isinstance(colors, str) or colors is None:
        colors = repeat(colors)

    for ind, (signal, color) in enumerate(zip(signals, colors)):
        ax.plot(signal + ind * offset, color=color, **plt_kwargs)

    if xlim:
        ax.set_xlim(xlim)
    else:
        # Despite seeming like this redundantly resets the limits to what they already are,
        #   for some reason this seems to make sure that shading goes the full length
        ax.set_xlim(*ax.get_xlim())

    if ylim:
        ax.set_ylim(ylim)

    if shade:
        ax.axvspan(*ax.get_xlim(), alpha=0.2, color=shade)

    ax.set(xticks=[], yticks=[], xlabel=None, ylabel=None);


def plot_spectra(freqs, powers, log_freqs=True, log_powers=True, xlim=None, ylim=None,
                 colors=None, shade_ranges=None, shade_colors=None, ax=None, **plt_kwargs):
    """Plot power spectra."""

    ax = check_ax(ax)

    if isinstance(powers, np.ndarray):
        powers = [powers]

    if isinstance(colors, str) or colors is None:
        colors = repeat(colors)

    if log_freqs:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            freqs = np.log10(freqs)

    for power, color in zip(powers, colors):

        if log_powers:
            power = np.log10(power)

        ax.plot(freqs, power, color=color, **plt_kwargs)

    if shade_ranges:
        add_shades(ax, shade_ranges, shade_colors, logged=log_freqs)

    if xlim:
        ax.set_xlim(xlim)
    if ylim:
        ax.set_ylim(ylim)

    ax.set(xticks=[], yticks=[], xlabel=None, ylabel=None);


def plot_bar(d1, d2, ax=None, ylim=None, **plt_kwargs):
    """Plot bar graph with two bars."""

    ax = check_ax(ax)

    ax.bar([0.5, 1.5], [d1, d2], width=0.65, **plt_kwargs)

    ax.set_xlim([0, 2])
    ax.set(xticks=[], yticks=[], xlabel=None, ylabel=None)
    if ylim:
        ax.set_ylim(ylim)


def plot_band_bars(deltas, colors=None, ylim=None, ax=None):
    """Plot power across frequency bands as a bar plot."""

    ax = check_ax(ax)

    labels = [r'$\delta$', r'$\theta$', r'$\alpha$', r'$\beta$', r'$\gamma$']

    ax.bar([0, 1, 2, 3, 4], deltas.values(),
            tick_label=labels, color=colors, alpha=0.6)

    ax.set(yticks=[])
    if ylim:
        ax.set_ylim(ylim);


def add_lines(ax, xpos, color, alpha):
    """Add vertical lines at f1 & f2 positions."""

    ax.axvline(xpos, color=color, alpha=alpha)
    ax.axvline(2 * xpos, color=color, alpha=alpha)
