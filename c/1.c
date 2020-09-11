#include <stdio.h>

int main()
{
	int returnVal = 0;
	
	for (int i=3; i<1000; i++)
	{
		if ((i%3==0) || (i%5==0))
		{
			returnVal+=i;
		}
	}

	printf("%d", returnVal);

	return 0;
}
