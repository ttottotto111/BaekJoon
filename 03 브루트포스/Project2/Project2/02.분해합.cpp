#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif

#include<stdio.h>

int main()
{
	int num, result = 0;
	int n1000000,n100000,n10000,n1000,n100, n10, n1;

	scanf("%d", &num);
	for (int i = 0; i < num; i++)
	{
		n1000000 = i / 1000000;
		n100000 = (i % 1000000) / 100000;
		n10000 = (i % 100000) / 10000;
		n1000 = (i % 10000) / 1000;
		n100 = (i % 1000) / 100;
		n10 = (i % 100) / 10;
		n1 = i % 10;
		result = i + n1000000 + n100000+ n10000+ n1000+ n100 + n10 + n1;
		if (result == num)
		{
			printf("%d", i);
			break;
		}
	}

	if (result != num)
		printf("%d", 0);

	return 0;
}