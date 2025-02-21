// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from number:msg/NumNum.idl
// generated code does not contain a copyright notice

#ifndef NUMBER__MSG__DETAIL__NUM_NUM__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define NUMBER__MSG__DETAIL__NUM_NUM__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "number/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "number/msg/detail/num_num__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace number
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_number
cdr_serialize(
  const number::msg::NumNum & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_number
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  number::msg::NumNum & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_number
get_serialized_size(
  const number::msg::NumNum & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_number
max_serialized_size_NumNum(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace number

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_number
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, number, msg, NumNum)();

#ifdef __cplusplus
}
#endif

#endif  // NUMBER__MSG__DETAIL__NUM_NUM__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
