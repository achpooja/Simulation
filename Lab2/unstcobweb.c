//For unstable Condition

#include<stdio.h>

int main()
{ 
    float p=1.0;
    float a=12.4 ,b=1.2,c=7.0,d=-0.6;
    float s=0,q=0;
    FILE *fptr;
    fptr=fopen("cobwebunst.xls","w");
    for(int x=0; x<5; x++){
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