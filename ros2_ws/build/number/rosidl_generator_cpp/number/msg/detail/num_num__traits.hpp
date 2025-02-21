// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from number:msg/NumNum.idl
// generated code does not contain a copyright notice

#ifndef NUMBER__MSG__DETAIL__NUM_NUM__TRAITS_HPP_
#define NUMBER__MSG__DETAIL__NUM_NUM__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "number/msg/detail/num_num__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace number
{

namespace msg
{

inline void to_flow_style_yaml(
  const NumNum & msg,
  std::ostream & out)
{
  out << "{";
  // member: a
  {
    out << "a: ";
    rosidl_generator_traits::value_to_yaml(msg.a, out);
    out << ", ";
  }

  // member: b
  {
    out << "b: ";
    rosidl_generator_traits::value_to_yaml(msg.b, out);
    out << ", ";
  }

  // member: sum
  {
    out << "sum: ";
    rosidl_generator_traits::value_to_yaml(msg.sum, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const NumNum & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: a
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "a: ";
    rosidl_generator_traits::value_to_yaml(msg.a, out);
    out << "\n";
  }

  // member: b
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "b: ";
    rosidl_generator_traits::value_to_yaml(msg.b, out);
    out << "\n";
  }

  // member: sum
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "sum: ";
    rosidl_generator_traits::value_to_yaml(msg.sum, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const NumNum & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace number

namespace rosidl_generator_traits
{

[[deprecated("use number::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const number::msg::NumNum & msg,
  std::ostream & out, size_t indentation = 0)
{
  number::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use number::msg::to_yaml() instead")]]
inline std::string to_yaml(const number::msg::NumNum & msg)
{
  return number::msg::to_yaml(msg);
}

template<>
inline const char * data_type<number::msg::NumNum>()
{
  return "number::msg::NumNum";
}

template<>
inline const char * name<number::msg::NumNum>()
{
  return "number/msg/NumNum";
}

template<>
struct has_fixed_size<number::msg::NumNum>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<number::msg::NumNum>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<number::msg::NumNum>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // NUMBER__MSG__DETAIL__NUM_NUM__TRAITS_HPP_
