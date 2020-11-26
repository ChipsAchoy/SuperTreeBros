package supertreebros.trees;

/**
 *
 * @author Anthony Chaves
 */
public class BstTree extends BinaryTree{
    private int current_depth = 0;
    
    @Override
    public void append(int data){
        this.current_depth = 1;
        this.elements++;
        this.root = this.append(data, this.root);
        if (this.current_depth > this.depth){
            this.depth = this.current_depth;
        }
    }
    
    @Override
    protected Node append(int data, Node current){
        if (current == null){
            return new Node(data);
        }else{
            this.current_depth ++;
        }
        if (data < current.getData()){
            current.setLeft(this.append(data, current.getLeft()));
        }else if(data > current.getData()){
            current.setRight(this.append(data, current.getRight()));
        }
        return current;
    }
    public void printTree(){
        super.printTree(this.root);
    }
    
}
