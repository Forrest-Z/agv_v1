#include "ros/ros.h"
#include <agv_main/agv_main.h>
#include <agv_main/agv_action.h>
// #include <agv_main/lift_up.h>s
#include <string>

#include <geometry_msgs/Twist.h>
#include "geometry_msgs/PoseStamped.h"


// bool lift_up_srv(agv_main::lift_up::Request  &req, agv_main::lift_up::Response &res)
// {
//   ROS_INFO("agv_main.cpp-7-lift_up_srv()");
//   action_.header.stamp = ros::Time::now();
//   action_.action = 5;
//   action_.status = 1;
//   PublishStatusService(action_);

//   res.sum = req.a + req.b;
//   ROS_INFO("agv_main.cpp-10-request: x=%ld, y=%ld", (long int)req.a, (long int)req.b);
//   ROS_INFO("agv_main.cpp-11-sending back response: [%ld]", (long int)res.sum);
//   return true;
// }
// bool lift_down_srv(agv_main::lift_up::Request  &req, agv_main::lift_up::Response &res)
// {
//   ROS_INFO("agv_main.cpp-16-lift_down_srv()");
//   return true;
// }
// bool charging_in_srv(agv_main::lift_up::Request  &req, agv_main::lift_up::Response &res)
// {
//   ROS_INFO("agv_main.cpp-21-charging_in_srv()");
//   return true;
// }
// bool charging_out_srv(agv_main::lift_up::Request  &req, agv_main::lift_up::Response &res)
// {
//   ROS_INFO("agv_main.cpp-26-charging_out_srv()");
//   return true;
// }

// void PublishStatusService(agv_main::agv_action action){
//   status_srv_pub_.publish(action);
//   ROS_INFO("agv_main.cpp-13-publish status action lift up!");
// }

void decodeJson(std::string type, std::string data){
  ROS_INFO("agv_main.cpp-59-type: %s", type.c_str());
  ROS_INFO("agv_main.cpp-60-data: %s", data.c_str());
}
void initialAgvAction(const agv_main::agv_action::ConstPtr& msg)
{
  ROS_INFO("agv_main.cpp-50-initialAgvAction()");
  uint8_t action, status;
  action = msg->action;
  status = msg->status;
  std::string type = msg->type;
  std::string data = msg->data;

  // std::string type = "geometry_msgs/PoseStamped";
  // std::string data = "{\"header":{"seq":1,"stamp":0,"frame_id":"map"},"pose":{"position":{"x":0,"y":0,"z":0},"orientation":{"x":0,"y":0,"z":0,"w":0}}}\";

  ROS_INFO("agv_main.cpp-57-action: %d", action);
  ROS_INFO("agv_main.cpp-58-status: %d", status);

  action_state = ActionState(action);
  switch(action_state){
    case ACTION_FLOAT:
      break;
    case ACTION_MANUAL:
      break;
    case ACTION_MOVE_BASE:
      decodeJson(type, data);
      break;
    case ACTION_INITIAL_POSE:
      break;
    case ACTION_CHARGING_IN:
      break;
    case ACTION_CHARGING_OUT:
      break;
    case ACTION_LIFT_UP:
      break;
    case ACTION_LIFT_DOWN:
      break;
    default:
    {}
  }
}

int main(int argc, char **argv)
{
  ROS_INFO("agv_main.cpp-41-main()");
  ros::init(argc, argv, "agv_main");

  // ros::ServiceServer lift_up_service_ = n.advertiseService("lift_up_", lift_up_srv);
  // ROS_INFO("agv_main.cpp-36-Advertise service: lift_up_");
  // ros::ServiceServer lift_down_service_ = n.advertiseService("lift_down_", lift_down_srv);
  // ROS_INFO("agv_main.cpp-38-Advertise service: lift_down_");
  // ros::ServiceServer chaging_in_service = n.advertiseService("charging_in_", charging_in_srv);
  // ROS_INFO("agv_main.cpp-40-Advertise service: chaging_in_");
  // ros::ServiceServer charging_out_service = n.advertiseService("charging_out_", charging_out_srv);
  // ROS_INFO("agv_main.cpp-42-Advertise service: chaging_out_");

  // // Publish the topic /current_pose
  // status_srv_pub_ = n.advertise<agv_main::agv_action>("agv_service_status", 0);
  // ROS_INFO("move_base.cpp-93-Publish topic: /agv_service_status");
  
  ros::NodeHandle n;
  action_state = ACTION_FLOAT;

  ros::Subscriber agv_action_ = n.subscribe("agv_action", 2, &initialAgvAction);
  ROS_INFO("agv_main.cpp-85-Subscriber topic: /agv_action");

  ros::spin();
  return 0;
}


