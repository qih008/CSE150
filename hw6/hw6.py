import operator
import math

initial = []
with open('initialStateDistribution.txt') as openfile1:
    for line in openfile1:
        temp = line.split()
        initial.append(temp[0])
    
Amatrix = [[0 for i in xrange(26)] for i in xrange(26)]
Bmatrix = [[0 for i in xrange(2)] for i in xrange(26)]

row = 0
with open('transitionMatrix.txt') as openfile2:
    for line in openfile2:
        temp = line.split()
        column = 0
        for i in temp:
            Amatrix[row][column] = temp[column]
            column += 1
        row += 1

row = 0
with open('emissionMatrix.txt') as openfile3:
    for line in openfile3:
        temp = line.split()
        column = 0
        for i in temp:
            Bmatrix[row][column] = temp[column]
            column += 1
        row += 1

observation = []
with open('observations.txt') as openfile4:
    for line in openfile4:
        temp = line.split()
        for i in range(48000):
            observation.append(temp[i])

valuematrix = [[0 for i in xrange(48000)] for i in xrange(26)]

count = 0
for t in range(48000):   # forward
    if t == 0:           # initial column
        for i in range(26):      # first column 
            bigvalue = math.log(float(initial[i]))  # log initial
            tempB = Bmatrix[i][int(observation[t])] # bi(Ot)
            tempB = math.log(float(tempB))          # log bi(Ot+1)
            bigvalue = bigvalue + tempB             # lj,t+1
            valuematrix[i][t] = bigvalue            # fill in value table
    else:
        count += 1
        for j in range(26):
            bigvalue = -9999999
            for i in range(26):
                tempvalue = math.log(float(Amatrix[i][j]))
                tempvalue = tempvalue + float(valuematrix[i][t-1])
                if bigvalue < tempvalue:
                    bigvalue = tempvalue
                    
            tempB = Bmatrix[j][int(observation[t])]
            tempB = math.log(float(tempB))
            bigvalue = bigvalue + tempB
            valuematrix[j][t] = bigvalue

maxvalue = -9999999       # back-tracking
for i in range(26):
    if maxvalue < valuematrix[i][47999]:   # T column
        maxvalue = valuematrix[i][47999]
        maxindex = i     
#print maxindex 

hiddenstates = []
hiddenstates.append(maxindex)    # ST
tempindex = maxindex

for t in range(47999):
    bigvalue = -9999999
    bigindex = 0
    for i in range(26): 
        tempvalue = math.log(float(Amatrix[i][tempindex]))
        tempvalue = tempvalue + float(valuematrix[i][47999-t])
        if bigvalue < tempvalue:
            bigvalue = tempvalue
            bigindex = i
            
    if bigindex != tempindex:
        hiddenstates.append(bigindex)
        tempindex = bigindex

hiddenstates.reverse()
for index in hiddenstates:
    print index

