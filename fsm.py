#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


class FSMRobot:
    def __init__(self):
        rospy.init_node('fsm_robot')

        # FSM states
        self.state = "FORWARD"

        self.cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber('/scan', LaserScan, self.scan_callback)

        self.min_dist = 0.5
        self.left_dist = 1.0
        self.right_dist = 1.0
        self.clear_dist = 0.7


        self.rate = rospy.Rate(10)

    def scan_callback(self, msg):
        ranges = msg.ranges

        front = min(ranges[0:15] + ranges[-15:])
        left  = min(ranges[30:60])
        right = min(ranges[-60:-30])

        self.left_dist = left
        self.right_dist = right

        if self.state == "FORWARD":
            if front < self.min_dist:
                self.state = "DECIDE"

        elif self.state in ["TURN_LEFT", "TURN_RIGHT"]:
            if front > self.clear_dist:
                self.state = "FORWARD"


    def run(self):
        while not rospy.is_shutdown():
            cmd = Twist()

            if self.state == "FORWARD":
                cmd.linear.x = 0.2
                cmd.angular.z = 0.0

            elif self.state == "DECIDE":
                # pilih arah dengan ruang lebih lega
                if self.left_dist > self.right_dist:
                    self.state = "TURN_LEFT"
                else:
                    self.state = "TURN_RIGHT"

            elif self.state == "TURN_LEFT":
                cmd.linear.x = 0.0
                cmd.angular.z = 0.6

            elif self.state == "TURN_RIGHT":
                cmd.linear.x = 0.0
                cmd.angular.z = -0.6

            self.cmd_pub.publish(cmd)
            self.rate.sleep()


if __name__ == "__main__":
    robot = FSMRobot()
    robot.run()
