#!/bin/bash

# delete old logfiles
pushd ../../../..
rm -rf install/lib/sick_line_guidance/*
rm -rf install/share/sick_line_guidance/*
rm -f build/catkin_make_install.log

# make install
catkin_make install 2>&1 | tee -a build/catkin_make_install.log
source ./install/setup.bash

# lint, install by running
# sudo apt-get install python-catkin-lint
# catkin_lint -W1 src/sick_line_guidance

# print warnings and errors
echo -e "\nmake.bash finished.\n"
echo -e "catkin_make warnings:"
cat build/catkin_make_install.log | grep -i "warning:"
echo -e "\ncatkin_make errors:"
cat build/catkin_make_install.log | grep -i "error:"

# print sick_line_guidance install files, libraries, executables
echo -e "\ninstall/lib/sick_line_guidance:"
ls -al install/lib/sick_line_guidance/*
echo -e "\ninstall/share/sick_line_guidance:"
ls install/share/sick_line_guidance/*.*
popd

