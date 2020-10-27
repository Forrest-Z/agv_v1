#!/usr/bin/env python
import rospy
from rospy_message_converter import json_message_converter
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseWithCovarianceStamped

# from agv_main.msg import agv_action
from rospy_message_converter.msg import agv_action


pub_init_pose = rospy.Publisher('initialpose', PoseWithCovarianceStamped, queue_size=10)
rospy.loginfo("agv_main.py-Publisher topic /initialpose")
pub_cmd_vel = rospy.Publisher('cmd_vel', Twist, queue_size=10)
rospy.loginfo("agv_main.py-Publisher topic /cmd_vel")
pub_charging = rospy.Publisher('charging_action', agv_action, queue_size=10)
rospy.loginfo("agv_main.py-Publisher topic /charging_action")
pub_lift = rospy.Publisher('lift_action', agv_action, queue_size=10)
rospy.loginfo("agv_main.py-Publisher topic /lift_action")
pub_move_base_goal = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=10)
rospy.loginfo("agv_main.py-Publisher topic /move_base_simple/goal")

def actionMode(argument):
    switcher = {
        0: "ACTION_FLOAT",
        1: "ACTION_MANUAL",
        2: "ACTION_MOVE_BASE",
        3: "ACTION_INITIAL_POSE",
        4: "ACTION_CHARGING_IN",
        5: "ACTION_CHARGING_OUT",
        6: "ACTION_LIFT_IN",
        7: "ACTION_LIFT_UP",
        8: "ACTION_LIFT_DOWN",
        9: "ACTION_LIFT_OUT"
    }
    return switcher.get(argument, "Invalid action")

def initialAgvAction(msg):
    rospy.loginfo("agv_main.py-initialAgvAction()")   
    # typeData = "geometry_msgs/PoseStamped"
    # message = PoseStamped({"header": {"stamp": {"secs": 0, "nsecs": 0}, "frame_id": "", "seq": 1}, "pose": {"position": {"y": 0.0, "x": 0.0, "z": 0.0}, "orientation": {"y": 0.0, "x": 0.0, "z": 0.0, "w": 0.0}}})
    # data = json_message_converter.convert_ros_message_to_json(message)

    action = msg.action
    typeData = msg.type
    data = msg.data
    rospy.loginfo("agv_main.py-data: " + str(data))
    message = json_message_converter.convert_json_to_ros_message(typeData, data)
    rospy.loginfo("agv_main.py-type: %s", typeData)
    # rospy.loginfo("agv_main.py-message: %s", message)
    # rospy.loginfo("agv_main.py-action: " + str(action))
    action_mode = actionMode(action)
    rospy.loginfo("agv_main.py-action_mode: " + str(action_mode))
    if (action_mode == "ACTION_FLOAT"):
        floatFunction()
    elif (action_mode == "ACTION_MANUAL"):
        manualFunction(message)
    elif (action_mode == "ACTION_MOVE_BASE"):
        navigationFunction(message)
    elif (action_mode == "ACTION_INITIAL_POSE"):
        initPoseFunction(message)
    elif (action_mode == "ACTION_CHARGING_IN"):
        chargingInFunction(msg)
    elif (action_mode == "ACTION_CHARGING_OUT"):
        chargingOutFunction(msg)
    elif (action_mode == "ACTION_LIFT_IN"):
        liftInFunction(msg)
    elif (action_mode == "ACTION_LIFT_UP"):
        liftUpFunction(msg)
    elif (action_mode == "ACTION_LIFT_DOWN"):
        liftDownFunction(msg)
    elif (action_mode == "ACTION_LIFT_OUT"):
        liftOutFunction(msg)

def floatFunction():
    print ("agv_main.py-Do Nothing")
def manualFunction(msg):
    print ("agv_main.py-manualFunction")
    global pub_cmd_vel
    pub_cmd_vel.publish(msg)
    rospy.loginfo("agv_main.py-pub_cmd_vel")
def navigationFunction(msg):
    print ("agv_main.py-navigationFunction")
    global pub_move_base_goal
    pub_move_base_goal.publish(msg)
    rospy.loginfo("agv_main.py-pub_move_base_goal")
def initPoseFunction(msg):
    print ("agv_main.py-initPoseFunction")
    global pub_init_pose
    initPose = PoseWithCovarianceStamped()
    initPose.header = msg.header
    initPose.pose.pose = msg.pose
    pub_init_pose.publish(initPose)
def chargingInFunction(msg):
    print ("agv_main.py-chargingInFunction")
    global pub_charging
    pub_charging.publish(msg)
    rospy.loginfo("agv_main.py-publish chargingIn: " + str(msg))
def chargingOutFunction(msg):
    print ("agv_main.py-chargingOutFunction")
    global pub_charging
    pub_charging.publish(msg)
    rospy.loginfo("agv_main.py-publish chargingOut: " + str(msg))
def liftInFunction():
    print ("agv_main.py-liftInFunction")
def liftUpFunction(msg):
    print ("agv_main.py-liftUpFunction")
    global pub_lift
    pub_lift.publish(msg)
def liftDownFunction(msg):
    print ("agv_main.py-liftDownFunction")
    global pub_lift
    pub_lift.publish(msg)
def liftOutFunction():
    print ("agv_main.py-liftOutFunction")

if __name__ == '__main__':
    rospy.init_node('agv_main', log_level=rospy.DEBUG)

    rospy.Subscriber("agv_action", agv_action, initialAgvAction)
    rospy.loginfo("agv_main.py-Subscriber topic /agv_action")

    rospy.spin()