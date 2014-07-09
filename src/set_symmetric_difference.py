'''
Created on Jul 9, 2014

@author: viejoemer

HowTo get the difference items of two or more sets in Python?

¿Cómo obtener los elementos diferentes de dos o más sets en Python?

symmetric_difference(other)
set ^ other ^ ...
Return a new set with elements in either the set or other but not both.
'''

#Create a set with values.
s = set([0,1,2,3])
print("set one", s)

s2 = set([1,6])
print("set two", s2)

#Get the symmetric difference
d = s.symmetric_difference(s2)
print("Items that aren't in one or the other",d)

s3 = set([3,4])
#Get the symmetric difference
d = s.symmetric_difference(s2).symmetric_difference(s3)
print("Items that aren't in one or the other",d)

#Other form set ^ other ^ ...
d = s ^ s2 ^ s3
print("Items that aren't in one or the other",d)
