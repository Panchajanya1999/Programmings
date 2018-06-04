import java.util.*;
import java.lang.Math.*;
class Increment{
  public static void main(String args[]){
    System.out.println("Enter The number:");
    Scanner sc=new Scanner(System.in);
    int n=sc.nextInt();
    double b=0;
    for(int i=0;i<n;i++){
      double power=Math.pow((i+1),(i+1));
      b=b+power;
      }
      Double val=new Double(b);
     int intval=val.intValue();
     System.out.println(intval);
    }
}
