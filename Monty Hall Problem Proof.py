# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 17:51:02 2021

@author: layto
"""

#Monty Hall Problem
#main assumptions
#equal probability car behind each door at start
#once door picked host chooses one of the 2 remaining doors and opens one with a goat behind, 
#if both remaining doors have goats then the host chooses at random
#host canot open the contestants door choice
#this is a simulation to compare outcomes of staying and switching strategies and so prove switching provides statistically significant winning odds of 2/3

#random array of goat
import random
from scipy import stats
import matplotlib.pyplot as plt
trials=100000
stay=0
switch=0
for q in range(0,trials):
    cardoor=random.randint(1,3)
    useroriginalchoice=random.randint(1,3)
    #which door opened
    ######
    arr=[1,2,3]
    arr.remove(cardoor)
    if cardoor==useroriginalchoice:          
        opened=arr[random.randint(0,1)]
    else:    
        arr.remove(useroriginalchoice)
        opened=arr[0]
    arr=[1,2,3]
    arr.remove(opened)    
    #####section between hashtags unnecessary but remains to show how detail can be abstracted as doesnt matter in the end 
    #2x branches, switch and none switch
    #non switch
    if cardoor==useroriginalchoice:
        stay=stay+1   
    #switch
    if cardoor!=useroriginalchoice:#2 doors remaining so if not already behind chosen door, must be behind other and hence switch would get car
        switch=switch+1
        
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
plt.title('A bar chart to show the number of trials each strategy won')
ax.bar(['stay','switch'],[stay,switch])
plt.show()

print('number of trials', trials)        
print('probability stay will win ',stay/trials)
print('probability switch will win ',switch/trials)
print('hypothesis test, probability that result is due to chance and the switch/stay is a 50:50 choice is ',100*stats.binom_test(switch, n=trials, p=0.5),'%')#at first theorised 50:50 probability of success
if (100*stats.binom_test(switch, n=trials, p=0.5)<2.5):
    print('probabilities are statistically significant and hence prove the Monty Hall problem')
    
    


