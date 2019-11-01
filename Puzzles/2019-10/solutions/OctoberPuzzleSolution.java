/**
 * @author Alex Billiot
 * @since 10-8-2019
 *
 */

import java.util.*;
import java.io.*;
import static java.lang.System.*;
import java.math.BigInteger;
class OctoberPuzzleSolution{
    public static void main(String [] args){
        Long sum = new Long("0");
        BigInteger startNum = new BigInteger("2");
        startNum = startNum.pow(2203);
        startNum = startNum.subtract(new BigInteger("1"));
        LinkedList <Integer> sortedList = new LinkedList <Integer>();
        String forCharArray = startNum.toString();
        for(char numChar : forCharArray.toCharArray()){
            sortedList.add(Character.getNumericValue(numChar));
        }
        //sorts sortedList
        Collections.sort(sortedList);
        int [] sums = new int [9];
        //removes zeros
        while(sortedList.contains(0)){
            sortedList.removeFirst();
        }
        //sums digits 1-9 in sums array
        for(int i = 1; i < 10; i++){
            while(sortedList.contains(i)){
                sums [i-1] = sums [i-1] + 1;
                sortedList.removeFirst();
            }
        }
        //sums[x] = sum of x+1 digits ex 111111 sum[0] == 6, last part is the sum of sum[4] (sum of 5's) minus one decending, ex 52 + 51 + 50 ... + 1
        out.println(sums[0] * sums[8] + sums[1] * sums[7] + sums[2] * sums[6] + sums[3] * sums[5] + (sums[4]-1)/2.0 * sums[4]);
    }
}