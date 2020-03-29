#!/usr/bin/env python
# -*- condign: utf-8 -*-

# Project Euler Problem 13
# http://projecteuler.net/index.php?section=problems&id=13

def main():
	arq = open('problem13.in', 'r')
	temp = 0
	for i in arq:
		temp += int(i.strip())
		
	a = str(temp)
	print a[:10]
	
	
if __name__ == '__main__':
	main()
