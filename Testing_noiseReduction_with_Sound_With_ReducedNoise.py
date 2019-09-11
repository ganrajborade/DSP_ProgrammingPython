import soundfile as sf
from scipy import signal
import matplotlib.pyplot as plt
#read .wav file
input_signal,fs = sf.read('Sound_With_ReducedNoise.wav')
sampling_frequency = fs  #Sampling frequency of input signal
print(len(input_signal))

plt.show()
M = 100
s = 0
y = [0]*len(input_signal)
for n in range(len(input_signal)):
    for k in range(-100,101):
        s = s + input_signal[n-k-100]
    y[n] = (1/((2*M) + 1))*s 
print(len(y))
print(y[1])

sf.write('Sound_With_ReducedNoise_using_MeanFilter.wav',y,fs)
plt.figure(1)
plt.subplot(211)
plt.plot(input_signal)
plt.subplot(212)
plt.plot(y)
plt.show()