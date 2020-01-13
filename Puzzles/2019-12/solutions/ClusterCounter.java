// Egor Mikhaylov

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class ClusterCounter {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        Scanner fileScanner = getFileScanner(keyboard);
        String data = fileScanner.nextLine();
        int answer = countCluster(data);
        System.out.println(answer);
        fileScanner.close();
        keyboard.close();
    }

    public static int countCluster(String data) {
        int clusterCount = 0;
        int redBulbs = 0;
        int orangeBulbs = 0;
        int greenBulbs = 0;
        int blueBulbs = 0;
        int purpleBulbs = 0;
        String currCluster = "";
        for (int i = 0; i < data.length();) {
            if (currCluster.length() < 5) {
                currCluster += data.substring(i, i+1);
                i++;
                // System.out.println(currCluster);
            }
            if (currCluster.length() == 5) {
                for (int j = 0; j < currCluster.length(); j++) {
                    if (currCluster.substring(j, j+1).equals("R")) {
                        redBulbs++;
                    } else if (currCluster.substring(j, j+1).equals("O")) {
                        orangeBulbs++;
                    } else if (currCluster.substring(j, j+1).equals("G")) {
                        greenBulbs++;
                    } else if (currCluster.substring(j, j+1).equals("B")) {
                        blueBulbs++;
                    } else {
                        purpleBulbs++;
                    }
                }
                // System.out.printf("Red: %d, Orange: %d, Green: %d, Blue %d, Purple: %d\n", redBulbs, orangeBulbs, greenBulbs, blueBulbs, purpleBulbs);
                if (redBulbs == 1 && orangeBulbs == 1 && greenBulbs == 1 && blueBulbs == 1 && purpleBulbs == 1) {
                    clusterCount++;
                    currCluster = "";
                    redBulbs = 0;
                    orangeBulbs = 0;
                    greenBulbs = 0;
                    blueBulbs = 0;
                    purpleBulbs = 0;
                } else {
                    // System.out.println(currCluster);
                    currCluster = currCluster.substring(1);
                    redBulbs = 0;
                    orangeBulbs = 0;
                    greenBulbs = 0;
                    blueBulbs = 0;
                    purpleBulbs = 0;
                }
            }
        }
        return clusterCount;
    }

    public static Scanner getFileScanner(Scanner keyboard){
        Scanner result = null;
        try {
            System.out.print("Enter the name of the file with the personality data: ");
            String fileName = keyboard.nextLine().trim();
            System.out.println();
            result = new Scanner(new File(fileName));
        }
        catch(FileNotFoundException e) {
            System.out.println("Problem creating Scanner: " + e);
            System.out.println("Creating Scanner hooked up to default data " + e);
            String defaultData = "1\nDEFAULT DATA\n"
                + "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
                + "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA";
            result = new Scanner(defaultData);
        }
        return result;
    }


}