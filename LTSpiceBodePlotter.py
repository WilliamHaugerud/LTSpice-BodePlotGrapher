import matplotlib.pyplot as plt
import numpy as np

f = open("Trinn2(C1&R5).txt", "r")
line1 = f.readline()

freq = []
gain = [] 
phase = []

line = f.readline().strip('\n')

while line !="":
    data1, data2 =  line.split()
    freq.append(round(float(data1), 4))
    gainRaw, phaseRaw = data2.split(",")
    gain.append(round(float(gainRaw.strip("(dB")), 4))
    phase.append(round(float(phaseRaw.strip(")°")), 4))
    line = f.readline()

#x_ticks = np.arange(min(freq), max(freq), len(freq))
absolute_difference_function = lambda list_value : abs(list_value - (max(gain)-3))
closest_value = min(gain, key=absolute_difference_function)
gain.index(closest_value)
freq_comment = str(freq[gain.index(closest_value)])


plt.figure()
plt.subplot(211)
plt.semilogx(freq, gain)
plt.scatter(freq[gain.index(closest_value)], gain[gain.index(closest_value)], color = 'red')
plt.annotate('-3dB at {}Hz'.format(freq_comment), (freq[gain.index(closest_value)], gain[gain.index(closest_value)]))
plt.grid()
plt.ylabel('dB Mag.')
#plt.ylim([-120,5])
plt.subplot(212)
plt.semilogx(freq, phase)
plt.grid()
plt.xlabel('Freq. (Hz)')
plt.ylabel('Phase (deg.)')
#plt.ylim([-185,10])
#out = plt.yticks(np.arange(-180,5,45))
plt.show()
