#!/usr/bin/env python

import exceptions
import GoalSender

if __name__ == '__main__':
    try:
        sender = GoalSender.GoalSender()
    except Exception as e:
        print "Turtle goal sender node is running out of scope."