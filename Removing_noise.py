import soundfile as sf
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
#read .wav file
input_signal,fs = sf.read('Sound_Noise.wav')
sampling_frequency = fs  #Sampling frequency of input signal
print(len(input_signal))

gaussian_noise = np.random.normal(0,1,len(input_signal))
input_signal_new = input_signal + gaussian_noise
sf.write('Sound_With_GaussianNoise.wav',input_signal_new,fs)
plt.show()
M = 1000
s = 0
x = 0
y = [0]*len(input_signal_new)
y1 = [0]*len(input_signal)
for n in range(len(input_signal)):
    for k in range(-1000,1001):
        s = s + input_signal_new[n-k-1000]
    y[n] = (1/((2*M) + 1))*s 

for m in range(len(input_signal)):
    for l in range(-1000,1001):
        x = x + input_signal[m-l-1000]
    y1[m] = (1/((2*M) + 1))*x 

print(np.abs(y[n] - y1[m]))
#print(len(y))
#print(y[1])

# sf.write('Sound_With_ReducedNoise_using_MeanFilter.wav',y,fs)
# plt.figure(1)
# plt.subplot(211)
# plt.plot(input_signal)
# plt.subplot(212)
# plt.plot(y)
# plt.show()