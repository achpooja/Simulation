#include<stdio.h>

int main()
{
    FILE *fptr;
    fptr=fopen("om's.xl","w");

    float v,r,i;
    printf("Enter the value of v and r ");
    scanf("%f%f",&v,&r);
     for(int x=0;x<10;x++)
     {
        i=v/r;
        printf("The value of v and i are: %f\t %f" ,v,i);
        printf("\n");
        fprintf(fptr,"%f\t%f\n",v,i);
        v=v+5;

     }
     fclose(fptr);
     return 0;
}