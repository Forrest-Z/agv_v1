cmake_minimum_required(VERSION 3.0.2)
project(agv_main)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

##### Add by TungNV
add_message_files(
  FILES
  agv_action.msg
)
add_service_files(
  FILES
  lift_up.srv
)
generate_messages(
  DEPENDENCIES
  std_msgs
)
#########################

catkin_package(
  CATKIN_DEPENDS
    roscpp
    std_msgs
    message_runtime
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)
#add_library(agv_main
#  src/move_base.cpp

##### Add by TungNV

add_executable(agv_main src/agv_main.cpp)
add_dependencies(agv_main ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(agv_main ${catkin_LIBRARIES})
set_target_properties(agv_main PROPERTIES OUTPUT_NAME agv_main)

######################################################################

