#!/usr/bin/env python

import exceptions
import Controller

if __name__ == '__main__':
    try:
        test = Controller.Controller()
    except Exception as e:
        print "Program is running out of scope."