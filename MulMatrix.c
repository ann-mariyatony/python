#include<stdio.h>
int main()
{
int r1,r2,c1,c2,i,j,k;
printf("Enter the size of first matrix:");
scanf("%d %d",&r1,&c1);
int a[r1][c1];
printf("Enter the elements:");
for(i=0;i<r1;i++)
  {
    for(j=0;j<c1;j++)
      {
        scanf("%d",&a[i][j]);
       }
  }
printf("Enter the size of second matrix:");
scanf("%d %d",&r2,&c2);
int b[r2][c2];
if (c1!=r2)
   {
     printf("Matrix multiplication can't be performed");
     return 0;
   }
printf("Enter the elements:");
for(i=0;i<r2;i++)
  {
    for(j=0;j<c2;j++)
      {
        scanf("%d",&b[i][j]);
       }
  }
  
int result[r1][c2];
for(i=0;i<r1;i++)
  {
    for(j=0;j<c2;j++)
      {
	result[i][j]=0;
       for(k=0;k<c1;k++)
         {
           result[i][j]= result [i][j] + a[i][k] * b[k][j];
        }
     }
  }
 printf("The result is:");
 for(i=0;i<r1;i++)
  {
    for(j=0;j<c2;j++)
      {
        printf("%d\t",result[i][j]);
       }
       printf("\n");
  }
  return 0;
  }
  
  
  
  
