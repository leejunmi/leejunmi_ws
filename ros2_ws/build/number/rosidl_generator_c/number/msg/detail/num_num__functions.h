// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from number:msg/NumNum.idl
// generated code does not contain a copyright notice

#ifndef NUMBER__MSG__DETAIL__NUM_NUM__FUNCTIONS_H_
#define NUMBER__MSG__DETAIL__NUM_NUM__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "number/msg/rosidl_generator_c__visibility_control.h"

#include "number/msg/detail/num_num__struct.h"

/// Initialize msg/NumNum message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * number__msg__NumNum
 * )) before or use
 * number__msg__NumNum__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_number
bool
number__msg__NumNum__init(number__msg__NumNum * msg);

/// Finalize msg/NumNum message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_number
void
number__msg__NumNum__fini(number__msg__NumNum * msg);

/// Create msg/NumNum message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * number__msg__NumNum__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_number
number__msg__NumNum *
number__msg__NumNum__create();

/// Destroy msg/NumNum message.
/**
 * It calls
 * number__msg__NumNum__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_number
void
number__msg__NumNum__destroy(number__msg__NumNum * msg);

/// Check for msg/NumNum message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_number
bool
number__msg__NumNum__are_equal(const number__msg__NumNum * lhs, const number__msg__NumNum * rhs);

/// Copy a msg/NumNum message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_number
bool
number__msg__NumNum__copy(
  const number__msg__NumNum * input,
  number__msg__NumNum * output);

/// Initialize array of msg/NumNum messages.
/**
 * It allocates the memory for the number of elements and calls
 * number__msg__NumNum__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_number
bool
number__msg__NumNum__Sequence__init(number__msg__NumNum__Sequence * array, size_t size);

/// Finalize array of msg/NumNum messages.
/**
 * It calls
 * number__msg__NumNum__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_number
void
number__msg__NumNum__Sequence__fini(number__msg__NumNum__Sequence * array);

/// Create array of msg/NumNum messages.
/**
 * It allocates the memory for the array and calls
 * number__msg__NumNum__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_number
number__msg__NumNum__Sequence *
number__msg__NumNum__Sequence__create(size_t size);

/// Destroy array of msg/NumNum messages.
/**
 * It calls
 * number__msg__NumNum__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_number
void
number__msg__NumNum__Sequence__destroy(number__msg__NumNum__Sequence * array);

/// Check for msg/NumNum message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_number
bool
number__msg__NumNum__Sequence__are_equal(const number__msg__NumNum__Sequence * lhs, const number__msg__NumNum__Sequence * rhs);

/// Copy an array of msg/NumNum messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_number
bool
number__msg__NumNum__Sequence__copy(
  const number__msg__NumNum__Sequence * input,
  number__msg__NumNum__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // NUMBER__MSG__DETAIL__NUM_NUM__FUNCTIONS_H_
