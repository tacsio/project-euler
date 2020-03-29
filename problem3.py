#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Project Euler - Problem 3
# http://projecteuler.net/index.php?section=problems&id=3
#
# Solved by tcs5

def main():
	
	count = 1
	maximo = 0
	i = 3
	while count < 600851475143:
		
		if 600851475143 % i == 0:
			if is_prime(i):
				count *= i
				maximo = i
		i += 1	
	
	print maximo
	
def is_prime(n):
	
	if n < 2:
		return False
	if n == 2:
		return True
	else:
		for i in range(n-1, 1, -1):
			if n % i == 0:
				return False
			else:
				b = True
		return b	
	
if __name__ == "__main__":
	main()
