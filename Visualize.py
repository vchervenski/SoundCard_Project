import matplotlib.pyplot as plt
import numpy as np
import wave
import sys


class Visualise:
    def start_visualizing(self, filename):
        spf = wave.open(filename, 'r')
        # Extract Raw Audio from Wav File
        signal = spf.readframes(-1)
        signal = np.fromstring(signal, 'Int16')

        # Split the data into channels
        channels = [[] for channel in range(spf.getnchannels())]
        for index, datum in enumerate(signal):
            channels[index % len(channels)].append(datum)

        # Get time from indices
        fs = spf.getframerate()
        Time = np.linspace(0, len(signal) / len(channels) / fs, num=int(len(signal) / len(channels)))
        spf.close()

        # Plot
        plt.figure(1)
        plt.title('Signal Wave...')
        for channel in channels:
            plt.plot(Time, channel)
        plt.show()
