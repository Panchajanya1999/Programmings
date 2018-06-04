import java.awt.*;
import java.applet.*;
import java.lang.Exception;
public class AppletInput extends Applet {
  TextField text1,text2;
  public void init() {
    text1=new TextField(8);
    text2=new TextField(8);
    add(text1);
    add(text2);
    text1.setText("0");
    text2.setText("0");
    //repaint();
  }
  public void paint(Graphics g) {
    int x=0,y=0,z=0;
    String s1,s2,s;
    g.drawString("Input a number :", 10, 50);
    //try{
      s1=text1.getText();
      x=Integer.parseInt(s1);
      s2=text2.getText();
      y=Integer.parseInt(s2);
  ////  }
    //catch(Exception E){
      z=x+y;
      s=String.valueOf(z);
      g.drawString("The Sum is :",10,75);
      g.drawString(s,100,75);
  //  }
  }
  public Boolean action (){
    repaint();
    return true;
  }
  }
