#!/usr/bin/env python
from sys import stderr

print "Hello World",10,20,"AnotherString"
print "This is second Line"

print >>stderr, "This is error"
#python print.py  >out, redirects to stderr