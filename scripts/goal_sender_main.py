#!/usr/bin/env python

import exceptions
from ros_random_goal_sender import GoalSender

if __name__ == '__main__':
    try:
        sender = GoalSender()
    except Exception as e:
        print "Turtle goal sender node is running out of scope."