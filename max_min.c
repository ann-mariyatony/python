// Author : Ann mariya tony
// Description : Finding the maximum and minimum element in an array and its position
//Date: 11-02-2025

#include <stdio.h>
int main()
{
int i,n,max,min,p1=0,p2=0;
printf("Enter the array size:");
scanf("%d",&n);
int a[n];
printf("Enter the elements");
for (i=0;i<n;i++)
 {
   scanf("%d",&a[i]);
  } 
 printf("Elements are:");
 for(i=0;i<n;i++)
 {
   printf("%d\t",a[i]);
  }
max=a[0];
min=a[0];
for (i=1;i<n;i++)
 {
   if (a[i]>max)
     {
       max=a[i];
       p1=i;
     }
   if (a[i]<min)
     {
       min=a[i];
       p2=i;
     }
  }
printf("\nThe maximum element is %d in position %d",max,p1);
printf("\n The minimum element is %d in position %d",min,p2);
return 0;
}

