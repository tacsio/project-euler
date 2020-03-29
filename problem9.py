#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Euler Project Problem - 9
# http://projecteuler.net/index.php?section=problems&id=9
#
# by tcs5

def main():

	n = 1000
	
	for i in range(3, n):
		for j in range(i+1, n):
			k = n - (i + j)
			if k*k == i*i + j*j:
				print k*i*j


if __name__ == '__main__':
    main()
