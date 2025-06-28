#include <algorithm>
#include <iostream>

bool validAnagram(std::string first, std::string second) {

  if (first.length() != second.length())
    return false;

  std::sort(first.begin(), first.end());
  std::sort(second.begin(), second.end());

  return first == second;
}

int main() {
  std::cout << "this should return false (0), testing jar and jam" << std::endl;
  std::cout << validAnagram("jar", "jam") << std::endl;

  std::cout << "" << std::endl;

  std::cout << "this should return true (1), testing racecar and carrace"
            << std::endl;
  std::cout << validAnagram("racecar", "carrace") << std::endl;

  return 3;
}
