class PrimeCheck{
   void Check(int n){
    int i,m=n/2;
    boolean flag=true;
    if(n==0||n==1){
      System.out.println(n+" is not a Prime number");
    }
    else{
      for(i=2;i<=m;i++){
        if(n%i==0){
          flag=false;
          break;
        }

      }
    }
    if(flag) System.out.println(n+" is a Prime number");
    else System.out.println(n+" is not a Prime number");
  }
}
class Prime_Classes extends PrimeCheck{
  public static void main(String args[]){
    try{
    int num=Integer.parseInt(args[0]);
    PrimeCheck n=new PrimeCheck();
    n.Check(num);
  }
  catch(ArrayIndexOutOfBoundsException e){
    System.out.print("Out of Array \n"+e);
  }
  }
}
