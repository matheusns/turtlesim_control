#!/usr/bin/env python

import angles as ros_angles
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose2D
import rospy
from turtlesim.msg import Pose

from math import pow, atan2, sqrt


class GoalSender:
    def __init__(self):
        rospy.init_node('turtle_pose_goal_sender')
        self.initMemberVariables()
        self.initROSChannels()
        self.randomGoalSender()

    def initMemberVariables(self):
        self.current_pose = Pose()

    def initROSChannels(self):
        self.pose_listener = rospy.Subscriber("turtle1/pose", Pose, self.callbackPose)
        self.goal_publisher = rospy.Subscriber("goal", Pose2D, queue_size=10)

    def randomGoalSender(self):
        r = rospy.Rate(0.5)  # 10hz
        while not rospy.is_shutdown():
            self.velocity_publisher.publish(self.vel_msg)
            r.sleep()
