#!/usr/bin/env python
import rospy
from rospy_message_converter import json_message_converter
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Twist

# from agv_main.msg import agv_action
from rospy_message_converter.msg import agv_action


pub_cmd_vel = rospy.Publisher('cmd_vel', Twist, queue_size=10)
rospy.loginfo("agv_main.py-Publisher topic /cmd_vel")
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
        initPoseFunction()
    elif (action_mode == "ACTION_CHARGING_IN"):
        chargingInFunction()
    elif (action_mode == "ACTION_CHARGING_OUT"):
        chargingOutFunction()
    elif (action_mode == "ACTION_LIFT_IN"):
        liftInFunction()
    elif (action_mode == "ACTION_LIFT_UP"):
        liftUpFunction()
    elif (action_mode == "ACTION_LIFT_DOWN"):
        liftDownFunction()
    elif (action_mode == "ACTION_LIFT_OUT"):
        liftOutFunction()

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
def initPoseFunction():
    print ("agv_main.py-initPoseFunction")
def chargingInFunction():
    print ("agv_main.py-chargingInFunction")
def chargingOutFunction():
    print ("agv_main.py-chargingOutFunction")
def liftInFunction():
    print ("agv_main.py-liftInFunction")
def liftUpFunction():
    print ("agv_main.py-liftUpFunction")
def liftDownFunction():
    print ("agv_main.py-liftDownFunction")
def liftOutFunction():
    print ("agv_main.py-liftOutFunction")

if __name__ == '__main__':
    rospy.init_node('agv_main', log_level=rospy.DEBUG)

    rospy.Subscriber("agv_action", agv_action, initialAgvAction)
    rospy.loginfo("agv_main.py-Subscriber topic /agv_action")

    rospy.spin()