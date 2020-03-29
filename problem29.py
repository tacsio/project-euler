#!/usr/bin/env python
# -*- coding:utf-8 -*-

def main():
	_sum = {}
	for i in xrange(2, 101):
		for j in xrange(2, 101):
			_sum[i**j] = i**j
	print len(_sum)
if __name__ == '__main__':
	main()
