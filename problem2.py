#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Project Euler - Problem 2
# http://projecteuler.net/index.php?section=problems&id=2
#
# Solved by tcs5

def main():

	count = 2
	
	n1, n2 = 1, 2
	temp = 0
	flag = True
	
	while(flag):
		temp = n2
		n2 = n1 + n2
		n1 = temp
		
		if n2 % 2 == 0:
			if n2 + count > 4000000:
				flag = False
			count += n2


	print count
	
if __name__ == "__main__":
	main()
