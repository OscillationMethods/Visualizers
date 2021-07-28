"""Ulility functions for oscillation methods visualizers."""

import numpy as np

from fooof.utils import trim_spectrum

from neurodsp.timefrequency import robust_hilbert

###################################################################################################
###################################################################################################

def yield_sig(sig, start=0, size=100, step=1):
    """Helper function to yield segments of a signal."""

    for st in range(start, len(sig)-size, step):
        yield sig[st:st+size]


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


def rotate_sig(sig, fs, delta_exp, f_rotation):
    """Spectrally rotate a time series."""

    fft_vals = np.fft.fft(sig)
    f_axis = np.fft.fftfreq(len(sig), 1./fs)

    if f_axis[0] == 0:
        skipped_zero = True
        p_0 = fft_vals[0]
        f_axis, fft_vals = f_axis[1:], fft_vals[1:]

    else:
        skipped_zero = False

    f_mask = 10**(np.log10(np.abs(f_axis)) * delta_exp)
    f_mask = f_mask / f_mask[np.where(f_axis == f_rotation)]

    fft_rot = fft_vals * f_mask

    if skipped_zero:
        fft_rot = np.insert(fft_rot, 0, p_0)

    sig_out = np.real(np.fft.ifft(fft_rot))

    return sig_out


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
