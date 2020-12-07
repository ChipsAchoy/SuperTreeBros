package supertreebros.comms;

import java.io.*;
import java.net.*;

/**
 * Clase para enviar enviar mensajes por medio de sockets
 * @author Anthony Chaves
 */ 
public class SendMessage {
    private Socket cliente;
    private int port;
    
    /**
     * Constructor de la clase de envio de mensajes
     * @param cliente socket al que se conectó el servidor
     */
    public SendMessage(Socket cliente){
        this.cliente = cliente;
    }
    /**
     * Método para enviar mensajes de tipo string por medio de los sockets
     * @param message string que será enviado
     */
    public void send(String message){
        try {
            PrintWriter out = new PrintWriter(this.cliente.getOutputStream(),true);
            out.println(message);
        } catch (Exception ex) {
            System.out.println(ex);
        }
    }
}
