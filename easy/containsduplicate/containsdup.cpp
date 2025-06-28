#include <iostream>
#include <vector>
#include <unordered_set>

bool hasDup(std::vector<int> nums) {
	std::unordered_set<int> seen;

	for (int num: nums) {
		if (seen.count(num) > 0) {
			return true;
		} 

		seen.insert(num);
	}

	return false;
}

int main () {

	std::cout << "This should return true" << std::endl;
	std::cout << hasDup({1,2,3,4,4}) << std::endl;
	std::cout << "" << std::endl;
	std::cout << "This should return false" << std::endl;
	std::cout << hasDup({1,2,3,4}) << std::endl;
	
	return 0;
}
