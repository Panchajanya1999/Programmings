import java.awt.*;
import java.applet.*;


public class House extends Applet 
{	
	public void paint(Graphics g) 
	{	
		
		g.setColor(Color.red);
		int xs[] = {100,160,220};
		int ys[] = {100,50,100};
		Polygon poly=new Polygon(xs,ys,3);
		g.fillPolygon(poly);
		
	
		g.setColor(Color.blue);
		g.fillRect(100,100,120,120);
		
	
		g.setColor(Color.black);
		g.fillRect(145,160,30,60);
		

		g.setColor(Color.yellow);
		g.fillOval(240,30,50,50);
		
	
		g.setColor(Color.black);
		g.fillRect(120,55,10,30);
	}
}