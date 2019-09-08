#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose2D
from turtlesim.msg import Pose


class PubGo2Goal:
    def __init__(self):
        rospy.init_node('PubGo2Goal')
        self.initControllerVariables()
        self.initROSChannels()
        rospy.spin()

    def initROSChannels(self):
        self.pose_listener = rospy.Subscriber("my_turtle/turtle1/pose", Pose, self.callbackPose)
        self.goal_listener = rospy.Subscriber("my_turtle/goal", Pose2D, self.callbackGoal)
        self.velocity_publisher = rospy.Publisher('my_turtle/turtle1/cmd_vel', Twist, queue_size=10)

    def initControllerVariables(self):
        self.vel_msg = Twist()
        self.current_pose = Pose()


    def callbackPose(self, msg):
            self.current_pose = msg
            print "X = " + str(self.current_pose.x) + "Y = " + str(self.current_pose.y)

    def callbackGoal(self, msg):
            rospy.loginfo(rospy.get_caller_id() + "I heard Goal")

    def goToPose(self, current_position, goal_position):
        r = rospy.Rate(0.5)  # 10hz
        self.vel_msg.linear.x = 10
        self.vel_msg.linear.y = 0
        self.vel_msg.linear.z = 0
        self.vel_msg.angular.x = 0
        self.vel_msg.angular.y = 0
        self.vel_msg.angular.z = 1.55
        rospy.spin()