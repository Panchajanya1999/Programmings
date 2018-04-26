import java.io.DataInputStream;
 
class Cosine {
    public static void main(String args[])
    {
		DataInputStream in=new DataInputStream(System.in);
		int n,k=-1,f=1,i,ch,t=0;
		double p,s=0,x,rad,r=0;
		try
		{
			System.out.println("Enter the values of x and n:");
			x=Float.valueOf(in.readLine()).floatValue();
			n=Integer.parseInt(in.readLine());
			System.out.println("\n1.Sine Series \n2.Cosine Series");
			System.out.println("Enter your choice : ");
			ch=Integer.parseInt(in.readLine());
			rad=3.14/180*x;
			if(ch==1)
			{
				s=rad;
				for(i=3;i<n;i+=2)
				{
					p=Math.pow(rad,i);
					f=f*(i-1)*i;
					r=p/f;
					s=s+k*r;
					k=k*(-1);
				}
				System.out.println("Sin("+x+")="+s);
			}
			else if(ch==2)
			{
				s=1.0;
			    for(i=2;i<n;i+=2)
			    {
			    	p=Math.pow(rad,i);
					f=f*(i-1)*i;
					r=p/f;
					s=s+k*r;
					k=k*(-1);
			    }
			    System.out.println("Cos("+x+")="+s);
			}
			else
				System.out.println("Wrong Choice!");	
		}
		catch(Exception e)
		{ 
			System.out.println("Error : "+e);
		}
    	}
}
