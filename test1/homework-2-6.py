__author__ = 'Lyan'
a = raw_input('please input a number :')
print type(a)
num = int(a)
print type(num)
if num == 0:
    print '%d = 0' %num
elif num > 0:
    print '%d > 0' %num
else:
    print '%d < 0' %num