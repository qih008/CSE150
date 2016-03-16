from __future__ import division

ziplist = []
poplist = []
prob = []
totalpop = 0
popcount = 0
h1=h2=h3=h4=h5 = 0
count = 0

with open('zipcode.txt') as openfile:
  for line in openfile:
    temp = line.split()
    ziplist.append(temp[0])
    poplist.append(temp[1])

ziplist.remove('%')
poplist.remove('Zip_Code')
#print ziplist[0], poplist[0]

for number in poplist:
  totalpop +=int(number)
 # count = count + 1
#print count

for number in poplist:
  temp = int(number) / totalpop
 # temp = format(temp, '.8f')
  prob.append(temp)

for number in prob:
  temp = float(number)
  if temp > h1:
    h5 = h4
    h4 = h3
    h3 = h2
    h2 = h1
    h1 = temp
  elif temp > h2:
    h5 = h4
    h4 = h3
    h3 = h2
    h2 = temp
  elif temp > h3:
    h5 = h4
    h4 = h3
    h3 = temp
  elif temp > h4:
    h5 = h4
    h4 = temp
  elif temp > h5:
    h5 = temp

#print ziplist[prob.index(h1)]
#print ziplist[prob.index(h2)]
#print ziplist[prob.index(h3)]
#print ziplist[prob.index(h4)]
#print ziplist[prob.index(h5)]

right = raw_input('Current zipcode: ').split()
wrong = raw_input('Digits not in zipcode: ').split()

#templist = ziplist

#for i in wrong:
#  print i
#  for j in templist:
#    if i in j:
#      count = count + 1
#      templist.remove(j)

#for number in templist:
#  count = count + 1
#print count

n = ['0','1','2','3','4','5','6','7','8','9']
s = [0,1,2,3,4]
totalproblist = []

for j in n:
  totalprob = 0
  subtotalpop = 0
  correctpop = 0
  if wrong.count(j) == 0:        # set prob of wrong guess to 0
    if right.count(j) == 0:      # set prob of correct guess to 1
      for i in ziplist:          # loop a new zip code
        wrongflag = 0
        rightflag = 0
        for k in wrong:          # check all wrong guess
          if k in i:             # only contain prob without wrong guess     
            wrongflag = 1
        for k in s:              # loop through all right guess
          if right[k] != '-1':
           # print right[k]
            if right[k] is not i[k]:
              #print right[k]
              rightflag = 1
          else:
            for m in s:          # loop through all right guess again
              if right[m] != '-1':
                if right[m] is i[k]:
                  rightflag = 1
        if wrongflag == 0:
          if rightflag == 0:
            subtotalpop += int(poplist[ziplist.index(i)])
            if j in i:
              #totalprob += prob[ziplist.index(i)]
              correctpop +=  int(poplist[ziplist.index(i)])
      totalprob = correctpop / subtotalpop
      totalproblist.append(totalprob)
    else:
      totalproblist.append(1)
  else:
    totalproblist.append(0)

#print totalproblist[0]

for j in n:
  print j,totalproblist[int(j)]
