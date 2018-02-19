import java.util.Scanner;
class Box {
  double width,height,depth;
}
class BoxDemo {
  public static void main(String[] args) {
    Scanner sc=new Scanner(System.in);
    System.out.print("Enter width, height and depth :");
    Box mybox=new Box();
    mybox.width=sc.nextDouble();
    mybox.height=sc.nextDouble();
    mybox.depth=sc.nextDouble();

    double vol=mybox.width*mybox.height*mybox.depth;
    System.out.println("Volume is : "+vol);
  }
}
