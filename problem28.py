#!/usr/bin/env python
# -*- coding:utf-8 -*-

def main():
	diag1 = diag_ne(1001)
	diag2 = diag_no(diag1)
	diag3 = diag_se(diag2)
	diag4 = diag_so(diag1)
	total = 0
	total += sum_diag(diag1)
	total += sum_diag(diag2)	
	total += sum_diag(diag3)
	total += sum_diag(diag4)

	print total - 3

def sum_diag(n):
	s = 0
	for i in n:
		s += i
	return s

def diag_ne(n):
	l = []
	l.append(1)
	for i in range(1,(n+1)/2):
		l.append(l[i-1] + (i)*8)
	return l

def diag_no(d):
	l = []
	l.append(1)
	for i in range(1,len(d)):
		l.append(d[i] - (i)*2)
	return l

def diag_se(d):
	l = []
	l.append(1)
	for i in range(1, len(d)):
		l.append(d[i] - (i)*4)
	return l

def diag_so(d):
	l = []
	l.append(1)
	for i in range(1, len(d)):
		l.append(d[i] - (i)*4)
	return l

if __name__ == '__main__':
	main()
