package supertreebros;

import java.io.IOException;
import java.net.ServerSocket;
import java.util.logging.Level;
import java.util.logging.Logger;
import supertreebros.comms.MessageReceiver;
import supertreebros.comms.SendMessage;
import supertreebros.trees.BstTree;

/**
 *
 * @author Anthony Chaves
 */
public class Main {
    public static void main(String[] args){
        BstTree bst = new BstTree();
        bst.append(5);
        bst.append(7);
        bst.append(10);
        bst.append(3);
        bst.append(2);
        
        bst.printTree();
    }
}
