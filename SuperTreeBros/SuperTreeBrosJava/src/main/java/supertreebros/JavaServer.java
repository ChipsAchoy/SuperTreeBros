package supertreebros;

import java.io.*;
import java.net.*;
import supertreebros.comms.MessageReceiver;
import supertreebros.comms.SendMessage;
/**
 * Clase main del server de Java
 * @author Anthony Chaves
 */ 
public class JavaServer {
    public static void main(String args[]) throws Exception {
        
        String toClient;
 
        ServerSocket server = new ServerSocket(12002);
        System.out.println("wait for connection on port 12002");
        Socket client = server.accept();
        MessageReceiver listener  = new MessageReceiver(client);
        //SendMessage sender = new SendMessage(client);
    }
}
