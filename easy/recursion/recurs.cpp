#include <iostream>
#include <stdlib.h>

int sumSquares(int n) {
	if (n <= 1) {
		return 1;
	} else {
		return n * n + sumSquares(n - 1);
	}
}

int main(void) {
	std::cout << "This should print 385" << std::endl;
	std::cout << sumSquares(10);
}
