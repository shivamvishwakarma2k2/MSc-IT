import java.rmi.*;
import java.rmi.server.*;
import java.util.*;

public class DateTimeServer extends UnicastRemoteObject implements DateTimeInterface {
    public DateTimeServer() throws Exception {

    }

    @Override
    public String showCurrentDateTime() throws Exception {
        Date currentDateTime = new Date();
        return currentDateTime.toString();
    }

    public static void main(String[] args) throws Exception {
        DateTimeServer server = new DateTimeServer();
        Naming.bind("DTserver", server);
        System.out.println("Object registered");
    }
}
