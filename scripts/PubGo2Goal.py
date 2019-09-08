#!/usr/bin/env python

import angles as ros_angles
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose2D
import rospy
from turtlesim.msg import Pose

from math import pow, atan2, sqrt


class PubGo2Goal:
    def __init__(self):
        rospy.init_node('PubGo2Goal')
        self.initMemberVariables()
        self.initROSChannels()
        rospy.spin()

    def initROSChannels(self):
        self.pose_listener = rospy.Subscriber("turtle1/pose", Pose, self.callbackPose)
        self.goal_listener = rospy.Subscriber("goal", Pose2D, self.callbackGoal)
        self.velocity_publisher = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)

    def initMemberVariables(self):
        self.current_pose = Pose()

    def callbackPose(self, msg):
        self.current_pose = msg

    def callbackGoal(self, msg):
        current_goal = msg
        self.goToGoal(current_goal)

    def goToGoal(self, goal_position):
        rospy.loginfo("Moving PUT TURTLENAME to the pose: (" + str(goal_position.x) + " , " + str(
            goal_position.y) + ")" + " and theta = " + str(goal_position.theta))

        vel_msg = Twist()

        vel_msg.linear.y = 0
        vel_msg.linear.z = 0

        vel_msg.angular.x = 0
        vel_msg.angular.y = 0

        distance_tolerance = 0.1

        rate = rospy.Rate(5)

        while self.euclideanDistance(goal_position) >= distance_tolerance:

            vel_msg.linear.x = self.linearVelocity(goal_position)
            vel_msg.angular.z = self.angularVelocity(goal_position)

            self.velocity_publisher.publish(vel_msg)
            rate.sleep()

        vel_msg.linear.x = 0
        vel_msg.angular.z = 0

        self.velocity_publisher.publish(vel_msg)

    def euclideanDistance(self, goal_pose):
        return sqrt(pow((goal_pose.x - self.current_pose.x), 2) + pow((goal_pose.y - self.current_pose.y), 2))

    def linearVelocity(self, goal_pose, gain=1.5):
        return gain * self.euclideanDistance(goal_pose)

    def angularVelocity(self, goal_pose, gain=4):
        return gain * ros_angles.shortest_angular_distance(self.current_pose.theta, self.angleToTheGoal(goal_pose))

    def angleToTheGoal(self, goal_pose):
        return atan2(goal_pose.y - self.current_pose.y, goal_pose.x - self.current_pose.x)
