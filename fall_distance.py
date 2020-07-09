# Author: Erik Blackowicz
# Date: 7/8/20
# Description: Write a fx that returns the distance(m) an object has fallen, given the time(s) it takes to reach ground.

def fall_distance(time):
 ''' Returns the distance(meters) an object has fallen in a given time(seconds),
 using gravity as a constant.'''
 dist = (time*time)*4.9
 return(dist)