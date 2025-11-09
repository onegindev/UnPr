#include <gmock/gmock.h>
#include <gtest/gtest.h>

#include <string>

#include "data_structures_interfaces.h"

namespace {

template <typename Key, typename Value>
class MockBinaryTree : public IBinaryTree<Key, Value> {
 public:
  MOCK_METHOD(void, push, (const Key& key, const Value& value), (override));
  MOCK_METHOD(Value, pop, (const Key& key), (override));
  MOCK_METHOD(Value*, search, (const Key& key), (override));
};

}  // namespace

TEST(BinaryTreeInterface, PushPopSequence) {
  testing::StrictMock<MockBinaryTree<int, std::string>> tree;
  testing::InSequence seq;

  EXPECT_CALL(tree, push(2, "root"));
  EXPECT_CALL(tree, push(1, "left"));
  EXPECT_CALL(tree, push(3, "right"));
  EXPECT_CALL(tree, pop(1)).WillOnce(testing::Return("left"));
  EXPECT_CALL(tree, pop(3)).WillOnce(testing::Return("right"));

  tree.push(2, "root");
  tree.push(1, "left");
  tree.push(3, "right");
  EXPECT_EQ(tree.pop(1), "left");
  EXPECT_EQ(tree.pop(3), "right");
}

TEST(BinaryTreeInterface, SearchReturnsAddressableValue) {
  testing::StrictMock<MockBinaryTree<int, std::string>> tree;
  std::string value = "found";

  EXPECT_CALL(tree, search(2)).WillOnce(testing::Return(&value));

  std::string* result = tree.search(2);
  ASSERT_NE(result, nullptr);
  EXPECT_EQ(*result, "found");
}

