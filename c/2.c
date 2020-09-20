#include <stdio.h>

int main() {

	long long int total = 0;
	long long int numbers[2];
	long long int subtotal = 0;
	numbers[0] = 1;
	numbers[1] = 1;

	while (subtotal<=4000000)
	{
		subtotal = numbers[0]+numbers[1];
		if (subtotal%2==0) {total+=subtotal;}
		numbers[0]=numbers[1];
		numbers[1]=subtotal;
		//printf("New num: %d\n", subtotal);
	}

	printf("%d", total);

	return 0;

}
