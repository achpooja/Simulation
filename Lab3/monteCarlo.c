//Generate the vlaue of the PI using Monte-Carlo Method

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
int main()
{
    int square=0,circle=0,i;
    double rand_x,rand_y,r,pi;
   srand(time(NULL));

    for(int i=0;i<100000;i++)
    {
        rand_x=((double)rand())/RAND_MAX;
        rand_y=((double)rand())/RAND_MAX;

        r=rand_x*rand_x+rand_y*rand_y;

        if(r<1)
        circle++;
        square++;
    }
        pi=(double)(4*circle)/square;
        printf("Value of pi is %f",pi);

        return 0;
    
}