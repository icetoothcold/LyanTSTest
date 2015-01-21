#!/usr/bin/env python
__author__ = 'Lyan'

"""
use list to make a stack
"""

stack=[]


def pushIt() :
    iterm = raw_input('Please push the next iterm >>>').strip()
    stack.append(iterm)
    print '%s has been pushed in' %iterm
    return 0

def popIt() :
    if len(stack)==0:
        print 'the stack is empty'
    else:
        iterm=stack.pop()
        print '%s has been popped out' %iterm
    return 0

def viewStack() :
    print 'now the stack is :'
    print stack
    return 0

def showMenu() :
    pr = '''
    p(O)p
    p(U)sh
    (V)iew
    (Q)uit
    Enter choice:'''

    while True:
        choice = raw_input(pr).strip().lower()
        if choice not in 'ouvq':
            choice='q'
            print '***you have typed a wrong choice'
        print 'you picked %s choice' %choice
        if choice=='q':
            break
        CMDs[choice]()



CMDs={'o': popIt, 'u': pushIt, 'v': viewStack}
if __name__ == '__main__':
    showMenu()

