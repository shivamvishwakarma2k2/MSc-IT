import java.rmi.*;

public class DateTimeClient {
    public static void main(String[] args) throws Exception {
        DateTimeInterface date = (DateTimeInterface) Naming.lookup("DTserver");
        String currentDate = date.showCurrentDateTime();
        System.out.println(currentDate);
    }
}
