#include<stdio.h>

int main()
{
    float u;
    int a=5,c=3,m=16,z=2,d[20],count=0;
    for (int i=0;i<=15;i++){
        d[i]=z;
        z=(a*z+c)%m;
        u=z*1.0/m;
        printf("z= %d\t",z);
        printf("u= %f\t",u);
        printf("%d\n",d[i]);
    }
    for(int i=0;i<=15;i++){
        for(int j=0;j<=15;j++){
            if(d[j]>d[j+1]){
                int temp=d[j];
                d[j]=d[j+1];
                d[j+1]=temp;
            }
        }
    }

    for(int i=0;i<=15;i++){
        printf("%d\t",d[i]);
        if(d[i]!=d[i+1])
        count++;
    }
    printf("\n Count= %d",count);
    if(count==16){
        printf("\n Full Period");
    }
    else{
        printf("\n Not a Full Period");
    }
    return 0;
}