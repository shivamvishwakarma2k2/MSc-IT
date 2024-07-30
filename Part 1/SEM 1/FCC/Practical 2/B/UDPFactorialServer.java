import java.net.*;

public class UDPFactorialServer {

    public static int fact(int n) {
        if (n == 1) {
            return 1;
        }
        return n * fact(n - 1);
    }

    public static void main(String args[]) {
        try {
            DatagramSocket ds = new DatagramSocket(2000);

            byte b[] = new byte[1024];

            DatagramPacket dp = new DatagramPacket(b, b.length);
            ds.receive(dp);

            String str = new String(dp.getData(), 0, dp.getLength());
            System.out.println("Number received : " + str);

            int a = Integer.parseInt(str);

            int result = fact(a);
            String resultStr = Integer.toString(result);

            byte b1[] = resultStr.getBytes();
            DatagramPacket dp1 = new DatagramPacket(b1, b1.length, dp.getAddress(), dp.getPort());
            ds.send(dp1);
            System.out.println("Response sent");

            ds.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
