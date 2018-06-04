public class Minimum {
  public static void main(String args[]){
    int minval=Integer.parseUnsignedInt(args[0]);
    for(int i=1;i<args.length;i++){
      if(Integer.parseUnsignedInt(args[i])<minval){
        minval=Integer.parseUnsignedInt(args[i]);
      }
    }
          System.out.println(minval);


  }
}
