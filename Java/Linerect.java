import java.applet.*;
import java.awt.*;

public class Linerect extends Applet {
  public void paint(Graphics g) {
g.setColor(Color.green);
g.fillArc(500,40,300,400,360,180);//top arch
g.fillRect(500,270,300,320);//mid body
g.fillRoundRect(820,270,300,40,10,10);//right hand
g.fillRoundRect(180,270,300,40,10,10);//left hand
g.fillRoundRect(500,600,60,235,10,10);//left leg
g.fillRoundRect(740,600,60,235,10,10);//right leg

  }
}
