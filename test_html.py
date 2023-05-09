#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'测试HTMLParser'

__author__ = 'BanishedWay'

# 在python中，使用HTMLParser解析HTML
from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request


class MyHTMLParser(HTMLParser):
    _name = ''

    def handle_starttag(self, tag, attrs):
        # print(attrs)
        if len(attrs) == 1 and 'events/python-events/' in attrs[0][1]:
            self._name = 'Title'
        if len(attrs) > 0 and 'datetime' in attrs[0]:
            self._name = 'Time'
        if ('class', 'event-location') in attrs:
            self._name = 'Location'

    def handle_data(self, data):
        if self._name == 'Title':
            print('Events\'s name is', data)
            self._name = ''
        if self._name == 'Time':
            print('Time:', data)
            self._name = ''
        if self._name == 'Location':
            print('Location is', data, end='\n\n')
            self._name = ''

    def handle_endtag(self, tag):
        pass

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_comment(self, data):
        pass

    def handle_entityref(self, name):
        pass

    def handle_charref(self, name):
        pass


parser = MyHTMLParser()
URL = 'https://www.python.org/events/python-events/'
with request.urlopen(URL) as f:
    parser.feed(f.read().decode('utf-8'))