#include<stdio.h>
int sum(int n);

int main(){
    int number, result;
    printf("enter a positive integer : \n");
    scanf("%d", &number);
    result = sum(number);
    printf("sum = %d \n", result);
    return 0;
}

int sum(int n){
    if(n != 0)
       return n + sum(n-1);
    else
       return n;
}
