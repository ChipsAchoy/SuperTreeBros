package supertreebros.comms;

import java.io.*;
import java.net.*;

/**
 *
 * @author Anthony Chaves
 */ 
public class SendMessage {
    private Socket cliente;
    private int port;
    
    public SendMessage(Socket cliente){
        this.cliente = cliente;
    }
    
    public void send(String message){
        try {
            PrintWriter out = new PrintWriter(this.cliente.getOutputStream(),true);
            out.println(message);
        } catch (Exception ex) {
            System.out.println(ex);
        }
    }
}
