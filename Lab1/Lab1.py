# loading the Audio File
from scipy.io import wavfile
import torch
import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns
import torchaudio


def analyse_audio(audio_file, save_path):
    """
    This fucntion reads the audio file, extracts its information, \
    plots visualization if the user wants, in his desired range of time.\
    After visualization, it saves the plot as png in the desired directory,\
    you mentioned during function call.

    """
    # Reading the audio file:
    fs, audiofile = wavfile.read(audio_file)

    # printing the signal information
    print("\nSample Rate of the audiofile: ", fs)
    duration = audiofile.shape[0] / fs
    duration_ms = duration * 1000 # duration in milliseconds
    print(f"Duration of the audiofile: {duration_ms} milliseconds")
    numSamples = duration * fs
    print("Number of Samples of the audiofile: ", numSamples)
    audio_metadata = torchaudio.info("oh no.wav")
    numChannel = audiofile.shape[1]
    print("Channel of the audio: ", numChannel)
    print("Quantization Bit: ", audio_metadata.bits_per_sample)
    
    # play the audio

    y_n = input("\nEnter [Y/y] to visualize the signal: ")
    ans = ["Y", "y"]
    if y_n in ans:

        start_time = input("\nEnter the start time in seconds [default is set to 0]: ")
        end_time = input("Enter the end time in seconds: ")

        # Convert to float if input is not empty, else use default values
        start_time = float(start_time) / 1000 if start_time.strip() else 0
        end_time = float(end_time) / 1000 if end_time.strip() else None

        # Defining default value for End time
        if end_time is None:
            print("End time is not provided. Using default value: End of audio")
            end_time = numSamples / fs # already in seconds

        # Converting to sample index
        start_sample = int(round(start_time * fs))
        end_sample = int(round(end_time * fs))

        # lets define time vector 
        t = np.arange(start_sample, end_sample) / fs # t is in seconds
        t_ms = t * 1000 # t is in milliseconds

        if numChannel == 2:
            print("\nThe Audio is Stereo")

            # Plotting Left and Right Channel Viz
            # Splitting left and right channel
            left_channel = audiofile[start_sample : end_sample, 0]
            right_channel = audiofile[start_sample : end_sample, 1]

            plt.figure(figsize = (10,10))
            # sns.set_style("darkgrid")
            
            # Left Channel
            plt.subplot(2, 1, 1)
            plt.plot(t_ms, left_channel, color = 'blue')
            # sns.lineplot(x = t_ms, y = left_channel, color="blue")
            plt.xlabel("Time (milliseconds)")
            plt.ylabel("Amplitude")
            plt.title("Waveform of the Audio (Left Channel)")

            # Right Channel
            plt.subplot(2, 1, 2)
            plt.plot(t_ms, right_channel, color = 'red')
            # sns.lineplot(x = t_ms, y = right_channel, color = "red")
            plt.xlabel("Time (milliseconds)")
            plt.ylabel("Amplitude")
            plt.title("Waveform of the Audio (Right Channel)")

            # Saving the figure
            plt.savefig(save_path, dpi = 300, bbox_inches = "tight")
            print(f"Plot saved as: {save_path}\n")

            plt.tight_layout()
            plt.show()
            
        else:
            print("\nThe audio is Mono\n")

            plt.plot(t_ms, audiofile, color = 'blue')
            plt.xlabel("Time (milliseconds)")
            plt.ylabel("Amplitude")
            plt.title("Waveform of the Audio (Mono)")
            
            # SAving the Figure
            plt.savefig(save_path, dpi = 300, bbox_inches = "tight")
            print(f"Figure saved as: {save_path}")
            plt.show()
    else : 
        print("You chose No. Therefore No Visualization available.\n")


def main():
    audiofile = "oh no.wav"
    save_path = "/Users/harishprabhu/Desktop/SUBJECTS/Sem_2/Speech and Signal Processing/Lab1/audio_analyse.png"
    
    # Calling the function
    analyse_audio("oh no.wav", save_path)

if __name__ == "__main__":
    main()