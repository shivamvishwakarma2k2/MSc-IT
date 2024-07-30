import java.net.*;

public class A_UDPServerEvenOdd {
    public static void main(String args[]) {
        try {
            DatagramSocket ds = new DatagramSocket(2000);

            byte b[] = new byte[1024];

            DatagramPacket dp = new DatagramPacket(b, b.length);
            ds.receive(dp);

            String str = new String(dp.getData(), 0, dp.getLength());
            System.out.println("Number received : " + str);

            int a = Integer.parseInt(str);

            String result = new String();
            if (a % 2 == 0) {
                result = "Number is EVEN";
            } else {
                result = "Number is ODD";
            }
            byte b1[] = new byte[1024];
            b1 = result.getBytes();
            DatagramPacket dp1 = new DatagramPacket(b1, b1.length, InetAddress.getLocalHost(), 1000);
            ds.send(dp1);
            System.out.println("Response sended");

            ds.close();
        } catch (Exception e) {
            e.toString();
        }
    }

}
