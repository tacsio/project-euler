#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Project Euler - Problem 4
# http://projecteuler.net/index.php?section=problems&id=4
#
# Solved by tcs5


def main():
	
	n1 = 101
	n2 = 101
	maximo = 0
	temp = n2
	
	for i in range(n1,999):
		for j in range(n2,999):
			temp = j*i
			if i <= j:
				if i % 10 != 0:
					if is_palindromo(str(temp)):
						if temp > maximo:
							maximo = temp
	print maximo
	
	
def is_palindromo(n):
	
	flag = True
	i = 0
	
	while(flag and i < len(n)):
		flag = (n[i] == n[-(i+1)])
		i += 1
	
	return flag

if __name__ == "__main__":
	main()
