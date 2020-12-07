package supertreebros.trees;

/**
 * Árbol Bst, proveniente del template method de árbol binario
 * @author Anthony Chaves
 */
public class BstTree extends BinaryTree{
    
    /**
     * Agrega un nodo al árbol bst
     * @param data numero que se agrega
     */
    @Override
    public void append(int data){
        this.root = this.append(data, this.root);
    }
    
    /**
     * Método recursivo para agregar un nodo al árbol bst
     * @param data numero asociado al nodo
     * @param current referencia al nodo actuañ
     * @return el nodo agregado
     */
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
    /**
     * Devuelve la representación del arbol bst
     * @return representación en sting del árbol
     */
    public String getTree(){
        return super.getTree(this.root);
    }
    
}
