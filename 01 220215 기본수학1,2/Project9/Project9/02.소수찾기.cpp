#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif

#include<stdio.h>

int main()
{
	int a, b[100],c=0 ,count=0, num;

	scanf("%d", &a);

	for (int i = 0; i < a; i++)
	{
		scanf("%d", &b[i]);
	}

	for (int j = 0; j < a; j++)
	{
		c = 0;
		num = b[j];
		if (num != 1)
		{
			for (int k = 2; k <= num; k++)
			{
				if (num % k == 0)
					c++;
			}

			if (c == 1) // �������� ���� 1�� ���� ���
				count+=1;
		}
	}
	printf("%d", count);
	return 0;
}