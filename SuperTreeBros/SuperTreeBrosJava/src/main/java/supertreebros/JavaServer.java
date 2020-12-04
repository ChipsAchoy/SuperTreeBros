/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package supertreebros;

import java.io.*;
import java.net.*;
import supertreebros.comms.MessageReceiver;
import supertreebros.comms.SendMessage;
 
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
