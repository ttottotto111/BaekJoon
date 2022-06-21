#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif

#include<stdio.h>

int main()
{
	int card, num, result;
	int arr[100];

	scanf("%d %d", &card, &num);

	for (int i = 0; i < card; i++)
	{
		scanf("%d", &arr[i]);
	}

	result = 0;

	for (int i = 0; i < card; i++)
	{
		for (int j = i + 1; j < card; j++)
		{
			for (int k = j + 1; k < card; k++)
			{
				if (num - (arr[i] + arr[j] + arr[k]) < num - result && arr[i] + arr[j] + arr[k] <= num)
					result = arr[i] + arr[j] + arr[k];
			}
		}
	}

	printf("%d", result);
}