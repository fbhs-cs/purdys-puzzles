// Alex Billiot
import java.util.*;
class January2020Puzzle {
  public static void main(String[] args) {
    ArrayList<Integer> sto = new ArrayList<Integer>();
    sto.add(1);
    sto.add(2);
    sto.add(3);
    for(int i = 3; i < 2020; i++){
      sto.add(i,sto.get(i-1) + sumInt(sto.get(i-1)));
    }
    System.out.println(sto.get(2019));
    System.out.println(sumInt(sto.get(2019)));
  }
  
  public static int sumInt(int num){
    int sum = 0;
    for(char c : (num + "").toCharArray()){
      sum += Character.getNumericValue(c);
    }
    return sum;
  }

}
