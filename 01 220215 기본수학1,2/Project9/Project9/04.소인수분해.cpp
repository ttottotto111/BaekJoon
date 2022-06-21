#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif

#include<stdio.h>

int main()
{
	int a, c=0, count = 0;
	int k = 2;
	scanf("%d", &a);

	while (a != 1)
	{	
		while(k <= a)
		{
			if (a % k == 0)
			{
				c++;	
				if (c == 1)
				{
					a = a / k;
					printf("%d\n", k);
					k = 2;
					c = 0;
				}
			}	
			else
			{
				k++;
			}
		}
	}
	return 0;
}