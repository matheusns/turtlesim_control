#!/usr/bin/env python

from math import pow, sqrt, pi
import random

from geometry_msgs.msg import Pose2D
import rospy
from turtlesim.msg import Pose


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
        self.goal_publisher = rospy.Publisher("goal", Pose2D, queue_size=10)

    def callbackPose(self, msg):
        self.current_pose = msg

    def randomGoalSender(self):
        r = rospy.Rate(1)
        goal_pose = Pose2D()
        tolerance = 0.5
        while not rospy.is_shutdown():
            if self.goal_publisher.get_num_connections() > 0:
                goal_pose.x = float(round(random.uniform(0.1, 10.0), 2))
                goal_pose.y = float(round(random.uniform(0.1, 10.0), 2))
                goal_pose.theta = float(round(random.uniform(-pi, pi), 2))
                self.goal_publisher.publish(goal_pose)

                while self.distanceToGoal(goal_pose) >= tolerance:
                    rospy.loginfo("Distance to goal = " + str(self.distanceToGoal(goal_pose)))
                    r.sleep()
            r.sleep()

    def distanceToGoal(self, goal_pose):
        return sqrt(pow((goal_pose.x - self.current_pose.x), 2) + pow((goal_pose.y - self.current_pose.y), 2))
