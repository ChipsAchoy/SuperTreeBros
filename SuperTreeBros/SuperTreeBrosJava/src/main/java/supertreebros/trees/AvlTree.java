package supertreebros.trees;

/**
 * Árbol Avl, proveniente del template method de árbol binario
 * @author Anthony Chaves
 */
public class AvlTree extends BinaryTree{
    /**
     * Actualiza la altura de un nodo
     * @param n Nodo al cual se le actualiza la altura
     */
    private void updateHeight(Node n) {
        n.setHeight(1 + Math.max(height(n.getLeft()), height(n.getRight())));
    }
    /**
     * Devuelve la altura del nodo
     * @param n Nodo del cual se quiere saber la altura
     * @return -1 en caso de ser nulo, de lo contrario, la altura del árbol
     */
    private int height(Node n) {
        return n == null ? -1 : n.getHeight();
    }
    /**
     * Calcula el factor de balance de un nodo según la altura de sus subárboles
     * @param n Nodo al que se le calcula el factor
     * @return El factor de balance del nodo
     */
    private int getBalance(Node n) {
        return (n == null) ? 0 : height(n.getRight()) - height(n.getLeft());
    }
    /**
     * Override del metodo recursivo de agregar nodos para el caso particular del AVL
     * @param data dato del nuevo nodo
     * @param current nodo que se está revisando
     * @return el nuevo nodo del árbol
     */
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
    /**
     * Rota el árbol hacia la derecha (single rotation)
     * @param y nodo que se desea rotar
     * @return el nodo que queda en esa posición
     */
    private Node rotateRight(Node y) {
        Node x = y.getLeft();
        Node z = x.getRight();
        x.setRight(y);
        y.setLeft(z);
        updateHeight(y);
        updateHeight(x);
        return x;
    }
    /**
     * Rota el árbol hacia la izquierda (single rotation)
     * @param y nodo que se desea rotar
     * @return el nodo que queda en esa posición
     */
    private Node rotateLeft(Node y) {
        Node x = y.getRight();
        Node z = x.getLeft();
        x.setLeft(y);
        y.setRight(z);
        updateHeight(y);
        updateHeight(x);
        return x;
    }
    /**
     * Rebalancea el nodo con base en su factor de balance
     * @param z Nodo que puede rebalancearse
     * @return devuelve el nodo con sus respectivas rotaciones
     */
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
    /**
     * Agrega un nodo al árbol (caso particular para el Avl)
     * @param data dato del nodo
     */
    @Override
    public void append(int data) {
        this.root = this.append(data, this.root);
    }
    /**
     * Devulve la representación del árbol
     * @return String que representa el árbol
     */
    public String getTree(){
        return super.getTree(this.root);
    }
    
}
