import java.util.Scanner;
public class Split
{
    public static void main(String args[])
    {
        int n, m, a,counter = 0;
        System.out.print("Enter any number:");
        n = new Scanner(System.in).nextInt();
        m = n;
        while(n > 0)
        {
            n = n / 10;
            counter++;
        }
        while(m > 0)
        {
            a = m % 10;
            System.out.print("Digit at position "+counter+" -> "+a+" : ");
            words(a);
            System.out.print("\n");
            m = m / 10;
            counter--;
        }
    }
    public static void words(int k) {
      switch(k) {
        case 1: System.out.print("One");
                  break;
        case 2: System.out.print("Two");
                  break;
        case 3: System.out.print("Three");
                            break;
        case 4: System.out.print("Four");
                  break;
        case 5: System.out.print("Five");
                  break;
        case 6: System.out.print("Six");
                  break;
        case 7: System.out.print("Seven");
                  break;
        case 8: System.out.print("Eight");
                   break;
        case 9: System.out.print("Nine");
                  break;
        default : System.out.print("Zero");
                   break;
      }
    }
}
