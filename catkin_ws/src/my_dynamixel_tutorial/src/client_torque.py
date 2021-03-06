#!/usr/bin/env python
import roslib
roslib.load_manifest('my_dynamixel_tutorial')

import rospy
import actionlib
from std_msgs.msg import Float64
import trajectory_msgs.msg
import control_msgs.msg
from trajectory_msgs.msg import JointTrajectoryPoint
from control_msgs.msg import JointTrajectoryAction, JointTrajectoryGoal, FollowJointTrajectoryAction, FollowJointTrajectoryGoal



class Joint:
        def __init__(self, motor_name):
            #arm_name should be b_arm or f_arm
            self.name = motor_name
            self.jta = actionlib.SimpleActionClient('/'+self.name+'/follow_joint_trajectory', FollowJointTrajectoryAction)
            self.speed_pub = rospy.Publisher('/joint1_controller/command', Float64, queue_size=1)
            rospy.loginfo('Waiting for joint trajectory action')
            self.jta.wait_for_server()
            rospy.loginfo('Found joint trajectory action!')



        def move_joint(self, angles):
            goal = FollowJointTrajectoryGoal()
            char = self.name[0] #either 'f' or 'b'
            # goal.trajectory.joint_names = ['joint_1'+char, 'joint_2'+char]
            goal.trajectory.joint_names = ['claw_1f', 'claw_2f']
            # goal.trajectory.joint_names = ['joint1_controller' , 'joint2_controller']
            point = JointTrajectoryPoint()
            point.positions = angles
            point.time_from_start = rospy.Duration(1)
            goal.trajectory.points.append(point) 
            self.jta.send_goal_and_wait(goal)

        def speed_joint(self,speed):
            
            


def main():
            arm = Joint('f_arm_controller')
            arm.move_joint([0.0,0.0])
            arm.move_joint([3.14,3.14])




if __name__ == '__main__':
      rospy.init_node('joint_position_tester')
      main()
