from numpy.random import sample
import matplotlib.pyplot as plt
from numpy.fft import rfft, rfftfreq, irfft
from numpy import cos, pi, arange, abs as nabs, where, mean, array

FD = 100
N = 50
filter_line = 3

t = arange(N)/FD
signal = 4*cos(2*pi*37*t) + 6*cos(2*pi*179*t) + 13*cos(2*pi*74*t)
noise = (-6)*sample(signal.shape[0]) + 3 #слишком большая амплитуда шума: (-np.pi, np.pi), хороший шум: (-0.1, 0.1)

noised_signal = signal + noise

freq = rfftfreq(N, 1./FD)
clear_ampl = 2*nabs(rfft(signal))/N
ampl = 2*nabs(rfft(noised_signal))/N
spectrum = rfft(noised_signal)

fig = plt.figure(figsize = (6, 6))
sub = fig.add_subplot(111) #цифры внутри - соотножения сторон от фигсайз

plt.plot(freq, ampl, label = 'Frequences', c = 'green')
plt.plot(freq, [mean(ampl) for i in range(freq.shape[0])], c = 'orange')
plt.plot(freq, [filter_line*mean(ampl) for i in range(freq.shape[0])], c = 'red')
plt.plot(freq, clear_ampl, c = 'blue')

sub.set_xlabel('Частоты (Гц)', fontsize = 12)

plt.legend(fontsize = 12)
plt.grid(True)

filtrated_frequances = [freq[i] if ampl[i] > filter_line*mean(ampl) else 0 for i in range(freq.shape[0])]
filtrated_signal = [spectrum[i] if ampl[i] > filter_line*mean(ampl) else 0 for i in range(freq.shape[0])]

fig = plt.figure(figsize = (6, 6))
sub = fig.add_subplot(111)

plt.plot(t, noised_signal, label = 'Зашумленный сигнал', c = 'orange')
plt.plot(t, irfft(filtrated_signal, N), label = 'Фильтрованный сигнал', c = 'green')
plt.plot(t, signal, label = 'Чистый сигнал', c = 'blue')

sub.set_xlabel('Время (с)', fontsize = 12)
sub.set_title('График исходного, зашумлённого и фильтрованного сигналов')

plt.legend(loc = 'upper center', fontsize = 12)
plt.grid(True)
plt.show()
