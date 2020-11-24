package supertreebros.trees;

/**
 *
 * @author Anthony Chaves
 */
public class Node {
    private int data;
    private Node right = null;
    private Node left = null;
    
    public Node(int data){
        this.data = data;
    }
    
    public void setRight(Node right){
        this.right = right;
    }
    
    public void setLeft(Node left){
        this.left = left;
    }
    
    public Node getRight(){
        return this.right;
    }
    
    public Node getLeft(){
        return this.left;
    }
    
    public int getData(){
        return this.data;
    }
}
