package supertreebros.trees;

import java.lang.Math;
/**
 *
 * @author Anthony Chaves
 */
public abstract class BinaryTree {
    protected Node root = null;
    public abstract void append(int data);
    protected abstract Node append(int data, Node current);

    protected String getTree(Node initial){
        String output = "";
        if (this.root != null)
            output = BinTreePrinter.printGetTree(this.root);
        return output;
        
    }
    
}
