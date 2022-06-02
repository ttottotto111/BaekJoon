#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif

#include<stdio.h>

#define MAX 1000001
int arr[MAX];

int main()
{
	int a, b;

	scanf("%d %d", &a, &b);
	
	for (int i = 2; i <=1000000; i++)
	{
		arr[i] = i;
	}

	//에라토스테네스의 체
	for (int i = 2; i <= 1000000; i++)
	{
		for (int j = i + i; j <= 1000000; j += i)
		{
			arr[j] = 0;
		}
	}
	
	for (int i = a; i <= b; i++)
	{
		if (arr[i] != 0)
			printf("%d\n", arr[i]);
	}

	return 0;
}