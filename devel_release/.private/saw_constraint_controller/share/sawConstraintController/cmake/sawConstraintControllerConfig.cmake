#
# Author(s):  Anton Deguet
# Created on: 2013-05-15
#
# (C) Copyright 2013-2016 Johns Hopkins University (JHU), All Rights Reserved.
#

# this file is automatically generated by CMake from
# sawConstraintControllerConfig.cmake.in

set (sawConstraintController_VERSION_MAJOR "1")
set (sawConstraintController_VERSION_MINOR "1")
set (sawConstraintController_VERSION_PATCH "0")
set (sawConstraintController_VERSION "1.1.0")

# figure out if this file is where it was configured (build tree) or
# not (installed tree)
set (sawConstraintController_CMAKE_CONFIG_FILE "/home/jiameng/catkin_dvrk/devel_release/.private/saw_constraint_controller/share/sawConstraintController/cmake/sawConstraintControllerConfig.cmake")
get_filename_component (THIS_FILE_PATH
                        ${CMAKE_CURRENT_LIST_FILE}
                        REALPATH)

if ("${sawConstraintController_CMAKE_CONFIG_FILE}" STREQUAL "${THIS_FILE_PATH}")
  # we're using the build directories
  set (sawConstraintController_INCLUDE_DIR "/home/jiameng/catkin_dvrk/src/cisst-saw/sawConstraintController/components/include;/home/jiameng/catkin_dvrk/build_release/saw_constraint_controller/include")
  set (sawConstraintController_LIBRARY_DIR "/home/jiameng/catkin_dvrk/build_release/saw_constraint_controller/lib")
else ()
  # try to find the install dir, we know the install is using
  # share/sawConstraintController so we can go ../..
  set (RELATIVE_INSTALL_DIR "${THIS_FILE_PATH}/../..")
  get_filename_component (ABSOLUTE_INSTALL_DIR "${RELATIVE_INSTALL_DIR}" ABSOLUTE)
  # set directories using the install dir
  set (sawConstraintController_INCLUDE_DIR "${ABSOLUTE_INSTALL_DIR}/include")
  set (sawConstraintController_LIBRARY_DIR "${ABSOLUTE_INSTALL_DIR}/lib")
endif ()

set (sawConstraintController_LIBRARIES   "sawConstraintController")
