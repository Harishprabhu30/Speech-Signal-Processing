#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 16:34:42 2025

@author: harishprabhu
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.io import wavfile

# ----------------- Task 1 -----------------
''' Plot the speech signal waveform (time in milliseconds). 
 The audio file should be loaded using the standard file selection dialog. 
 It is recommended to use recordings of individual words. '''
 
# Path to wav files
unvoiced_sha = Path("/Users/harishprabhu/Desktop/SUBJECTS/Sem_2/Speech-and-Signal-Processing/Lab3/unvoiced_sha.wav")
voiced_za = Path("/Users/harishprabhu/Desktop/SUBJECTS/Sem_2/Speech-and-Signal-Processing/Lab3/voiced_za.wav") 
background_noise = Path("/Users/harishprabhu/Desktop/SUBJECTS/Sem_2/Speech-and-Signal-Processing/Lab3/background_noise.wav") 

# voiced fricatives
voiced_car = Path("/Users/harishprabhu/Desktop/SUBJECTS/Sem_2/Speech-and-Signal-Processing/Lab3/voiced_car.wav")
voiced_food = Path("/Users/harishprabhu/Desktop/SUBJECTS/Sem_2/Speech-and-Signal-Processing/Lab3/voiced_food.wav")
voiced_a = Path("/Users/harishprabhu/Desktop/SUBJECTS/Sem_2/Speech-and-Signal-Processing/Lab3/voiced_a.wav")

# Loading audiofile
audiofile = unvoiced_sha
fs, audiofile = wavfile.read(audiofile)
#print(audiofile.shape) # the audio is mono channel and samples: 16000

#audiofile = np.mean(audiofile, axis=1)  # Average left & right channels
#print(audiofile.shape) # the audio is mono channel and samples: 16000

numSamples = audiofile.shape[0]
duration = numSamples / fs # total duration

# defining time vector
t = np.arange(0, numSamples)
t_ms = (t / fs) * 1000 # time in milliseconds
#print("t: ", t.shape)
#print("T_ms: ", t_ms.shape)
#print("NumSamples: ", numSamples)

# plotting
plt.figure(figsize = (15, 8))
plt.plot(t_ms, audiofile)
plt.title("Speech Signal Waveform")
plt.xlabel("time (in milliseconds)")
plt.ylabel("Signal Amplitude")
plt.grid()
plt.show()

# ----------------- Task 2 -----------------
""" Plot the waveform of a selected signal segment. 
The user specifies the start and end times in milliseconds 
(choose a 15-25 ms segment for analysis). """

duration_ms = duration * 1000 # duration in milliseconds
print(f"Duration of the audiofile: {duration_ms} milliseconds")

start_time = input("Enter start time (in seconds): ")
end_time = input("Enter End time (in seconds): ")

# convert to float if input is not empty, else it stores default values
start_time = float(start_time) / 1000 if start_time.strip() else 0
end_time = float(end_time) / 1000 if end_time.strip() else None

# Define default value for end_time
if end_time is None:
    print("End Time not specified. Using the default value.")
    end_time = numSamples / fs
    
# converting to sample index
start_sample = int(round(start_time * fs))
end_sample = int(round(end_time * fs))

# define time vector 
t = np.arange(start_sample, end_sample) / fs # in seconds
t_ms = t * 1000 # t in milli-seconds

plt.figure(figsize = (15, 8))
plt.plot(t_ms, audiofile[start_sample : end_sample])
plt.title("Displaying selected region of speech signal")
plt.xlabel("time (in milliseconds)")
plt.ylabel("Signal Amplitude")
plt.grid()
plt.show()

# ----------------- Task 3 -----------------
""" Compute and plot the frequency spectrum of the selected segment. 
The x-axis should be in kilohertz (kHz)."""

# compute fft for the segmented audio signal
segment = audiofile[start_sample : end_sample]
N = len(segment) # No. of samples in the selected region

# Apply fft
fft_values = np.fft.fft(segment)
freqs = np.fft.fftfreq(N, d = 1 / fs) # freq values in Hz

# As fft is symmetric, take positive half of frequencies
positive_freqs = freqs[: N // 2]
magnitude_spectrum = np.abs(fft_values[: N // 2]) # Take magnitude for the positive half of freqs

positive_freqs_KHz = positive_freqs / 1000 # Hz -> KHz

# plotting frequency spectrum
plt.figure(figsize = (15, 8))
plt.plot(positive_freqs_KHz, magnitude_spectrum)
plt.title("Frequency Spectrum for selected region of Speech Signal")
plt.xlabel("Frequency (in KHz)")
plt.ylabel("Magnitude")
plt.grid()
plt.show()

# ----------------- Task 4 -----------------
""" Compute and plot the cepstrum of the selected segment. 
The x-axis should be in milliseconds. """

# as fft is already calculated. Let's compute log of fft_values
log_magnitude_spectrum = np.log(np.abs(fft_values) + 1e-10) # avoiding log(0) by adding a small number

# applying Inverse FFT on log magnitude spectrum
log_magnitude_spectrum_ifft = np.fft.ifft(log_magnitude_spectrum).real

# quefrency values
quefrency = np.arange(len(log_magnitude_spectrum)) / fs # in seconds
quefrency_ms = quefrency * 1000 # in milli-seconds

# plotting cepstrum for the selected region of signal
plt.figure(figsize = (15, 8))
plt.plot(quefrency_ms, log_magnitude_spectrum_ifft)
plt.title("Cepstrum for selected region of Speech Signal")
plt.xlabel("quefrency (in milliseconds)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()




