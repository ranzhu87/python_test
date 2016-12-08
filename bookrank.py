#!/usr/bin/env python

import urllib
from atexit import register
from re import compile 
from threading import Thread 
from  time import ctime
import urllib2 

REGEX = compile('#([\d,]+) in Books ')
AMZIN = 'http://amazon.com/dp/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' 
headers = {'User-Agent':user_agent}

ISBNs = {
	'0132269937': 'Core Python Programming',
	'0132356139': 'Python Web Development with Django',
	'0137143419': 'Python Fundamentals',
}


def getRanking (isbn):
	print '%s%s' % (AMZIN,isbn)
	send_data = AMZIN+isbn
	req = urllib2.Request(send_data,None,headers)
	page = urllib2.urlopen(req)

	# page = uopen('%s%s' % (AMZIN,isbn))
	data = page.read()
	# print data
	page.close()
	return REGEX.findall(data)[0]


def _showRanking(isbn):


	print '-%r ranked %s' %(
		ISBNs[isbn],getRanking(isbn))


def main():
	print 'At',ctime(),'on Amazon...'
	for isbn in ISBNs:
		# _showRanking(isbn)
		Thread(target = _showRanking,args=(isbn,)).start()



@register
def _atexit():
	print 'all DONE at', ctime()



if __name__=='__main__':
	main()


