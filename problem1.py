#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Project Euler - Problem 1
# http://projecteuler.net/index.php?section=problems&id=1
#
# Solved by tcs5


def main():
	
	count = 0
	for i in range(1, 1000):
		if i%3 == 0:
			count += i
		elif i%5 == 0:
			count += i

	print count
			
if __name__ == "__main__":
	main()
