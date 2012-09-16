#!/usr/bin/python3

'''
Created on 28.11.2011

@author: savit
'''
import urllib
url = 'http://yandex.ru/yandsearch'
data = {'text': 'tra-la-la'}
request = '?'.join((url, urllib.urlencode(data)))   #для python2 
result = urllib.urlopen(request).read()             #для python2
print (result)