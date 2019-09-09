#!/usr/bin/env python

import exceptions
import Controller

if __name__ == '__main__':
    try:
        controller = Controller.Controller()
    except Exception as e:
        print "Turtle controller node is running out of scope."