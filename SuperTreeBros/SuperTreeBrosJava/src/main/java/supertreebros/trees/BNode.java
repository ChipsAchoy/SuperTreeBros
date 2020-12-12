/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package supertreebros.trees;

/**
 * Nodo para el arbol B
 * @author Jan Marschatz
 */
public class BNode {

    public int [] data = new int[8];
    public BNode [] children = new BNode[8];
    public int count = 0;
    public int m;
    
    /**
     * Constructor de la clase
     * @param m grado del arbol
     */
    public BNode(int m) {
        this.m = m;
    }
    
    /**
     * Metodo para agregar nodos al arbol
     * @param value valor asociado al nodo
     * @return 1 o -1 segun si se debe realizar split al arbol
     */
    public int insert(int value){
        int index = 0;
        while(index < this.count && this.data[index] < value){
            index++;
        }
        if(this.children[index] == null){
            insert_into(value, index);
        }else{
            int state = this.children[index].insert(value);
            if(state == -1){
                split_branch(index);
            }
        }
        if(this.count > this.m){
            return -1;
        }else{
            return 1;
        }
    }
    
    /**
     * Inserta un nodo en un posicion especifica (metodo necesario para hacer split)
     * @param value valor asociado al nodo
     * @param index posicion donde se inserta el nodo
     */
    public void insert_into(int value, int index){
        int j = this.count;
        while (j > index){
            this.data[j] = this.data[j-1];
            this.children[j+1] = this.children[j];
            j--;
        }
        data[index] = value;
        this.children[index+1] = this.children[index];
        this.count++;
    }
    
    /**
     * Realiza split a una pagina si se encuentra llena
     * @param index posicion donde se realiza el split
     */
    public void split_branch(int index){
        BNode ptr = this.children[index];
        BNode child0 = new BNode(ptr.m);
        BNode child1 = new BNode(ptr.m);
        int i = 0;
        while (i < Math.floor(ptr.m/2)){
            child0.children[i] = ptr.children[i];
            child0.data[i] = ptr.data[i];
            child0.count++;
            i++;
        }
        child0.children[i] = ptr.children[i];
        int mid = i;
        i++; //SKIP
        int j = 0;
        while (i < ptr.count){
            child1.children[j] = ptr.children[i];
            child1.data[j] = ptr.data[i];
            child1.count++;
            j++;
            i++;
        }
        child1.children[j] = ptr.children[i];

        this.insert_into(ptr.data[mid], index);
        this.children[index] = child0;
        this.children[index+1] = child1;
    }
}
