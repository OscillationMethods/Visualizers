"""Functions for computing measures of interest for oscillation methods visualizers."""

import numpy as np

from fooof.utils import trim_spectrum

from neurodsp.timefrequency import robust_hilbert

###################################################################################################
###################################################################################################

def compute_abs_power(freqs, powers, band):
    """Compute absolute power for a given frequency band."""

    _, band_powers = trim_spectrum(freqs, powers, band)
    avg_power = np.sum(band_powers)

    return avg_power


def compute_rel_power(freqs, powers, band, method='sum', norm_range=None):
    """Compute relative power for a given frequency band."""

    band_power = compute_abs_power(freqs, powers, band)

    total_band = [freqs.min(), freqs.max()] if not norm_range else norm_range
    total_power = compute_abs_power(freqs, powers, total_band)

    rel_power = band_power / total_power * 100

    return rel_power


def compute_pac(signal_alpha_filt, signal_beta_filt, n_bins=21):
    """Compute phase-amplitude coupling for a mu signal."""

    beta_env = np.abs(robust_hilbert(signal_beta_filt))
    phase_alpha = np.angle(robust_hilbert(signal_alpha_filt))

    bins = np.linspace(-np.pi, np.pi, n_bins)
    phase_bins = np.digitize(phase_alpha, bins)

    pac = np.zeros(n_bins)
    for i_bin, c_bin in enumerate(np.unique(phase_bins)):
        pac[i_bin] = np.mean(beta_env[(phase_bins == c_bin)])

    return bins, pac
