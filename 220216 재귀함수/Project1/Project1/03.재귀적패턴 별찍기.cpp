#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h>
#include <string.h>

char arr[2201][2201];

void star(int x, int y, int num)
{
    if (num == 1)
    {
        arr[x][y] = '*';
        return;
    }

    int div = num / 3;
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (i == 1 && j == 1)
                continue;
            else
                star(x + (i * div), y + (j * div), div);
        }
    }
}
int main()
{
    int a;
    scanf("%d", &a);

    memset(arr, ' ', sizeof(arr));

    star(0, 0, a);
    for (int i = 0; i < a; i++)
    {
        for (int j = 0; j < a; j++)
            printf("%c", arr[i][j]);
        printf("\n");
    }
}