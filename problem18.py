#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Project Euler Problem 18
#
# http://projecteuler.net/index.php?section=problems&id=18
#
# Solved by tcs5

import time

def main():
	tStart = time.time()
	arq = open('problem18.in', 'r')
	array = []
	for i in range(15):
		temp = arq.readline().strip()
		array.append(temp.split(' '))

	for i in range(len(array)-1, 0, -1):
		for j in range(i):
			if (array[i][j] > array[i][j+1]):
				array[i-1][j] = int(array[i][j]) + int(array[i-1][j])
			else:
				array[i-1][j] = int(array[i][j+1]) +int(array[i-1][j])
	
	print array[0][0]
	print "Run Time = " + str(time.time() - tStart)

if __name__ == '__main__':
	main()
