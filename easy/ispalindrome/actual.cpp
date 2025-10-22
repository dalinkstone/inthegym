#include <string>
#include <iostream>

bool isPal(std::string word) {
	for(int i = 0; i <= word.length() - 1; i++) {
		if(word[i] != word[word.length() - 1 - i]) {
			return false;
		}
	}

	return true;
}

int main() {
	bool firstTest = isPal("monkey");
	bool secondTest = isPal("racecar");

	std::cout << "This first test is for the word monkey and should return false." << std::endl;
	std::cout << firstTest << std::endl;

	std::cout << "" << std::endl;

	std::cout << "This second test is for the word racecar and should return true." << std::endl;
	std::cout << secondTest << std::endl;
	
}
