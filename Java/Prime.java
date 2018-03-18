import java.util.Scanner;
class Prime
{
   public static void main(String args[])
   {
	int temp;
	boolean isPrime=true;
  System.out.println("Enter any number:");
	int num = new Scanner(System.in).nextInt();
	for(int i=2;i<=num/2;i++)
	{
           temp=num%i;
	   if(temp==0)
	   {
	      isPrime=false;
	      break;
	   }
	}
	//If isPrime is true then the number is prime else not
	if(isPrime) System.out.println(num + " is a Prime Number");
	else System.out.println(num + " is not a Prime Number");
   }
}
