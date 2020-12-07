package supertreebros.trees;

/**
 * Nodo de los árboles binarios
 * @author Anthony Chaves
 */
public class Node {
    private int data;
    private int height;
    private Node right = null, left = null, parent = null;
    /**
     * Constructor de la clase
     * @param data 
     */
    public Node(int data){
        this.data = data;
    }
    /**
     * Setea el nodo derecho del árbol 
     * @param right nodo derecho
     */
    public void setRight(Node right){
        this.right = right;
    }
    /**
     * Setea el nodo izquierdo del árbol 
     * @param right nodo izquierdo
     */
    public void setLeft(Node left){
        this.left = left;
    }
    /**
     * Devuelve el nodo derecho
     * @return referencia al nodo derecho
     */
    public Node getRight(){
        return this.right;
    }
    /**
     * Devuelve el nodo izquierdo
     * @return referencia al nodo izquierdo
     */
    public Node getLeft(){
        return this.left;
    }
    /**
     * Devuelve el dato en ese nodo
     * @return el numero asociado al nodo
     */
    public int getData(){
        return this.data;
    }
    /**
     * Setea la altura del nodo
     * @param h altura del nodo
     */
    public void setHeight(int h){
        this.height = h;
    }
    /**
     * Devuelve la altura del nodo
     * @return numero asociado a la altura
     */
    public int getHeight(){
        return this.height;
    }
    /**
     * Devuelve el nodo padre del nodo actual
     * @return referencia al nodo padre
     */
    public Node getParent(){
        return this.parent;
    }
    /**
     * Setea el nodo padre del nodo actual
     * @param par padre del nodo actual
     */
    public void setParent(Node par){
        this.parent = par;
    }
}
