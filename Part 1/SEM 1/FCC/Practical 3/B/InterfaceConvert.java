import java.rmi.*;

public interface InterfaceConvert extends Remote {
    public String convertDigit(String no) throws Exception;
}
