// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from number:msg/NumNum.idl
// generated code does not contain a copyright notice

#ifndef NUMBER__MSG__DETAIL__NUM_NUM__BUILDER_HPP_
#define NUMBER__MSG__DETAIL__NUM_NUM__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "number/msg/detail/num_num__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace number
{

namespace msg
{

namespace builder
{

class Init_NumNum_sum
{
public:
  explicit Init_NumNum_sum(::number::msg::NumNum & msg)
  : msg_(msg)
  {}
  ::number::msg::NumNum sum(::number::msg::NumNum::_sum_type arg)
  {
    msg_.sum = std::move(arg);
    return std::move(msg_);
  }

private:
  ::number::msg::NumNum msg_;
};

class Init_NumNum_b
{
public:
  explicit Init_NumNum_b(::number::msg::NumNum & msg)
  : msg_(msg)
  {}
  Init_NumNum_sum b(::number::msg::NumNum::_b_type arg)
  {
    msg_.b = std::move(arg);
    return Init_NumNum_sum(msg_);
  }

private:
  ::number::msg::NumNum msg_;
};

class Init_NumNum_a
{
public:
  Init_NumNum_a()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_NumNum_b a(::number::msg::NumNum::_a_type arg)
  {
    msg_.a = std::move(arg);
    return Init_NumNum_b(msg_);
  }

private:
  ::number::msg::NumNum msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::number::msg::NumNum>()
{
  return number::msg::builder::Init_NumNum_a();
}

}  // namespace number

#endif  // NUMBER__MSG__DETAIL__NUM_NUM__BUILDER_HPP_
