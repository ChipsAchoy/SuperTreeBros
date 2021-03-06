package supertreebros.trees;

/**
 * Árbol Splay, proveniente del template method de árbol binario
 * @author Anthony Chaves
 */
public class SplayTree extends BinaryTree{
    /**
     * Realiza un single rotation hacia la izquierda (zag)
     * @param x nodo que será rotado
     */
    public void leftRotate(Node x) {
        Node y = x.getRight();
        x.setRight(y.getLeft());
        if(y.getLeft() != null) {
          y.getLeft().setParent(x);
        }
        y.setParent(x.getParent());
        if(x.getParent() == null) { //x is root
          this.root = y;
        }
        else if(x == x.getParent().getLeft()) { //x is left child
          x.getParent().setLeft(y);
        }
        else { //x is right child
          x.getParent().setRight(y);
        }
        y.setLeft(x);
        x.setParent(y);
    }
    /**
     * Realiza un single rotation hacia la derecha (zig)
     * @param x nodo que será rotado
     */
    public void rightRotate(Node x) {
        Node y = x.getLeft();
        x.setLeft(y.getRight());

        if(y.getRight() != null) {
          y.getRight().setParent(x);
        }

        y.setParent(x.getParent());
        if(x.getParent() == null) {
          this.root = y;
        }
        else if(x == x.getParent().getRight()) { //x is left child
          x.getParent().setRight(y);
        }
        else { //x is right child
          x.getParent().setLeft(y);
        }
        y.setRight(x);
        x.setParent(y);
    }
    /**
     * Realiza la operación de splay al árbol, moviéndolo en función de mostrar
     * el nodo nuevo en la raíz
     * @param n nodo al que se le realiza el splay
     */
    public void splay(Node n) {
        while(n.getParent() != null) { //node is not root
            if(n.getParent() == this.root) { //node is child of root, one rotation
                if(n == n.getParent().getLeft()) {
                  this.rightRotate(n.getParent());
                }
                else {
                  this.leftRotate(n.getParent());
                }
            }
            else {
                Node p = n.getParent();
                Node g = p.getParent(); //grandparent

                if(n.getParent().getLeft() == n && p.getParent().getLeft() == p) { //both are left children
                  this.rightRotate(g);
                  this.rightRotate(p);
                }
                else if(n.getParent().getRight() == n && p.getParent().getRight() == p) { //both are right children
                  this.leftRotate(g);
                  this.leftRotate(p);
                }
                else if(n.getParent().getRight() == n && p.getParent().getLeft()== p) {
                  this.leftRotate(p);
                  this.rightRotate(g);
                }
                else if(n.getParent().getLeft() == n && p.getParent().getRight() == p) {
                  this.rightRotate(p);
                  this.leftRotate(g);
                }
            }
        }
    }
    /**
     * Agrega un nodo al arbol splay 
     * @param data numero asociado al nodo
     */
    @Override
    public void append(int data) {
        Node y = null;
        Node temp = this.root;
        while(temp != null) {
          y = temp;
          if(data < temp.getData())
            temp = temp.getLeft();
          else
            temp = temp.getRight();
        }
        Node n = new Node(data);
        n.setParent(y);
        
        if(y == null) //newly added node is root
          this.root = new Node(data);
        else if(data < y.getData())
          y.setLeft(n);
        else
          y.setRight(n);

        this.splay(n);
    }
    /**
     * Agrega un nodo al arbol
     * @param data numero asociado al nodo
     * @param current nodo actual
     * @return null
     */
    @Override
    protected Node append(int data, Node current) {
        return null;
    }
    /**
     * Devuleve la representación del árbol splay
     * @return String que representa el arbol
     */
    public String getTree(){
        return super.getTree(this.root);
    }
}
