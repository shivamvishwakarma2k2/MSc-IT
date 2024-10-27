import java.io.*;
import java.net.*;

public class TCPChatClient {
    public static void main(String[] args) {
        try {
            Socket s = new Socket("Localhost", 8000);
            System.out.println("Connected to server successfully");

            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

            DataOutputStream out = new DataOutputStream(s.getOutputStream());
            DataInputStream in = new DataInputStream(s.getInputStream());

            System.out.println("--- To stop chatting enter STOP ---");
            System.out.print("client : ");
            String msg;

            while ((msg = br.readLine()) != null) {
                out.writeBytes(msg + "\n");
                if (msg.toLowerCase().equals("stop")) {
                    System.out.println("--- Chat ended ---");
                    break;
                }

                System.out.println("server : " + in.readLine());
                System.out.print("client : ");
            }

            s.close();
            br.close();
            in.close();
            out.close();
        } catch (Exception e) {
            e.toString();
        }
    }
}
