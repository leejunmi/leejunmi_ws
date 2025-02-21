# Install script for directory: /home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/leejunmi/ros2_ws/install/microstrain_inertial_driver")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/definitions" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/definitions/commands_3dm.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/definitions" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/definitions/commands_base.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/definitions" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/definitions/commands_filter.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/definitions" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/definitions/commands_gnss.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/definitions" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/definitions/commands_rtk.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/definitions" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/definitions/commands_aiding.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/definitions" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/definitions/commands_system.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/definitions" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/definitions/data_filter.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/definitions" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/definitions/data_gnss.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/definitions" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/definitions/data_sensor.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/definitions" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/definitions/data_shared.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/definitions" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/definitions/data_system.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/definitions" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/definitions/commands_3dm.hpp")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/definitions" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/definitions/commands_base.hpp")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/definitions" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/definitions/commands_filter.hpp")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/definitions" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/definitions/commands_gnss.hpp")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/definitions" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/definitions/commands_rtk.hpp")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/definitions" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/definitions/commands_aiding.hpp")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/definitions" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/definitions/commands_system.hpp")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/definitions" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/definitions/data_filter.hpp")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/definitions" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/definitions/data_gnss.hpp")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/definitions" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/definitions/data_sensor.hpp")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/definitions" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/definitions/data_shared.hpp")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/definitions" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/definitions/data_system.hpp")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/mip_interface.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/mip_device.hpp")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/mip_version.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/mip_cmdqueue.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/mip_dispatch.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/mip_field.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/mip_offsets.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/mip_packet.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/mip_parser.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/mip_result.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/mip_types.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/definitions" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/definitions/common.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/definitions" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/definitions/descriptors.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/mip.hpp")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/mip_all.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/mip_all.hpp")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/mip_logging.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/utils" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/utils/byte_ring.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/utils" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/utils/serialization.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/utils" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/utils/serial_port.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/utils" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/utils/tcp_socket.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/platform" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/platform/serial_connection.hpp")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/platform" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/platform/tcp_connection.hpp")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/extras" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/extras/composite_result.hpp")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/extras" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/extras/descriptor_id.hpp")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/extras" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/extras/device_models.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/extras" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/extras/index.hpp")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/extras" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/extras/recording_connection.hpp")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/extras" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/extras/scope_helper.hpp")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mip/extras" TYPE FILE FILES "/home/leejunmi/ros2_ws/src/microstrain_inertial/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/src/mip/extras/version.hpp")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "/home/leejunmi/ros2_ws/build/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/libmip.a")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/cmake/mip/mip-targets.cmake")
    file(DIFFERENT EXPORT_FILE_CHANGED FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/cmake/mip/mip-targets.cmake"
         "/home/leejunmi/ros2_ws/build/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/CMakeFiles/Export/share/cmake/mip/mip-targets.cmake")
    if(EXPORT_FILE_CHANGED)
      file(GLOB OLD_CONFIG_FILES "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/cmake/mip/mip-targets-*.cmake")
      if(OLD_CONFIG_FILES)
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/cmake/mip/mip-targets.cmake\" will be replaced.  Removing files [${OLD_CONFIG_FILES}].")
        file(REMOVE ${OLD_CONFIG_FILES})
      endif()
    endif()
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/cmake/mip" TYPE FILE FILES "/home/leejunmi/ros2_ws/build/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/CMakeFiles/Export/share/cmake/mip/mip-targets.cmake")
  if("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^()$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/cmake/mip" TYPE FILE FILES "/home/leejunmi/ros2_ws/build/microstrain_inertial_driver/microstrain_inertial_driver_common/mip_sdk/CMakeFiles/Export/share/cmake/mip/mip-targets-noconfig.cmake")
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmipx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/cmake/mip" TYPE FILE FILES
    "/home/leejunmi/ros2_ws/build/microstrain_inertial_driver/mip-config.cmake"
    "/home/leejunmi/ros2_ws/build/microstrain_inertial_driver/mip-config-version.cmake"
    )
endif()

