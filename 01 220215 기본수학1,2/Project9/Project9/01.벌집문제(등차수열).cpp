#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h>

int main()
{
	int a;

	scanf("%d", &a);


	if (a == 1)
		printf("%d", a);
	else
	{
		for (int i = 0;; i++) {
			if (a <= 3 * i * i + 3 * i + 1)
			{
				printf("%d\n", i + 1);
				break;
			}
		}

		return 0;
	}
}