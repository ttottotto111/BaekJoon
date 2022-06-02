#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif

#include<stdio.h>

int count = 0;

int hanoicount(int n, int num1, int num2, int num3)
{
	if (n == 1)
	{
		count += 1;
	}
	else
	{
		hanoicount(n - 1, num1, num3, num2);
		count += 1;
		hanoicount(n - 1, num2, num1, num3);
	}
	return count;
}

void hanoi(int n, int num1, int num2, int num3)
{
	if (n == 1)
	{		
		printf("%d %d\n", num1, num3);
	}
	else
	{
		hanoi(n - 1, num1, num3, num2);
		printf("%d %d\n", num1, num3);
		hanoi(n - 1, num2, num1, num3);
	}
}

int main() {
	int a;
	
	scanf("%d", &a);
	
	printf("%d\n", hanoicount(a, 1, 2, 3));
	hanoi(a, 1, 2, 3);
}