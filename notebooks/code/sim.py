"""Functions for creating and manipulating simulated data, for oscillation methods visualizers."""

import numpy as  np

###################################################################################################
###################################################################################################

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


def mu_wave(time, shift=0, freq=10, wave_shift=0.5*np.pi):
    """Create a non-sinusoidal signal as a sum of two sine-waves with fixed phase-lag."""

    alpha = 1.0 * np.sin(freq * 2 * np.pi * (time + shift))
    beta = 0.25 * np.sin(freq * 2 * np.pi * 2 * (time + shift) + wave_shift)

    return alpha + beta
