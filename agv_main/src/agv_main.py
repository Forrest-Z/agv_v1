#!/usr/bin/env python
import rospy
from rospy_message_converter import json_message_converter
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped

# from agv_main.msg import agv_action
from rospy_message_converter.msg import agv_action


def initialAgvAction(msg):
    
    # rospy.loginfo("agv_main.py-typeData: %s", msg.type)
    # rospy.loginfo("agv_main.py-data: %s", msg.data)

    # typeData = "std_msgs/String"
    # message = String(data = 'Hello')    
    typeData = "geometry_msgs/PoseStamped"
    # message = PoseStamped({header:{seq:1,stamp:0,frame_id:"map"},pose:{position:{x:0,y:0,z:0},orientation:{x:0,y:0,z:0,w:0}}})
    message = PoseStamped({"header":{"seq":1,"stamp":0,"frame_id":"map"},"pose":{"position":{"x":0,"y":0,"z":0},"orientation":{"x":0,"y":0,"z":0,"w":0}}})

    data = json_message_converter.convert_ros_message_to_json(message)
    rospy.loginfo("agv_main.py-data: %s", data)

    # typeData = "std_msgs/String"
    # data = '{"data": "Hello"}'
    # typeData = msg.type
    # data = msg.data
    message = json_message_converter.convert_json_to_ros_message(typeData, data)
    rospy.loginfo("agv_main.py-message: %s", message)

if __name__ == '__main__':
    rospy.init_node('agv_main', log_level=rospy.DEBUG)
    rospy.Subscriber("agv_action", agv_action, initialAgvAction)
    rospy.loginfo("agv_main.py-Subscriber topic /agv_action")
    rospy.spin()