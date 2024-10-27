import java.io.*;
import java.net.*;

public class TCPChatServer {
    public static void main(String[] args) {
        try {
            ServerSocket ss = new ServerSocket(8000);
            System.out.println("Waiting for client to connect....");
            Socket s = ss.accept();
            System.out.println("Connected to client successfully");

            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

            DataOutputStream out = new DataOutputStream(s.getOutputStream());
            DataInputStream in = new DataInputStream(s.getInputStream());

            String receive, send;

            while ((receive = in.readLine()) != null) {
                if (receive.toLowerCase().equals("stop")) {
                    System.out.println("--- Chat Ended from Client Side ---");
                    break;
                }
                System.out.println("client : " + receive);
                System.out.print("server : ");
                send = br.readLine();
                out.writeBytes(send + "\n");
            }
            ss.close();
            s.close();
            br.close();
            in.close();
            out.close();
        } catch (Exception e) {
            e.toString();
        }
    }
}
