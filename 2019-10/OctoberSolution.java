import java.math.BigInteger;


public class OctoberSolution {

    public static void main(String[] args) {
        BigInteger num = BigInteger.valueOf(2);
        num = num.pow(2203);
        num = num.subtract(BigInteger.ONE);
        int count = 0;
        String numString = num.toString();
        //System.out.println(numString);
        for(int i = 0;i<numString.length()-1;i++) {
            for(int j = i+1; j<numString.length();j++) {
                int a = Integer.parseInt(numString.substring(i,i+1));
                int b = Integer.parseInt(numString.substring(j,j+1));
                if(a+b == 10) {
                    count++;
                }
            }
        }
        System.out.println(count);

    }
}