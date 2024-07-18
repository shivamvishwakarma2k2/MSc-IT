import java.io.*;
import java.net.*;

public class A_TCPClientPrimeCheck {
    public static void main(String[] args) {
        try {
            Socket s = new Socket("LocalHost", 8001);
            System.out.println("Connected to Server.");

            BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
            System.out.print("Enter a number : ");
            int a = Integer.parseInt(bf.readLine());

            DataOutputStream out = new DataOutputStream(s.getOutputStream());
            out.writeInt(a);

            DataInputStream in = new DataInputStream(s.getInputStream());
            System.out.println("Response : " + in.readUTF());

            s.close();
            in.close();
            out.close();
            bf.close();
        } catch (IOException e) {
            System.out.println(e.toString());
        } catch (Exception e) {
            System.out.println(e.toString());
        }
    }
}
