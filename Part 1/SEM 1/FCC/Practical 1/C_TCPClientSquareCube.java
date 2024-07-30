import java.io.*;
import java.net.*;

public class C_TCPClientSquareCube {
     public static void main(String[] args) {
        try {
            Socket s = new Socket("localhost", 8000);
           
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            DataOutputStream out = new DataOutputStream(s.getOutputStream());
            BufferedReader in = new BufferedReader(new InputStreamReader(s.getInputStream()));

            String numberStr;
            while (true) {
                System.out.print("Enter a number (or 'STOP' to quit): ");
                numberStr = br.readLine();
               
                out.writeBytes(numberStr + "\n");

                if (numberStr.equalsIgnoreCase("STOP")) {
                    break;
                }

                String serverResponse = in.readLine();
                System.out.println("Server response: " + serverResponse);
            }
            br.close();
            out.close();
            in.close();
            s.close();
           
        } catch (IOException e) {
            e.toString();
        }
        catch (Exception e) {
            e.toString();
        }
    }
}
