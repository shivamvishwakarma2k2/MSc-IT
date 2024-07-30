import java.rmi.*;

public interface DateTimeInterface extends Remote{
    public String showCurrentDateTime() throws Exception;
}