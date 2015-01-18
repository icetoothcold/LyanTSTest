__author__ = 'Lyan'
'''make a text file'''

import os
sep=os.linesep
myinput=raw_input('input end to exit >>>')
textfile=open('textfile.txt','w')
while myinput != 'end':

    textfile.writelines(myinput+sep)
    myinput=raw_input('input end to exit >>>')

textfile.close()
