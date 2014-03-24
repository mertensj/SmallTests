#!/usr/bin/python2

# Fibonacci Serie
#

a,b=0,1
while b < 1000:
	print b,
	a,b = b, a+b
print

# if statement
#

x=int(raw_input("Enter Integer: "))
if x<0 :
	x = 0
	print 'Negative number. Changed to zero'
elif x == 0 :
	print 'Zero'
elif x == 1 :
	print 'Single'
else :
	print 'More'
	
# for statement
#

words = [ 'cat' , 'cavia' , 'dog' ]

for w in words :
	print '-> ' , w , len(w)



