#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Project Euler Problem 14
# http://projecteuler.net/index.php?section=problems&id=14


def main():
	pd = {}
	maximo = 1
	indice = 1
	n = 1000000
	for i in xrange(1, n+1):
		temp = []
		j = i
		bol = True
		
		temp.append(i)
		
		while(j != 1 and bol):
			if (j % 2) == 0:
				j = j / 2
			else:
				j = 3*j+1
			
			try:
				x = pd[j]
				pd[i] = len(temp) + x
				bol = False
			except KeyError:
				temp.append(j)
			
		if bol:
			pd[i] = len(temp)
			
		if pd[i] > maximo:
			maximo = pd[i]
			indice = i
			
	print 'maximo = ' + str(maximo)
	print 'indice = ' + str(indice)
	
if __name__ == '__main__':
	main()
