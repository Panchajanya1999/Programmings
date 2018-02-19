import java.util.*;
class ForEach
{
 public static void main (String args[])
 {
  Scanner sc=new Scanner(System.in);
  System.out.println("How many numbers?");
  int n=sc.nextInt();
  int [] m=new int[n];
  System.out.println("Enter "+n+" numbers :");
  int i=0;
  for(;i<n;)
  { m[i]=sc.nextInt();
    i++;
  }
  int sum=0;
  for(int x:m)
  {
   System.out.println("Value is : "+x);
   sum +=x;
  }
  System.out.println("Summation is :"+sum);
 }
}

