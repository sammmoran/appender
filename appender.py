#!/usr/bin/python

import sys, getopt
import argparse

def appender(final, argv):
  temp=open(sys.argv[1],'r')
  for line in temp:
    final.write(line)
    

def main(argv):
  final = open("final.json","w+")
  final.write('{\n"dashboard":\n')
  
  appender(final,argv)
  
  final.write('}')
  final.close()

if __name__ == "__main__":
  main(sys.argv[1:])
