// Andres Flores

import java.util.Scanner;
import java.io.File;
import java.io.IOException;
import java.util.List;
import java.util.Arrays;

public class december {
    
    public static void main(String[] args) throws IOException {
        
        int count = 0;
        File textFile = new File("bulbs.txt");
        Scanner s = new Scanner(textFile);

        String text = s.next();
        String[] arrText = new String[text.length()];

        for (int i = 0; i < text.length(); i++) {
            arrText[i] = text.substring(i,i+1);
        }
        
        // if a grouping is found skip to after the group!

        for (int i = 0; i < arrText.length - 4; i++) {
            List<String> list = Arrays.asList(arrText).subList(i,i+5);

            if (list.containsAll(Arrays.asList("R","O","G","B","P"))) {
                count++;
                i+=4;
            }
        }

        System.out.println(count);
        s.close();
    }
}