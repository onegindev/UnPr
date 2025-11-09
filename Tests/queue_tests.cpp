#include <gmock/gmock.h>
#include <gtest/gtest.h>

#include "data_structures_interfaces.h"

namespace {

template <typename T>
class MockQueue : public IQueue<T> {
 public:
  MOCK_METHOD(void, push, (const T& value), (override));
  MOCK_METHOD(T, pop, (), (override));
  MOCK_METHOD(std::size_t, size, (), (const, noexcept, override));
};

}  // namespace

TEST(QueueInterface, PushAndPopAreInvokedInOrder) {
  testing::StrictMock<MockQueue<int>> queue;
  testing::InSequence seq;

  EXPECT_CALL(queue, push(1));
  EXPECT_CALL(queue, push(2));
  EXPECT_CALL(queue, pop()).WillOnce(testing::Return(1));
  EXPECT_CALL(queue, pop()).WillOnce(testing::Return(2));

  queue.push(1);
  queue.push(2);
  EXPECT_EQ(queue.pop(), 1);
  EXPECT_EQ(queue.pop(), 2);
}

TEST(QueueInterface, SizeReflectsInteractions) {
  testing::StrictMock<MockQueue<int>> queue;

  EXPECT_CALL(queue, size()).WillOnce(testing::Return(0U));
  EXPECT_EQ(queue.size(), 0U);

  EXPECT_CALL(queue, push(testing::_));
  queue.push(42);

  EXPECT_CALL(queue, size()).WillOnce(testing::Return(1U));
  EXPECT_EQ(queue.size(), 1U);
}

