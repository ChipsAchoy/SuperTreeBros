package supertreebros.trees;

/**
 *
 * @author Anthony Chaves
 */
public class BstTree {
    private Node root = null;
    
    public void append(int data){
        this.root = this.append(data, this.root);
        
    }
    
    private Node append(int data, Node current){
        if (current == null){
            return new Node(data);
        }
        if (data < current.getData()){
            current.setLeft(this.append(data, current.getLeft()));
        }else if(data > current.getData()){
            current.setRight(this.append(data, current.getRight()));
        }
        return current;
    }
    
    public void printTree(){
        
    }
    
}
