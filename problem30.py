#!/usr/bin/env python
# -*- coding:utf-8 -*-

def main():
	n = 0
	#limite: 9^5*6
	for i in range(2, 354294):
		if i == pot(i, 5):
			n += i
	print n
	
def pot(b, p=4):
	n = str(b)
	ret = 0
	for i in n:
		ret += int(i)**p
	return ret


if __name__ == '__main__':
	main()
