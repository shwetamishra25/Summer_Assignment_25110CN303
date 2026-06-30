#include<stdio.h>
int main()
{
    int i,N,sum=0;
    printf("enter the limit N");
    scanf("%d",&N);
    for(i=0; i<=N; i++)
    {
        sum=sum+i;
    }
    printf("the sum of first %d natural numbers = %d",N,sum);
    return 0;
}