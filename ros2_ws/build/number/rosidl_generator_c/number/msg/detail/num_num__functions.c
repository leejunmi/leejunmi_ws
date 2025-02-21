// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from number:msg/NumNum.idl
// generated code does not contain a copyright notice
#include "number/msg/detail/num_num__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
number__msg__NumNum__init(number__msg__NumNum * msg)
{
  if (!msg) {
    return false;
  }
  // a
  // b
  // sum
  return true;
}

void
number__msg__NumNum__fini(number__msg__NumNum * msg)
{
  if (!msg) {
    return;
  }
  // a
  // b
  // sum
}

bool
number__msg__NumNum__are_equal(const number__msg__NumNum * lhs, const number__msg__NumNum * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // a
  if (lhs->a != rhs->a) {
    return false;
  }
  // b
  if (lhs->b != rhs->b) {
    return false;
  }
  // sum
  if (lhs->sum != rhs->sum) {
    return false;
  }
  return true;
}

bool
number__msg__NumNum__copy(
  const number__msg__NumNum * input,
  number__msg__NumNum * output)
{
  if (!input || !output) {
    return false;
  }
  // a
  output->a = input->a;
  // b
  output->b = input->b;
  // sum
  output->sum = input->sum;
  return true;
}

number__msg__NumNum *
number__msg__NumNum__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  number__msg__NumNum * msg = (number__msg__NumNum *)allocator.allocate(sizeof(number__msg__NumNum), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(number__msg__NumNum));
  bool success = number__msg__NumNum__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
number__msg__NumNum__destroy(number__msg__NumNum * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    number__msg__NumNum__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
number__msg__NumNum__Sequence__init(number__msg__NumNum__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  number__msg__NumNum * data = NULL;

  if (size) {
    data = (number__msg__NumNum *)allocator.zero_allocate(size, sizeof(number__msg__NumNum), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = number__msg__NumNum__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        number__msg__NumNum__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
number__msg__NumNum__Sequence__fini(number__msg__NumNum__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      number__msg__NumNum__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

number__msg__NumNum__Sequence *
number__msg__NumNum__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  number__msg__NumNum__Sequence * array = (number__msg__NumNum__Sequence *)allocator.allocate(sizeof(number__msg__NumNum__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = number__msg__NumNum__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
number__msg__NumNum__Sequence__destroy(number__msg__NumNum__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    number__msg__NumNum__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
number__msg__NumNum__Sequence__are_equal(const number__msg__NumNum__Sequence * lhs, const number__msg__NumNum__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!number__msg__NumNum__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
number__msg__NumNum__Sequence__copy(
  const number__msg__NumNum__Sequence * input,
  number__msg__NumNum__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(number__msg__NumNum);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    number__msg__NumNum * data =
      (number__msg__NumNum *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!number__msg__NumNum__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          number__msg__NumNum__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!number__msg__NumNum__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
