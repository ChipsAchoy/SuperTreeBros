package supertreebros;

import java.io.IOException;
import java.net.ServerSocket;
import java.util.logging.Level;
import java.util.logging.Logger;
import supertreebros.comms.MessageReceiver;
import supertreebros.comms.SendMessage;

/**
 *
 * @author Anthony Chaves
 */
public class Main {
    public static void main(String[] args){
        ServerSocket server = null;
        try {
            //MessageReceiver server = new MessageReceiver();
            server = new ServerSocket(12002);
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }
        
        //SendMessage sender = new SendMessage(server);
        //while(true){
        //    sender.send("Holaa");
        //}
    }
}
