import java.io.*;
public class List {
  public static void main (String args[]) {
    File folder=new File("/home/panchajanya/Documents/Programmings/Java/File Handling");
    String[] files = folder.list();
    for(String file:files) {
      System.out.println(file);
    }
    }
  }
