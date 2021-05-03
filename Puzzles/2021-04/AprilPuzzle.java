import java.util.*;
import java.io.*;

public class AprilPuzzle{
    public static void main(String[] args)throws IOException{
        Scanner in = new Scanner(new File("precipitation_data.csv"));
        ArrayList<String> info = new ArrayList<String>();
        while(in.hasNext()) {
            String tempstr = in.nextLine();
            if(tempstr.charAt(tempstr.length()-1) == ',') {
                tempstr = tempstr + "0";
            }
            String temp[] = tempstr.split("[/,]");
            for(int i = 0; i < temp.length; i++) {
                info.add(temp[i]);
            }
        }
        for(int i = 1988; i < 2022; i++) {
            double hist[] = new double[12];
            boolean jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec;
            jan=feb=mar=apr=may=jun=jul=aug=sep=oct=nov=dec=false;
            double sum = 0;
            boolean valid = false;
            for(int j = 2; j < info.size(); j+=4) {
                int year = Integer.parseInt(info.get(j));
                if( year == i) {
                    int month = Integer.parseInt(info.get(j-2));
                    double rain = Double.parseDouble(info.get(j+1));
                    hist[month-1] = hist[month-1] + rain;
                    switch(month) {
                        case 1:
                            jan = true;
                            break;
                        case 2: 
                            feb = true;
                            break;
                        case 3:
                            mar = true;
                            break;
                        case 4:
                            apr = true;
                            break;
                        case 5: 
                            may = true;
                            break;
                        case 6:
                            jun = true;
                            break;
                        case 7:
                            jul = true;
                            break;
                        case 8: 
                            aug = true;
                            break;
                        case 9:
                            sep = true;
                            break;
                        case 10:
                            oct = true;
                            break;
                        case 11: 
                            nov = true;
                            break;
                        case 12:
                            dec = true;
                            break;
                    }
                }
            }
            valid = jan&&feb&&mar&&apr&&may&&jun&&jul&&aug&&sep&&oct&&nov&&dec;
            for(int j = 0; j < hist.length; j++) {
                sum += hist[j]; 
            }
            if(valid) {
                if(hist[3] > sum/12.0) {
                    System.out.println("April Showers - " + i);
                }
            }
        }
    }
}