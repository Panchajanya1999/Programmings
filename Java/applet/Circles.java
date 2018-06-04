import java.awt.*;
import java.applet.*;

public class Circles extends Applet {
  public void paint(Graphics g) {
    g.setColor(Color.red);
    g.fillOval(20,20,150,150);
    g.setColor(Color.green);
    g.fillOval(100,20,150,150);
    g.setColor(Color.blue);

    g.fillOval(60,70,150,150);

  }
}
