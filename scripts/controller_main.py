#!/usr/bin/env python

import exceptions
from controller import Controller

if __name__ == '__main__':
    try:
        controller = Controller()
    except Exception as e:
        print "Turtle controller node is running out of scope."