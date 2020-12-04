package supertreebros.comms;

import java.io.*;
import java.net.*;
import supertreebros.EventHandler;

/**
 *
 * @author Anthony Chaves
 */
public class MessageReceiver implements Runnable{
    private Socket cliente = null;
    public boolean serverup = true;
    public String message = "";
    private EventHandler eventhandler;
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
                if (this.message.substring(0, 5).equals("event")){
                    eventhandler = EventHandler.getInstace(this.message.substring(6, 9), Integer.parseInt(this.message.substring(10, 11)));
                    System.out.println("Nuevo evento");
                    sender.send("Confirmed");
                }else{
                    if (this.message.substring(0, 6).equals("finish"))
                        this.serverup = false;
                    eventhandler.parseNodes(this.message);
                    sender.send(eventhandler.getCurrentTree());
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
