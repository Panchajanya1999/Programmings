class Odd_Char{
  public static void main(String args[]){
    String s=args[0];
    for(int i=0;i<s.length();i=i+2){
      char c=s.charAt(i);
      System.out.println("The character at "+(i+1)+" place is "+c);
        }

  }
}
