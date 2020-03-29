#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Project Euler Problem 20
#
# http://projecteuler.net/index.php?section=problems&id=20
#
# Solved by tcs5

import time

def main():
	s = time.time()
	a = str(fat(100))
	ret = 0
	for i in a:
		ret += int(i)
		
	print ret
	print "Time: " + str(time.time() - s)
	

def fat(n):
	if n < 1:
		return 1
	else:
		return n*fat(n-1)

'''	
def fat(n):
	if (n==0 or n==1):
		return 1
		
	return fatac(1, n)

def fatac(i, n):
	if n==0:
		return i
	else:
		return fatac(i*n, n-1)
'''	
	
if __name__ == '__main__':
	main()
