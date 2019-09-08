#!/usr/bin/env python

import exceptions
import PubGo2Goal

if __name__ == '__main__':
    try:
        test = PubGo2Goal.PubGo2Goal()
    except Exception as e:
        print "Program is running out of scope."