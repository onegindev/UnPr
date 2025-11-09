#include <gmock/gmock.h>
#include <gtest/gtest.h>

#include "data_structures_interfaces.h"

namespace {

template <typename T>
class MockHeap : public IHeap<T> {
 public:
  MOCK_METHOD(void, push, (const T& value), (override));
  MOCK_METHOD(T, pop, (), (override));
  MOCK_METHOD(bool, empty, (), (const, noexcept, override));
};

}  // namespace

TEST(HeapInterface, PushPopMaintainsPriorityContract) {
  testing::StrictMock<MockHeap<int>> heap;
  testing::InSequence seq;

  EXPECT_CALL(heap, push(3));
  EXPECT_CALL(heap, push(1));
  EXPECT_CALL(heap, push(5));
  EXPECT_CALL(heap, pop()).WillOnce(testing::Return(5));
  EXPECT_CALL(heap, pop()).WillOnce(testing::Return(3));
  EXPECT_CALL(heap, pop()).WillOnce(testing::Return(1));

  heap.push(3);
  heap.push(1);
  heap.push(5);
  EXPECT_EQ(heap.pop(), 5);
  EXPECT_EQ(heap.pop(), 3);
  EXPECT_EQ(heap.pop(), 1);
}

TEST(HeapInterface, EmptyReportsState) {
  testing::StrictMock<MockHeap<int>> heap;

  EXPECT_CALL(heap, empty()).WillOnce(testing::Return(true));
  EXPECT_TRUE(heap.empty());

  EXPECT_CALL(heap, push(testing::_));
  heap.push(10);

  EXPECT_CALL(heap, empty()).WillOnce(testing::Return(false));
  EXPECT_FALSE(heap.empty());
}

