package supertreebros.trees;

/**
 * Clase para construir arboles B
 * @author Jan Marschatz
 */
public class Btree {
    public int m = 4;
    public BNode root = new BNode(m);
    private String tree_out = "";
    
    /**
     * Constructor de la clase
     * @param m grado del arbol
     */
    public Btree(int m) {
        this.m = m;
    }
    
    /**
     * Realiza un split a la raiz del arbol
     * @param ptr Nodo al que se le realiza el split
     */
    public void split_root(BNode ptr){
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
        i++;
        int j = 0;
        while (i < ptr.count){
            child1.children[j] = ptr.children[i];
            child1.data[j] = ptr.data[i];
            child1.count++;
            j++;
            i++;
        }
        child1.children[j] = ptr.children[i];

        ptr.data[0] = ptr.data[mid];
        ptr.children[0] = child0;
        ptr.children[1] = child1;
        ptr.count = 1;
    }
    /**
     * Metodo recursivo para hacer print al arbol
     * @param ptr nodo actual
     * @param level Nivel actual del nodo
     */
    public void print_rec(BNode ptr, int level){
        if(ptr != null){
            int i = ptr.count-1;
            while (i >= 0){
                print_rec(ptr.children[i+1], level+1);
                for (int j = 0; j < level; j++){
                    System.out.print("   ");
                    this.tree_out += "   ";
                }
                System.out.println(ptr.data[i]);
                this.tree_out += Integer.toString(ptr.data[i]) + "\n";
                i--;
            }
            print_rec(ptr.children[0], level+1);
        }
    }
    
    /**
     * Inserta un nodo nuevo al arbol
     * @param value valor asociado al nodo
     */
    public void insert(int value){
        int state = this.root.insert(value);
        if(state == -1){
            split_root(this.root);
        }
    }
    /**
     * Retorna y muestra una representacion del arbol en string
     * @return String que representa al arbol
     */
    public String getTree(){
        this.tree_out = "";
        System.out.println("******************");
        print_rec(this.root, 0);
        System.out.println("******************");
        return this.tree_out;
    }
}

