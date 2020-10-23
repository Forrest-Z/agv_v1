
#include <ros/ros.h>
#include "std_msgs/Int32.h"

enum ActionState {
    ACTION_FLOAT,
    ACTION_MANUAL,
    ACTION_MOVE_BASE,
    ACTION_INITIAL_POSE,
    ACTION_CHARGING_IN,
    ACTION_CHARGING_OUT,
    ACTION_LIFT_IN,
    ACTION_LIFT_UP,
    ACTION_LIFT_DOWN, 
    ACTION_LIFT_OUT 
};

ros::Publisher status_srv_pub_;
ros::Subscriber initial_pose_sub_, agv_action_;
ActionState action_state;
// void PublishStatusService(agv_main::agv_action action);
// agv_main::agv_action action_;
// void initSetup();
// void initialAgvAction(const agv_main::agv_actionConstPtr& msg);