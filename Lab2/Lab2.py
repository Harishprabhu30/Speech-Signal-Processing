# importing the essential libraries 
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.io import wavfile

# ----------------- Task 1 -----------------
# Loading audiofile
audiofile = Path("/Users/harishprabhu/Desktop/SUBJECTS/Sem_2/Speech and Signal Processing/Lab2/oh no.wav")
fs, audiofile = wavfile.read(audiofile)
# print(audiofile.shape) # audio is 2 channel, samples = 73729

# duration of the audio
numSamples = audiofile.shape[0] # total num of samples in the signal
numChannels = audiofile.shape[1]
leftChannel = audiofile[:, 0]
rightChannel = audiofile[:, 1]
duration = numSamples / fs # total duration of the signal
# defining time vector 
t = np.arange(0, numSamples) / fs # can also use np.linspace(0, (numSamples - 1) / fs, numSamples)
t_ms = t * 1000 # in milliseconds

# plotting both the channels of signal
plt.figure(figsize = (15, 8))
ax1 = plt.subplot(211)
plt.plot(t_ms, leftChannel, color = "b")
plt.title("Left Channel")
# plt.xlabel("Time (millisecond)")
plt.ylabel("Signal Amplitude")
ax1.tick_params("x", labelbottom = False) # disables xlabel

ax2 = plt.subplot(212, sharex = ax1)
plt.plot(t_ms, rightChannel, color = "r")
plt.title("Right Channel")
plt.xlabel("Time (millisecond)")
plt.ylabel("Signal Amplitude")
plt.show()

# ----------------- Task 2 -----------------
# choose a frame length 
frameLength = 20 # anywhere in the range 15-25ms
frameSize = int(round(frameLength * fs / 1000)) # converting frame_length millisecond to samples
overlap = int(0.5 * frameSize) # about half of frame length
frameShift = frameSize - overlap 

energy_values = []
time_values = []
for i in range(0, len(audiofile) - frameSize, frameShift):
    frame = audiofile[i : i + frameSize] # Exact frame size
    energy = sum(x**2 for x in frame) # compute energy
    energy_values.append(energy)
    time_values.append(i / fs * 1000) # converts start sample to time in milliseconds

# plot energy vs time (ms)
plt.figure(figsize = (15, 8))
plt.subplot(211)
plt.plot(time_values, energy_values, marker = 'o', linestyle = "-")
plt.xlabel("Time (milliseconds)")
plt.ylabel("Energy")
plt.title("Energy Diagram (Time-Based)")

# plot energy vs frame Number
frameNumbers = np.arange(len(energy_values))
plt.subplot(212)
plt.plot(frameNumbers, energy_values, marker = "o", linestyle = '-', color = 'r')
plt.xlabel("Frame Numbers")
plt.ylabel("Energy")
plt.title("Energy Diagram (Frame-Based)")
plt.show()

# ----------------- Task 3 -----------------