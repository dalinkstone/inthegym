#include <iostream>
#include <vector>

std::vector<int> twoSum(std::vector<int> numbers, int target) {
  int l = 0;
  int r = numbers.size() - 1;
  std::vector<int> result;

  while (l < r) {
    int currentSum = numbers[l] + numbers[r];

    if (currentSum > target) {
      r -= 1;
    } else if (currentSum < target) {
      l += 1;
    } else {
      result.push_back(l + 1);
      result.push_back(r + 1);
      return result;
    }
  }

  return {0, 0};
}

int main(void) {

  std::vector<int> oneResult = twoSum({2, 4, 5, 6, 7}, 10);  

  std::cout << "This is TwoSum using two pointers\n" << std::endl;
  std::cout << "This first test is using an array [2, 4, 5, 6, 7] with a "
               "target of 10\n"
            << std::endl;
  std::cout << "We should expect the output of a one-based index vector [2, 4]"
            << std::endl;
  std::cout << "[";

  const char* separator = "";

  for (int elem : oneResult) {
    std::cout << separator << elem;
    separator = ", ";
  }

  std::cout << "]" << std::endl;

  return 0;
}
