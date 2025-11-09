#pragma once

#include <cstddef>

template <typename T>
class IQueue {
 public:
  virtual ~IQueue() = default;

  virtual void push(const T& value) = 0;
  virtual T pop() = 0;
  virtual std::size_t size() const noexcept = 0;
};

template <typename T>
class IHeap {
 public:
  virtual ~IHeap() = default;

  virtual void push(const T& value) = 0;
  virtual T pop() = 0;
  virtual bool empty() const noexcept = 0;
};

template <typename Key, typename Value>
class IBinaryTree {
 public:
  virtual ~IBinaryTree() = default;

  virtual void push(const Key& key, const Value& value) = 0;
  virtual Value pop(const Key& key) = 0;
  virtual Value* search(const Key& key) = 0;
};

