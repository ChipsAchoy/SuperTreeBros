package supertreebros.trees;

/**
 *
 * @author Anthony Chaves
 */
public class AvlTree extends BinaryTree{
    
    private void updateHeight(Node n) {
        n.setHeight(1 + Math.max(height(n.getLeft()), height(n.getRight())));
    }
 
    private int height(Node n) {
        return n == null ? -1 : n.getHeight();
    }
 
    private int getBalance(Node n) {
        return (n == null) ? 0 : height(n.getRight()) - height(n.getLeft());
    }
    
    @Override
    protected Node append(int data, Node current) {
        if (current == null){
            return new Node(data);
        }
        if (data < current.getData()){
            current.setLeft(this.append(data, current.getLeft()));
        }else{
            current.setRight(this.append(data, current.getRight()));
        }
        return this.rebalance(current);
    }
    
    private Node rotateRight(Node y) {
        Node x = y.getLeft();
        Node z = x.getRight();
        x.setRight(y);
        y.setLeft(z);
        updateHeight(y);
        updateHeight(x);
        return x;
    }
    Node rotateLeft(Node y) {
        Node x = y.getRight();
        Node z = x.getLeft();
        x.setLeft(y);
        y.setRight(z);
        updateHeight(y);
        updateHeight(x);
        return x;
    }
    private Node rebalance(Node z){
        updateHeight(z);
        int balance = getBalance(z);
        if (balance > 1) {
            if (height(z.getRight().getRight()) > height(z.getRight().getLeft())) {
                z = rotateLeft(z);
            } else {
                z.setRight(rotateRight(z.getRight()));
                z = rotateLeft(z);
            }
        } else if (balance < -1) {
            if (height(z.getLeft().getLeft()) > height(z.getLeft().getRight()))
                z = rotateRight(z);
            else {
                z.setRight(rotateLeft(z.getLeft()));
                z = rotateRight(z);
            }
        }
        return z;
    }
    
    @Override
    public void append(int data) {
        this.root = this.append(data, this.root);
    }

    public String getTree(){
        return super.getTree(this.root);
    }
    
}
