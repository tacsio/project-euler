#!/usr/bin/env python
# -*- conding: utf-8 -*-

# Project Euler Problem 11
# http://projecteuler.net/index.php?section=problems&id=11
#
# Solved by tcs5

def main():

	global grid
	global maximo
	
	grid = get_array()
	maximo = 0

	for i in range(0,20):
		for j in range(0,20):
			if i < 17:
				test_down(i,j)
			if j < 17:
				test_right(i,j)
			if i < 17 and j < 17:
				test_diagonalD(i,j)
			if i < 17  and j > 2:
				test_diagonalE(i,j)
		
	print maximo
	
def test_down(i,j):
	global maximo
	temp = 1
	n = i + 3

	while(i <= n):
		temp *= grid[i][j]
		i += 1
		
	if (temp > maximo):
		maximo = temp
	
def test_right(i,j):
	global maximo
	temp = 1
	n = j + 3
	while(j <= n):
		temp *= grid[i][j]
		j += 1

	
	if(temp > maximo):
		maximo = temp
		
def test_diagonalD(i,j):
	global maximo
	temp = 1
	n = j + 3
	p = i + 3
	
	while(j <= n and i <= p):
		temp *= grid[i][j]
		i += 1
		j += 1
		
	if (temp > maximo):
		maximo = temp
		
	
def test_diagonalE(i,j):
	global maximo
	temp = 1
	n = j - 3 
	p = i + 3 
	
	while(n <= j and i <= p):
		temp *= grid[p][n]
		p -=1
		n +=1
	
	if(temp > maximo):
		maximo = temp
		
	
	
def get_array():
	grid = []
	arq = open('problem11.in', 'r')
	flag = 0
	for i in range(20):
		flag = 0
		temp = arq.readline().strip()
		grid.append([])
		for j in range(0,len(temp), 3):
			grid[i].append(int(temp[j:j+2]))

	return grid


if __name__ == '__main__':
	main()
