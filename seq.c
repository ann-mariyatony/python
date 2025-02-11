#include <stdio.h>
int main()
{
int i,n,key,flag=0,pos=0;
printf("Enter the array size:");
scanf("%d",&n);
int a[n];
printf("Enter the elements:");
for (i=0;i<n;i++)
 {
   scanf("%d",&a[i]);
  }
printf("Enter the key to be found:");
scanf("%d",&key);
for (i=0;i<n;i++)
 {
   if (a[i]==key)
     {
       flag=1;
       pos=i;
       break;
     }
  }
if (flag==0)
   {
     printf("The element not found");
   }
else
   {
     printf("The element %d is found at position %d ",key,pos);
    }
return 0;
}
