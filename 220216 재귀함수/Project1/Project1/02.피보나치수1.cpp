#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif

#include<stdio.h>

int number(int n)
{
	if (n == 0)
		return 0;
	else if (n == 1)
		return 1;
	else 
	{
		return number(n - 1) + number(n - 2);
	}
}

int main()
{
	int a;

	scanf("%d", &a);

	printf("%d", number(a));

	return 0;
}