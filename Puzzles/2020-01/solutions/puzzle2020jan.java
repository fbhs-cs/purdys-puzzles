// Devin Schwartz
import java.util.ArrayList;

public class puzzle2020jan{
	public static void main( String[] args ){
        ArrayList<Integer> sequence=new ArrayList<Integer>();
        sequence.add(1);
        sequence.add(2);
        sequence.add(3);
        for (int i=0;i<2017;i++){
            sequence.add(sequence.get(sequence.size()-1)+sumInts(sequence.get(sequence.size()-1)));
        }
        for (int i=0;i<15;i++){
            System.out.println((i+1)+": "+sequence.get(i));
        }
        System.out.println("100: "+sequence.get(99));
        System.out.println("1000: "+sequence.get(999));
        System.out.println("2020: "+sequence.get(2019)+" (sum of digits: "+sumInts(sequence.get(2019))+")");

    }
    public static int sumInts(int num){
        int sum=0;
        while(num!=0){
            sum+=num%10;
            num/=10;
        }
        return sum;
    }
}
