#!/usr/bin/env python3


import numpy as np
import matplotlib.pyplot as plt

#Read the file and make list of both time and absorbance
def ReadData(Name_of_file):
    time = []      
    absorbance = []      
    i=0
    with open(Name_of_file) as f:
        for line in f:
            i = i+1
            if i>3:
                words = line.split()
                try:
                    time.append(words[0])
                    absorbance.append(words[1])
                except:
                    pass
                #sys.exit()
    return time,absorbance



time,absorbance = ReadData("superose6_50.asc")
time,absorbance = np.array(time).astype(float),np.array(absorbance).astype(float)



plt.plot(time,absorbance)
plt.xlabel('Time')
plt.ylabel('Absorbance')


#Find the peaks

threshold = 80
IsPeak = False
Peak_start = []
Peak_end   = []
Peak_max   = []
for i in range(len(time)):
    absorbance_val = absorbance[i]
    if ((absorbance[i] >= threshold) and (absorbance[i-1]<threshold)) :
        Peak_start.append(time[i])
        IsPeak = True
    if IsPeak:
        if ((absorbance[i]>absorbance[i-1]) and (absorbance[i]>absorbance[i+1])):
            Peak_max.append((time[i],absorbance[i]))
    if ((absorbance[i] >= threshold) and (absorbance[i+1]<threshold)):
        Peak_end.append(time[i])
        IsPeak = False
        



Peak_start,Peak_end,Peak_max = np.array(Peak_start),np.array(Peak_end),np.array(Peak_max)

print ("The peaks are at the following x,y values (time, absorbance):")
print (Peak_max)

#Find the start and end point of all the peaks
plt.figure(figsize=(10,5))
plt.plot(time,absorbance)
plt.scatter(Peak_max[:,0],Peak_max[:,1],color ='orange')
for i in range(len(Peak_start)):
    x_start = Peak_start[i]
    x_end   = Peak_end[i]
    if i==0:
        plt.axvline(x=x_start, color='y', linestyle='--',label="Peak_start")
        plt.axvline(x=x_end, color='g', linestyle='--',label="Peak_end")
    else:
        plt.axvline(x=x_start, color='y', linestyle='--')
        plt.axvline(x=x_end, color='g', linestyle='--')
plt.axhline(y=threshold,color = 'r',linestyle='--')
plt.xlabel('Time(min)')
plt.ylabel('Absorbance(mAu)')
plt.legend()
plt.show()

#Print the boundaries where peaks start and end in the chromatogram

print ("The peaks I, II, III and IV begin at ", Peak_start, " minutes, respectively")

print ("The peak I, II, III and IV end at ", Peak_end, " minutes, respectively")
