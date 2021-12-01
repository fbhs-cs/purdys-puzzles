import java.time.*;

public class November2021 {
    public static void main(String[] args){
        int total = 0;
        for(int i = 2001; i < 3001; i++){
            LocalDate date = LocalDate.of(i,Month.JANUARY,1);
            String dow = date.getDayOfWeek().toString();
            if(dow.equals("MONDAY"))
                total++;
            
            date = LocalDate.of(i,Month.FEBRUARY,1);
            dow = date.getDayOfWeek().toString();
            if(dow.equals("MONDAY"))
                total++;

            date = LocalDate.of(i,Month.MARCH,1);
            dow = date.getDayOfWeek().toString();
            if(dow.equals("MONDAY"))
                total++;

            date = LocalDate.of(i,Month.APRIL,1);
            dow = date.getDayOfWeek().toString();
            if(dow.equals("MONDAY"))
                total++;
            
            date = LocalDate.of(i,Month.MAY,1);
            dow = date.getDayOfWeek().toString();
            if(dow.equals("MONDAY"))
                total++;

            date = LocalDate.of(i,Month.JUNE,1);
            dow = date.getDayOfWeek().toString();
            if(dow.equals("MONDAY"))
                total++;

            date = LocalDate.of(i,Month.JULY,1);
            dow = date.getDayOfWeek().toString();
            if(dow.equals("MONDAY"))
                total++;

            date = LocalDate.of(i,Month.AUGUST,1);
            dow = date.getDayOfWeek().toString();
            if(dow.equals("MONDAY"))
                total++;

            date = LocalDate.of(i,Month.SEPTEMBER,1);
            dow = date.getDayOfWeek().toString();
            if(dow.equals("MONDAY"))
                total++;

            date = LocalDate.of(i,Month.OCTOBER,1);
            dow = date.getDayOfWeek().toString();
            if(dow.equals("MONDAY"))
                total++;

            date = LocalDate.of(i,Month.NOVEMBER,1);
            dow = date.getDayOfWeek().toString();
            if(dow.equals("MONDAY"))
                total++;

            date = LocalDate.of(i,Month.DECEMBER,1);
            dow = date.getDayOfWeek().toString();
            if(dow.equals("MONDAY"))
                total++;
        }
        System.out.println(total);

    }
}
