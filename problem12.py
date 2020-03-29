#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Project Euler Problem 12

def main():
	
	triangle_number = 4707846
	indice = 1
	num_divisores = 96
	
	while(num_divisores <= 500):
	
		indice += 1
		triangle_number = triangle_number + indice
		num_divisores = get_number_of_divisors(triangle_number)

	print triangle_number
	
def get_number_of_divisors(n):
	count = 0
	for num_divisores in xrange(1, n+1):
		if (n % num_divisores == 0):
			count += 1
	return count
	
if __name__ == '__main__':
	main()

