#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Project Euler - Problem 10
# http://projecteuler.net/index.php?section=problems&id=10
#
# by tcs5

#TODO Crivo errado

def main():
	
	n = 2000000
	r = 0
		
	for i in range(n):
		if is_prime(i):
			r += i

	print str(r)
	
def is_prime(n):

	if n < 2:
		return False
	elif n % 2 == 0:
		return (n == 2)
	elif n % 3 == 0:
		return (n == 3)
	elif n % 5 == 0:
		return (n == 5)
	else:
		for i in range(7, int(pow(n, 0.5))+1,30):
			if n % i == 0:
				return False
		return True

if __name__ == '__main__':
	main()
