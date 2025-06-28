#include <iostream>
#include <unordered_map>

bool validAnagram(std::string first, std::string second) {
	
	if (first.length() != second.length()) {
		return false;
	}

	std::unordered_map<char, int> countFirst;
	std::unordered_map<char, int> countSecond;

	for (int i = 0; i < first.length(); i++) {
		countFirst[first[i]]++;
		countSecond[second[i]]++;
	}

	return countFirst == countSecond;

}

int main () {

	std::cout << "this should return false (0), testing jar and jam" << std::endl;
	std::cout << validAnagram("jar", "jam") << std::endl;
	std::cout << "" << std::endl;
	std::cout << "this should return true (1), testing racecar and carrace" << std::endl;
	std::cout << validAnagram("racecar", "carrace") << std::endl;

	return 3;
}
