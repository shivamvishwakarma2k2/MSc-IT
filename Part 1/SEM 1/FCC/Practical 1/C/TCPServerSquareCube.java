import java.io.*;
import java.net.*;

public class TCPServerSquareCube {
    public static void main(String[] args) {
        try {
            ServerSocket ss = new ServerSocket(8000);
            System.out.println("Waiting for client to connect...");
           
            Socket s = ss.accept();
            System.out.println("Client connected.");

            BufferedReader in = new BufferedReader(new InputStreamReader(s.getInputStream()));
            DataOutputStream out = new DataOutputStream(s.getOutputStream());

            String receive;
            while ((receive = in.readLine()) != null) {
                try {
                    double number = Double.parseDouble(receive);
                   
                    double square = number * number;
                    double squareRoot = Math.sqrt(number);
                    double cube = number * number * number;
                    double cubeRoot = Math.cbrt(number);

                    String response = "Square: " + square + ", Square Root: " + squareRoot
                                    + ", Cube: " + cube + ", Cube Root: " + cubeRoot;

                    out.writeBytes(response + "\n");
                } catch (NumberFormatException e) {
                    out.writeBytes("Invalid input. Please enter a valid number.\n");
                }
            }
        
            in.close();
            out.close();
            s.close();
            ss.close();
           
        } catch (IOException e) {
            e.toString();
        } catch (Exception e) {
            e.toString();
        }
    }
}
