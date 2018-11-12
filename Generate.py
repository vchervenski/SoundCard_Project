import math
import wave
import array
import random


class Generate:
    # ToDo make stereo
    def sine_wave(self):
        for i in range(self.numSamples):
            data = self.sample * math.sin(math.pi * 2 * (i % self.numSamplesPerCyc) / self.numSamplesPerCyc)
            self.data.append(int(data))

    def square_wave(self):
        for i in range(self.numSamples):
            data = self.sample * self.sign(math.sin(math.pi * 2 * (i % self.numSamplesPerCyc) / self.numSamplesPerCyc))
            self.data.append(int(data))

    def sawtooth_wave(self):
        samplePerWaveLength = self.sampleRate / (self.freq / self.numChan)
        ampStep = (self.sample * 2) / samplePerWaveLength
        totalSamplesWriten = 0
        while totalSamplesWriten < self.numSamples:
            tempSample = -self.sample
            i = 0
            while i < samplePerWaveLength and totalSamplesWriten < self.numSamples:
                # print("In")
                tempSample = tempSample + ampStep
                self.data.append(int(tempSample))
                i = i + 1
                totalSamplesWriten = totalSamplesWriten + 1

    def triangle_wave(self):
        samplePerWaveLength = self.sampleRate / (self.freq / self.numChan)
        ampStep = (self.sample * 2) / samplePerWaveLength
        tempSample = -self.sample
        for i in range(self.numSamples):
            if abs(tempSample) > self.sample:
                ampStep = -ampStep
            tempSample = tempSample + ampStep
            self.data.append(int(tempSample))

    def white_noise(self):
        for i in range(200):
            rand = random.randint(-self.sample, self.sample)
            self.data.append(int(rand))

    def sign(self, x):
        return 1 if x >= 0 else -1

    def start_gen(self, type_wave):
        if type_wave == 1:
            wavename = "SineWave_"
            self.sine_wave()
        elif type_wave == 2:
            wavename = "SquareWave_"
            self.square_wave()
        elif type_wave == 3:
            wavename = "SawtoothWave_"
            self.sawtooth_wave()
        elif type_wave == 4:
            wavename = "TriangleWave_"
            self.triangle_wave()
        elif type_wave == 5:
            wavename = "WhiteNoise_"
            self.white_noise()
        else:
            return None

        f = wave.open(wavename + str(self.freq) + 'Hz.wav', 'w')
        f.setparams((self.numChan, self.dataSize, self.sampleRate, self.numSamples, "NONE", "Uncompressed"))
        f.writeframes(self.data.tostring())
        f.close()
        return wavename + str(self.freq) + 'Hz.wav'

    def __init__(self, duration, freq, volume):
        # seconds
        self.duration = duration

        # of cycles per second (Hz) (frequency of the sine waves)
        self.freq = freq

        # percent
        self.volume = volume

        # signed short integer (-32768 to 32767) data
        # ToDo increase array size for different waves
        self.data = array.array("h")

        # of samples per second (standard)
        self.sampleRate = 44100

        # of channels (1: mono, 2: stereo)
        self.numChan = 1

        # 2 bytes because of using signed short integers => bit depth = 16
        self.dataSize = 2

        self.numSamplesPerCyc = int(self.sampleRate / self.freq)

        self.numSamples = self.sampleRate * self.duration

        self.sample = 32767 * float(self.volume) / 100
