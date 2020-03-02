// Alex Billiot
import java.util.*;
class FebPuzzle{
    public static void main(String [] args){
        int [] sto = new int [2020];
        for(int i = 0; i < 2020; i++){
            sto[i] = getSumDiv(i);
        }
        int low = 0;
        int high = 0;
        for(int l = 0; l < 2020; l++){
            for(int h = 2019; h > l; h--){
                if(sto[l] == sto[h] && high - low < h - l && sto[l] != 1){
                    low = l;
                    high = h;
                }
            }
        }
        System.out.println(high + " " + low);
        System.out.println(sto[high] + " " + sto[low]);
    }

    public static int getSumDiv(int in){
        int sum = 0;
        for(int i = 1; i < in; i++){
            if(in % i == 0){
                sum += i;
            }
        }
        return sum;
    }
}