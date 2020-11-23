

package supertreebros.comms;

import java.io.*;
import java.net.*;

/**
 *
 * @author Anthony Chaves
 */
public class MessageReceiver implements Runnable{
    private Socket cliente = null;
    public boolean serverup = true;
    public String message = "";
    public MessageReceiver(Socket cliente){
        this.cliente = cliente;
        Thread th = new Thread(this);
        th.start();
    }
    
    @Override
    public void run() {
        SendMessage sender = new SendMessage(this.cliente);
        while (this.serverup) {

            try{
                String fromClient;
                BufferedReader in = new BufferedReader(new InputStreamReader(cliente.getInputStream()));
                this.message = in.readLine();
                System.out.println("received: " + this.message);
                    if (this.message.equals("Hello")){
                        System.out.println("Recibido");
                        sender.send(message);
                }
                
            }catch(Exception e){
                System.out.println(e.getMessage());
            }
        }
        try {
            this.cliente.close();
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }
                
    }
}
