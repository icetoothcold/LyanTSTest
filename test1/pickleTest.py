__author__ = 'Lyan'

try:
    import cPickle as pickle
except ImportError:
    import pickle

try:
    import os
except ImportError, e:
    print 'except:',e

import json


d = dict(name='Bob',age=20,score=88)
print d
d1 = pickle.dumps(d)
print d1
absPath=os.path.abspath('..')
print absPath
realPath=os.path.join(absPath, 'test2')
filePath=os.path.join(realPath, 'test2.txt')
print filePath
f = open(filePath,'wb')
#f.write('hello word')
pickle.dump(d,f)
f.close()
f = open(filePath,'rb')
d2 = pickle.load(f)
f.close()
print d2
print d

j1=json.dumps(d)
print j1
j2=json.loads(j1)
print j2










