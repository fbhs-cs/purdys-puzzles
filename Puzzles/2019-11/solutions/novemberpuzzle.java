public class novemberpuzzle {

    /**
     * returns the date of black friday
     */
    public static int getDate(int year){
        int[] dates = {24,23,29,28,27,26,25};
        int tracker = 0;
        for (int i =1; i <= year; i++){
            
            if (i % 400 == 0){
                tracker+=2;
            }
            else if (i % 4 == 0 && i % 100 !=0){
                tracker+=2;
            }
            else{
                tracker++;
            }
        }
        return dates[tracker % 7];
    }


    public static int numBlackFriday(){

        int count = 0;                     // counts num of black friday primes
        int[] calender = new int[2];       // {day , year}

        for (int i = 1; i < 3000; i++){    // cycles through every year
            calender[0] = getDate(i);       // c[0] = day
            calender[1] = i % 100;         // c[1] =  last 2 digits of year

            boolean isPrime = true;

            /*
            ===================
            * i = year , j = items in calender , k = every num < (j / 2)
            ===================
            */
            for (int j: calender){         // for elem in cal
                while (isPrime){
                    if (j == 0 || j == 1){ 
                        isPrime = false;
                        break;
                    }
                    for (int k = 2; k < (j/2) + 1; k++){ //prime checker
                        
                        if (j % k == 0){ // if j(nums in calender array) is divisble by any number(K); not prime
                            isPrime = false;
                            break;
                        }
                    }
                    break;
                }
                
            }
            if (isPrime){ // if isPrime is still true after all the checks
                count++;

                isPrime = false; //reset isPrime
            }
        }
        
        return count;
    }

    public static void main(String[] args){
        System.out.println(numBlackFriday());

    }


}