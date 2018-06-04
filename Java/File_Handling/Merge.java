import java.io.*;
 
public class Merge 
{
    public static void main(String[] args) throws IOException 
    {
        // PrintWriter object for file3.txt
        PrintWriter pw = new PrintWriter("/home/panchajanya/Documents/Programmings/Java/File Handling/Box3/Text3.txt");
         
        // BufferedReader object for file1.txt
        BufferedReader br = new BufferedReader(new FileReader("/home/panchajanya/Documents/Programmings/Java/File Handling/Box1/Text1.txt"));
         
        String line = br.readLine();
         
        // loop to copy each line of 
        // file1.txt to  file3.txt
        while (line != null)
        {
            pw.println(line);
            line = br.readLine();
        }
         //Buffer reader for file2.txt
        br = new BufferedReader(new FileReader("/home/panchajanya/Documents/Programmings/Java/File Handling/Box2/Text2.txt"));
         
        line = br.readLine();
         
        // loop to copy each line of 
        // file2.txt to  file3.txt
        while(line != null)
        {
            pw.println(line);
            line = br.readLine();
        }
         
        pw.flush();
         
        // closing resources
        br.close();
        pw.close();
         
        System.out.println("Merged Text1.txt and Text2.txt into Text3.txt");
    }
}
