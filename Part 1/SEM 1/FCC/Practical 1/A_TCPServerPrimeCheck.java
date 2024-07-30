import java.io.*;
import java.net.*;

public class A_TCPServerPrimeCheck {
    public static void main(String[] args) {
        try {
            ServerSocket ss = new ServerSocket(8001);
            System.out.println("Waiting for client");

            Socket s = ss.accept();
            System.out.println("Connected to client");

            DataInputStream in = new DataInputStream(s.getInputStream());
            int x = in.readInt();
            System.out.println("Number received : " + x);

            DataOutputStream out = new DataOutputStream(s.getOutputStream());

            if (x == 1) {
                out.writeUTF(x + " is nor a Prime nor a Composite.");
                System.exit(0);
            } else if (x == 2 || x == 3) {
                out.writeUTF(x + " is a Prime Number.");
                System.exit(0);
            }
            for (int i = 2; i <= x / 2; i++) {
                if (x % i != 0) {
                    out.writeUTF(x + " is a Prime number.");
                } else {
                    out.writeUTF(x + " is a Composite number.");
                }
            }

            ss.close();
            s.close();
            in.close();
            out.close();
        } catch (IOException e) {
            System.out.println(e.toString());
        } catch (Exception e) {
            System.out.println(e.toString());
        }
    }
}
