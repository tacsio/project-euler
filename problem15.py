#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Project Euler Problem 15
# http://projecteuler.net/index.php?section=problems&id=15


def main():
	print fact(40)/fact(20)/fact(20)

def fact(n):
	f = 1
	for x in xrange(1, n+1):
		f = f * x
	
	return f

if __name__ == '__main__':
	main()
