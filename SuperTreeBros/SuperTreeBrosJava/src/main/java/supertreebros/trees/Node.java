package supertreebros.trees;

/**
 *
 * @author Anthony Chaves
 */
public class Node {
    private int data;
    private int height;
    private Node right = null, left = null, parent = null;
    
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
    public void setHeight(int h){
        this.height = h;
    }
    public int getHeight(){
        return this.height;
    }
    public Node getParent(){
        return this.parent;
    }
    public void setParent(Node par){
        this.parent = par;
    }
}
