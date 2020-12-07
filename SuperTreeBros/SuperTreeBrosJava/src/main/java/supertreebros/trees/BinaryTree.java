package supertreebros.trees;

import java.lang.Math;
/**
 * Clase abstract de árbol binario, funciona como template method
 * @author Anthony Chaves
 */
public abstract class BinaryTree {
    protected Node root = null;
    /**
     * Método abstracto para agregar nodos al árbol
     * @param data numero que se agrega
     */
    public abstract void append(int data);
    /**
     * Método recursivo para agregar nodos al árbol
     * @param data numero que se agrega
     * @param current nodo actual
     * @return 
     */
    protected abstract Node append(int data, Node current);
    /**
     * Método para obtener un string del árbol
     * @param initial nodo inicial desde el que se genera el string
     * @return el string que representa el árbol
     */
    protected String getTree(Node initial){
        String output = "";
        if (this.root != null)
            output = BinTreePrinter.printGetTree(this.root);
        return output;
        
    }
    
}
