// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from number:msg/NumNum.idl
// generated code does not contain a copyright notice

#ifndef NUMBER__MSG__DETAIL__NUM_NUM__STRUCT_HPP_
#define NUMBER__MSG__DETAIL__NUM_NUM__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__number__msg__NumNum __attribute__((deprecated))
#else
# define DEPRECATED__number__msg__NumNum __declspec(deprecated)
#endif

namespace number
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct NumNum_
{
  using Type = NumNum_<ContainerAllocator>;

  explicit NumNum_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->a = 0ll;
      this->b = 0ll;
      this->sum = 0ll;
    }
  }

  explicit NumNum_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->a = 0ll;
      this->b = 0ll;
      this->sum = 0ll;
    }
  }

  // field types and members
  using _a_type =
    int64_t;
  _a_type a;
  using _b_type =
    int64_t;
  _b_type b;
  using _sum_type =
    int64_t;
  _sum_type sum;

  // setters for named parameter idiom
  Type & set__a(
    const int64_t & _arg)
  {
    this->a = _arg;
    return *this;
  }
  Type & set__b(
    const int64_t & _arg)
  {
    this->b = _arg;
    return *this;
  }
  Type & set__sum(
    const int64_t & _arg)
  {
    this->sum = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    number::msg::NumNum_<ContainerAllocator> *;
  using ConstRawPtr =
    const number::msg::NumNum_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<number::msg::NumNum_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<number::msg::NumNum_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      number::msg::NumNum_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<number::msg::NumNum_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      number::msg::NumNum_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<number::msg::NumNum_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<number::msg::NumNum_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<number::msg::NumNum_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__number__msg__NumNum
    std::shared_ptr<number::msg::NumNum_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__number__msg__NumNum
    std::shared_ptr<number::msg::NumNum_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const NumNum_ & other) const
  {
    if (this->a != other.a) {
      return false;
    }
    if (this->b != other.b) {
      return false;
    }
    if (this->sum != other.sum) {
      return false;
    }
    return true;
  }
  bool operator!=(const NumNum_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct NumNum_

// alias to use template instance with default allocator
using NumNum =
  number::msg::NumNum_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace number

#endif  // NUMBER__MSG__DETAIL__NUM_NUM__STRUCT_HPP_
