import math
import sys

x=int(sys.argv[1])
y=int(sys.argv[2])
z=int(sys.argv[3])

a='la-'*(x-1)+"la"
b=(a+" ")*(y-1)+a 

if y==0: b=''

if z==1: c='!' 
if z==0: c='.'

print 'Everybody sing a song:' + b + c
