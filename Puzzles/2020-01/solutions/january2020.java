// Aaron Vera

public class january2020{
    public static void main(String[] args){
        sequence(2020);
    }

    public static int sequence(int n){
        int count = 6;
        int num2 = 15;
        int total = 15;

        while (count < n){
            String str = Integer.toString(num2);
            
            for (int i = 0; i < str.length();i++){
                int digit = Integer.valueOf(str.substring(i,i+1));
                total += digit;
            }

            num2 = total;
            count++;
        }
        System.out.println(total);
        return total;
    }
}