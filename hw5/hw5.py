from __future__ import division
import operator
import math

xlist = []
ylist = []
with open('x.txt') as openfile1:
    for line in openfile1:
        xlist.append(line)

with open('y.txt') as openfile2:
    for line in openfile2:
        temp = line.split()
        ylist.append(temp[0])
        
pi = []
for i in range(23):
    pi.append(1 / 23)    # Initialize pi

Ti = []
for i in range(23):
    tempcount = 0
    for t in range(267):
        temp = xlist[t].split()
        tempcount += int(temp[i])
    Ti.append(tempcount)

#for i in range(23):
#    print Ti[i]

for it in range(513):
    piold = []
    for i in range(23):
        piold.append(pi[i]) 
    mistake = 0
    for i in range(23):       # unpdate pi
        tempsum = 0
        for t in range(267):
            temptop = xlist[t].split()
            numerator = int(ylist[t])*int(temptop[i])*piold[i]
            tempbottom = 1
            for j in range(23):
                tempx = xlist[t].split()
                temppower = math.pow(float(1-piold[j]), float(tempx[j]))
                tempbottom = tempbottom * temppower
            denominator = 1 - tempbottom
            tempsum += numerator / denominator
        pi[i] = tempsum / Ti[i]
    
    templog = 0
    for t in range(267):     # calculate log-likelihood
        tempbottom = 1
        for i in range(23):
            tempx = xlist[t].split()
            temppower = math.pow(float(1-piold[i]), float(tempx[i]))
            tempbottom = tempbottom * temppower
        if ylist[t] == '0':
            Py = tempbottom
        elif ylist[t] == '1':
            Py = 1 - tempbottom
        Py1 = 1 - tempbottom    # only use for calculate mistake
        if ylist[t] == '0':
            if Py1 >= 0.5:
                mistake += 1
        elif ylist[t] == '1':
            if Py1 <= 0.5:
                mistake += 1
        templog += math.log(Py)
    log = templog / 267

    if it == 0:
        print 'iteration:', it, mistake, log   # print iteration 0

    for k in range(10):
        tempiter = math.pow(2, k)
        if it == tempiter:
            print 'iteration:', it, mistake, log  # print the following iteration


for i in range(23):             # final estimated values for pi
    print 'pi', i+1, piold[i]
