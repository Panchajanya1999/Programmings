import java.util.Scanner;
class SearchForEach
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
  System.out.println("Enter the number to be searched :");
  int a=sc.nextInt();
  boolean found=false;
  int c=0;
  for(int x:m)
  {
    ++c;
    if(x==a)
    {
      found=true;
       break;
    }
    else found=false;
  }
  if(found=true)
    System.out.println("Number "+a+" can be found at "+c+" position");
  if(found=false)
    System.out.println(a+" Cannot be found");
 }
}
