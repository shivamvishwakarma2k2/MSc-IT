<%-- 
    Document   : index
    Created on : 28 Jul, 2024, 3:59:52 PM
    Author     : Shivam Vishwakarma
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <h1>Hello World!</h1>
        
            <%-- start web service invocation --%><hr/>
    <%
    try {
	org.me.calculator.CalculatorWS_Service service = new org.me.calculator.CalculatorWS_Service();
	org.me.calculator.CalculatorWS port = service.getCalculatorWSPort();
	 // TODO initialize WS operation arguments here
	int n1 = 16;
	int n2 = 8;
	// TODO process result here
	int result = port.add(n1, n2);
	out.println("Result = "+result);
    } catch (Exception ex) {
	out.println("exception" + ex);
    }
    %>
    <%-- end web service invocation --%><hr/>

    </body>
</html>
