#include <stdio.h>
void OR()
{
    printf("i j iORj\n");
    int a[2][2];
    for(int i=0;i<=1;i++)
    {
    for(int j=0;j<=1;j++)
    {
    a[i][j]=i||j;
    printf("%d %d %d\n",i,j,a[i][j]);
    }
    }
    printf("\n\n");
}
void AND()
{
    printf("i j iANDj\n");
    int b[2][2];
    for(int i=0;i<=1;i++)
    {
    for(int j=0;j<=1;j++)
    {
    b[i][j]=i&&j;
    printf("%d %d %d\n",i,j,b[i][j]);
    }
    }
    printf("\n\n");
}
void NOT()
{
    printf("i NOTi\n");
    int c[2];
    for(int i=0;i<=1;i++)
    {
    c[i]=!i;
    printf("%d %d\n",i,c[i]);
    }
}
int main() {
        
        OR();
        AND();
        NOT();
        return 0;
} 