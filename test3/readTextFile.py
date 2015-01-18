#!user/bin/ env python
__author__ = 'Lyan'
'''read a text file'''

filename=raw_input('please input a text file name >>>')
try:
    textfile=open(filename,'r')
except IOError, e:
    print '*** file open err',e
#for a in textfile.readlines():
#    print a

#print textfile.read()

for eachline in textfile:
    print eachline