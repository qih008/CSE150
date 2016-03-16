from __future__ import division
import operator
import math

ulist = []
vlist = []
# Q1 find the unigram probability
with open('unigram.txt') as openfile1:
    for line in openfile1:
        temp = line.split()
        ulist.append(temp[0])

with open('vocab.txt') as openfile2:
    for line in openfile2:
        temp = line.split()
        vlist.append(temp[0])

unigramcount = 0
for number in ulist:
    unigramcount += int(number)

for char in vlist:
    if char[0] == 'A':
        uniprob = int(ulist[vlist.index(char)]) / unigramcount
        #print char, uniprob    # print Q1 answer


# Q2 find top 10 w' follow by "THE" , and theri bigram probability
index = []
bicount = []
with open('bigram.txt') as openfile3:
    for line in openfile3:
        temp = line.split()
        index.append((temp[0],temp[1]))
        bicount.append(temp[2])

indexthe = vlist.index('THE')   # get 'The' index
thecount = int(ulist[indexthe]) # get 'The' count   
biproblist = []
for line in index:
    if indexthe == int(line[0])-1:
        biprob = int(bicount[index.index(line)]) / thecount
        biproblist.append((vlist[int(line[1])-1], biprob))  # store in pair

biproblist.sort(key=lambda x:x[1], reverse=True)    # reverse the order
#for i in range(10):
    #print biproblist[i]     # print Q2 answer


# Q3 compute and compare the log-likelihoods
clist = ['STOCK','MARKET','FELL','BY','ONE','HUNDRED','POINTS','LAST','WEEK']

# under the unigram models
loguniprob = 0
tempindex = 0
loguniprob = thecount / unigramcount
for i in clist: 
    tempindex = int(vlist.index(i))
    loguniprob = loguniprob * (int(ulist[tempindex]) / unigramcount)
    #print loguniprob
#print loguniprob
print 'Lu is:',math.log(loguniprob)   # print Q3 Lu !!!!!!!!!!!!!!!!!!!!

# under the bigram models
thefollows = 0
logbiprob = 0
indexs = vlist.index('<s>')  # get '<s>' index
for line in index:                  # find Pb(the|<s>)
    if indexs == int(line[0])-1:
        if indexthe == int(line[1])-1:
            thefollows = int(bicount[index.index(line)]) / int(ulist[indexs])

indexstock = vlist.index('STOCK')      # get 'stock' index

for line in index:              # find Pb(stock|the)
    if indexthe == int(line[0])-1:
        if indexstock == int(line[1])-1:
            logbiprob = int(bicount[index.index(line)]) / thecount
logbiprob = logbiprob * thefollows  # contain first two terms for now

for i in range(len(clist)-1):
    haveflag = 0
    tempindex1 = int(vlist.index(clist[i]))   # index for 1st word
    tempindex2 = int(vlist.index(clist[i+1])) # index for 2nd word
    for j in index:
            if tempindex1 == int(j[0])-1:
                if tempindex2 == int(j[1])-1:
                    haveflag = 1
    if haveflag == 1:
        for line in index:
            if tempindex1 == int(line[0])-1:
                if tempindex2 == int(line[1])-1:
                        tempprob=int(bicount[index.index(line)])/int(ulist[tempindex1])
                        #print tempprob
                        logbiprob = logbiprob * tempprob
                        #print logbiprob
    else:
        print vlist[tempindex1],vlist[tempindex2]
        logbiprob =0
#print logbiprob
if logbiprob != 0:
    print 'Lb is:',math.log(logbiprob)   # print Q3 Lb!!!!!!!!!!!!!!!!!!!!!!!!!!!


# Q4 compute and compare the log-likelihoods
dlist = ['SIXTEEN','OFFICIALS','SOLD','FIRE','INSURANCE']

# under the unigram models
loguniprob = 0
tempindex = 0
loguniprob = thecount / unigramcount
for i in dlist:
    tempindex = int(vlist.index(i))
    loguniprob = loguniprob * (int(ulist[tempindex]) / unigramcount)
    #print loguniprob
#print loguniprob
print 'Lu is:', math.log(loguniprob)   # print Q4 Lu!!!!!!!!!!!!!!!!!!!!!!!!!

# under the bigram models
logbiprob = 0
temprob = 0
indexsixteen = vlist.index('SIXTEEN')  # get 'sixteen' index

for line in index:              # find Pb(sixteen|the)
    if indexthe == int(line[0])-1:
        if indexsixteen == int(line[1])-1:
            sixteenfollowthe = int(bicount[index.index(line)]) / thecount
logbiprob =  sixteenfollowthe * thefollows  # contain first two terms for now

for i in range(len(dlist)-1):
    haveflag = 0
    tempindex1 = int(vlist.index(dlist[i]))   # index for 1st word
    tempindex2 = int(vlist.index(dlist[i+1])) # index for 2nd word
    for j in index:
            if tempindex1 == int(j[0])-1:
                if tempindex2 == int(j[1])-1:
                    haveflag = 1
    if haveflag == 1:
        for line in index:
            if tempindex1 == int(line[0])-1:
                if tempindex2 == int(line[1])-1:
                    if haveflag == 1:
                        tempprob=int(bicount[index.index(line)])/int(ulist[tempindex1])
                        logbiprob = logbiprob * tempprob
                        #print logbiprob
    else:
        print vlist[tempindex1],vlist[tempindex2]
        logbiprob =0
#print logbiprob
if logbiprob != 0:
    print 'Lb is:',math.log(logbiprob)   # print Q4 Lb!!!!!!!!!!!!!!!!!!!!!!!!!!!
else:
    print 'Those previous adjacent words are not observed in the training corpus'

# Q5 mixture model
v = 0
tempbi = 0
probthe = thecount / unigramcount
probsixteen = int(ulist[indexsixteen]) / unigramcount
for r in range(101):
    logmiprob = (1-v)*probthe + v*thefollows   # Pm(the|<s>)
    tempprob = (1-v)*probsixteen + v*sixteenfollowthe # Pm(sixteen|the)
    logmiprob = logmiprob * tempprob    # contain first two terms for now
    for i in range(len(dlist)-1):
        haveflag = 0
        tempindex1 = int(vlist.index(dlist[i]))   # index for 1st word
        tempindex2 = int(vlist.index(dlist[i+1])) # index for 2nd word
        tempuni = int(ulist[tempindex2]) / unigramcount
        for j in index:
            if tempindex1 == int(j[0])-1:
                if tempindex2 == int(j[1])-1:
                    haveflag = 1
        if haveflag == 1:
            for line in index:
                if tempindex1 == int(line[0])-1:
                    if tempindex2 == int(line[1])-1:
                        tempbi=int(bicount[index.index(line)])/int(ulist[tempindex1])
        else:
            tempbi = 0
        tempprob = (1-v)*tempuni + v*tempbi
        logmiprob = logmiprob * tempprob
    print v, 'Lm is:',math.log(logmiprob)
    v += 0.01

