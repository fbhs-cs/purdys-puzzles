// Alex Billiot
import java.io.*;
import java.util.*;
import static java.lang.System.*;
class solution{
    public static void main(String [] args) throws IOException{
        Scanner s = new Scanner(new File("bulbs.txt"));
        String str = s.nextLine();
        str = str.substring(0,100);
        out.println(str);

        int count = 0;
        for(int i = 5; i <= str.length(); i++){
            String sub = str.substring(i-5,i);
            if(sub.indexOf("G") != -1 && sub.indexOf("B") != -1 && sub.indexOf("P") != -1 && sub.indexOf("O") != -1 && sub.indexOf("R") != -1 ){
                i += 4;
                count++;
                //out.println(sub);
            }
        }
        out.println(count);
    }
}