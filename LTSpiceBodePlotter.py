import matplotlib.pyplot as plt
import numpy as np

f = open("Trinn1.txt", "r")
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

#Finding the -3 dB value and finding the value nearest this value in the list.
absolute_difference_function = lambda list_value : abs(list_value - (max(gain)-3))
closest_value = min(gain, key=absolute_difference_function)
peak_dB_LTSpice = max(gain)
freq_comment = str(freq[gain.index(closest_value)]) 
x_coord_LTSpice = freq[gain.index(closest_value)]
y_coord_LTSpice = gain[gain.index(closest_value)]

#dB plot
plt.figure()
plt.subplot(211)
plt.semilogx(freq, gain)

#Comment out these to remove the point, annotation and legend.
plt.scatter(x_coord_LTSpice, y_coord_LTSpice, color = 'red')
plt.annotate('-3dB at {}Hz'.format(freq_comment), (x_coord_LTSpice, y_coord_LTSpice))
plt.legend(['Peak value {}dB'.format(peak_dB_LTSpice)], loc ="lower left") #Use this to change the location

plt.ylabel('dB Mag.')
plt.grid()

#Phaseplot
plt.subplot(212)
plt.semilogx(freq, phase)
plt.xlabel('Freq. (Hz)')
plt.ylabel('Phase (deg.)')
plt.grid()
plt.show()
