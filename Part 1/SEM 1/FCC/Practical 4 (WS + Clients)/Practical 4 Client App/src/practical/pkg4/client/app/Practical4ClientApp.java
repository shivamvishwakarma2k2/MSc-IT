/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package practical.pkg4.client.app;

/**
 *
 * @author Shivam Vishwakarma
 */
public class Practical4ClientApp {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        try { 
            int i = 30; 
            int j = 42; 
            int result = add(i, j); 
            System.out.println("Result = " + result); 
        } catch (Exception ex) { 
            System.out.println("Exception: " + ex); 
        } 
    }
    
    private static int add(int n1, int n2) { 
        org.me.calculator.CalculatorWS_Service service = new org.me.calculator.CalculatorWS_Service(); 
        org.me.calculator.CalculatorWS port = service.getCalculatorWSPort(); 
        return port.add(n1, n2); 
    }   
}
