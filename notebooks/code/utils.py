"""Utility functions for oscillation methods visualizers."""

import numpy as np

###################################################################################################
###################################################################################################

def yield_sig(sig, start=0, size=100, step=1):
    """Helper function to yield segments of a signal."""

    for st in range(start, len(sig)-size, step):
        yield sig[st:st+size]


def sweep_values(mid, low, high, step, round_vals=None):
    """Create a an upward/downward sweep across a range of values."""

    values = np.concatenate([np.arange(mid, high, step),
                             np.arange(high, low, -step),
                             np.arange(low, mid, step)])

    if round_vals:
        values = np.round(values, round_vals)

    return values
