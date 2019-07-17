#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 12:54:48 2019

@author: one
"""

from random import randint


##creating empty lists
##these lists are used in the code further

box = list()
length=list()
ran_list=list()
val_list=list()
ratio=list()
half_list=list()


#creating a list of 50 entries
#full pill is represented by 2 in the list
#half pill is represented by 1

for i in range(50):
        box.append(2)



#since it takes 100 days for the box to get empty, the outer loop runs 100 iterations
for j in range(100):
    for i in range(len(box)):      
        
        ratio.append(sum(box[i] for i in range(len(box)) if box[i] == 1)/len(box))  ##this list stores the ratio of half pills(1) to full pills(2) in the box when each pill is selected(i.e for each iteration)
        
        half_list.append(sum(box[i] for i in range(len(box)) if box[i] == 1))    ##this list stores the number of half pills(1) in the box when each pill is selected(i.e for each iteration)
        
        random = randint(0,len(box)-1)   ## one pill is randomly selected from the list
        
        ran_list.append(random)    ##list stores the index of selected list
        
        value=box[random]
        
        val_list.append(value)     ## stores the value of selected element (whether full or half pill)

        if value == 2:            ## if the selected pill is full(2), it is replaced by half pill(1) in the box(list)
            
            box[random]=1         
        
        else:                     ##if the selected pill is half(1), it is removed from the box(list)
            
            del box[random]
            
        length.append(len(box))   ## this list stores the number of pills(both half and full) present in the box each day
        break
 

run1=ratio  ## run this code after first run
run2=ratio  ## run this code after second run
run3=ratio  ## run this code after third run
run4=ratio  ## run this code after fourth run

##average of the ratios is stored in list 

average_ratio_list = [(x + y + z + w)/4 for x, y, z, w in zip(run1,run2,run3,run4)]


##print the averages of each day    
for i in range(100):
    print("Day",i+1,"average",":",average_ratio_list[i])