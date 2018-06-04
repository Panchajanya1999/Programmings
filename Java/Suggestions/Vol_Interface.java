interface Volume{
  final static double pi=3.141;
  double compute(double x,double y,double z);
}
class Sphere implements Volume{
  public double compute(double x, double y,double z){
    return(1.333*pi*x*x*x);
  }
}

class Cube implements Volume{
  public double compute(double x,double y, double z){
    return(x*x*x);
  }
}

class Rectangle implements Volume{
  public double compute(double x,double y, double z){
    return(x*y*z);
  }
}
class Vol_Interface{
  public static void main(String args[]){
    Sphere sph=new Sphere();
    Cube cub=new Cube();
    Rectangle rect=new Rectangle();
    System.out.println("Volume of Sphere = "+sph.compute(9,0,0));
    System.out.println("Volume of Cube = "+cub.compute(9,0,0));
    System.out.println("Volume of Rectangle = "+rect.compute(9,8,7));
  }
}
