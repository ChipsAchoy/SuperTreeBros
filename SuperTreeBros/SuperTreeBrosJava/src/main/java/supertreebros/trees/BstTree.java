package supertreebros.trees;

/**
 *
 * @author Anthony Chaves
 */
public class BstTree extends BinaryTree{
    
    @Override
    public void append(int data){
        this.root = this.append(data, this.root);
    }
    
    @Override
    protected Node append(int data, Node current){
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
    public String getTree(){
        return super.getTree(this.root);
    }
    
}
