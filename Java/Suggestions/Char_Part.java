class Char_Part {
  public static void main(String args[]){
  String charac=args[0];
  String part=args[1];
  char c=part.charAt(0);
    int count=0,i=0;
    for(;i<charac.length();i++){
      if(charac.charAt(i)==c){
        count++;
      }
    }
    System.out.println("Number of times "+part+" appeared is "+count);
  }
}
