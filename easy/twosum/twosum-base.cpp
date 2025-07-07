#include <vector>
#include <iostream>
#include <unordered_map>

std::vector<int> twoSum(std::vector<int> nums, int target) {

  std::unordered_map<int, int> numbers;

  for (int i = 0; i < nums.size(); i++) {
    
    int difference = target - nums[i];

    if (numbers.find(difference) != numbers.end()) {
      std::vector<int> answer = {numbers[difference], i};
      return answer;
    }
    
    numbers[nums[i]] = i;

  }

  return {0, 0};
}

int main() {

  std::vector<int> oneTest = {3,4,5,6};
  std::vector<int> oneResult = twoSum(oneTest, 7);

  std::vector<int> twoTest = {4,5,6};
  std::vector<int> twoResult = twoSum(twoTest, 10);

  const char* separator = "";

  std::cout << "This should return an array of [0, 1], testing [3,4,5,6]" << std::endl;
  std::cout << "[";

  for (int elem: oneResult) {
    std::cout << separator << elem;
    separator = ", ";
  }

  std::cout << "]" << std::endl;

  separator = "";

  std::cout << "This should return an array of [0, 2], testing [4,5,6]" << std::endl;
  std::cout << "[";

  for (int elem: twoResult){
    std::cout << separator << elem;
    separator = ", ";
  }

  std::cout << "]" << std::endl;

  return 0;
}
