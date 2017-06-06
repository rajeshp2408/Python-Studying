#!/usr/bin/python
#check a username and PIN
database=[
['test','1234'],
['abcd','1234'],
['9876','1234'],
['january','1234']
]
print 'Welcome, to Authorize window!! Login below'
user=raw_input("\nEnter username :")
passwd=raw_input("\nEnter password :")
if [user,passwd] in database: 
 print 'Access Granted'
else:
 print 'Access denied! Try again'
