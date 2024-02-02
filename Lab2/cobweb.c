// To simulate supply demand behaviour of market(Cobweb model).Lag Model for stable condition
#include<stdio.h>

int main()
{ 
    float p=1;
    float a=12.4 ,b=1.2,c=1.0,d=0.9;
    float s=0,q=0;
    FILE *fptr;
    fptr=fopen("cobweb.xls","w");
    for(int x=0; x<10; x++){
        s=c+d*p;
        q=s;
        p=(a-q)/b;

        printf("values: %f\t %f",q,p);
        printf("\n");
        fprintf(fptr,"%f\t%f\t%f\n",q,s,p);     
    }
    fclose(fptr);
    return 0;
}