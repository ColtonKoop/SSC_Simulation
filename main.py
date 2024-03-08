import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.fft import fft, fftfreq

if __name__ == '__main__':
    # Define time parameters for signal generation
    start_time = 0        # Start of the time range
    stop_time = 1e-6      # End of the time range, set to 1 microsecond
    sampling_rate = 500e6 # Sampling rate, set to 500 MHz for high-frequency signals

    # Create a time array based on the defined time parameters
    t = np.arange(start_time, stop_time, 1/sampling_rate)

    # Frequency parameters for modulation
    f0 = 100e6      # Central frequency of the square wave (100 MHz)
    fm = 33.3e6     # Modulation frequency of the triangular wave (33.3 MHz)
    delta_f = 2e6   # Frequency deviation for modulation (2 MHz)

    # Create a modulated frequency signal using a triangular waveform
    modulated_f = f0 + delta_f * signal.sawtooth(2 * np.pi * fm * t, width=0.5)

    # Amplitude of the square wave
    A_sq = 1    # Clock amplitude, set to 1 for simplicity

    # Generate an unmodulated square wave
    sq = A_sq * signal.square(2 * np.pi * f0 * t)

    # Generate a frequency-modulated square wave
    sq_modulated = A_sq * signal.square(2 * np.pi * modulated_f * t)

    # Perform FFT on both the unmodulated and modulated square waves
    fft_sq = fft(sq)
    fft_sq_modulated = fft(sq_modulated)
    fft_freq = fftfreq(len(t), 1 / sampling_rate)  # Frequency array for FFT

    # Plotting the FFT results
    plt.plot(fft_freq, abs(fft_sq), label="Unmodulated Clock")
    plt.plot(fft_freq, abs(fft_sq_modulated), label="Modulated Clock")
    plt.title("Spread Spectrum Clocking (SSC) Simulation")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.xlim(0.75*f0, 1.25*f0)  # Focus on the frequency range around 100 MHz
    plt.grid(True)
    plt.legend()

    plt.show()

