package supertreebros;

import supertreebros.trees.AvlTree;
import supertreebros.trees.BTree;
import supertreebros.trees.BstTree;
import supertreebros.trees.SplayTree;

/**
 * Clase encargada de manejar los eventos, crear árboles, nodos entre otros
 * @author Anthony Chaves
 */
public class EventHandler {
    public String type;
    public int elems;
    public int level1 = 0, level2 = 0;
    public boolean won1 = false, won2 = false;
    private boolean current;
    public BstTree p1BstTree,p2BstTree;
    public AvlTree p1AvlTree,p2AvlTree;
    public SplayTree p1SpTree,p2SpTree;
    public BTree<Integer, Integer> p1BTree, p2BTree;
    private static EventHandler instance = null;
    
    /**
     * Concstructor de la clase event handler
     * @param type tipo de arbol que sera manejado
     * @param elems cantidad de elementos
     */
    private EventHandler(String type, int elems){
        this.elems = elems;
        this.type = type;
        this.defineType(); 
    }
    
    /**
     * Método estatico para obtener la instancia
     * @param type tipo de arbol que sera manejado
     * @param elems  cantidad de elementos del arbol
     * @return instacia de la clase
     */
    public static EventHandler getInstace(String type, int elems){
        if (instance == null){
            instance = new EventHandler(type, elems);
            instance.won1 = false;
            instance.won2 = false;
        }
            
        else{
            instance.elems = elems;
            instance.type = type;
            instance.won1 = false;
            instance.won2 = false;
            instance.level1 = 0;
            instance.level2 = 0;
            instance.defineType();
        }
        return instance;
    }
    
    /**
     * Método estatico para obtener la instancia
     * @return la instancia de la clase (incluso si es null)
     */
    public static EventHandler getInstance(){
        return instance;
    }
    /**
     * Define el tipo de árbol y declara uno para cada jugador
     */
    public void defineType(){
        if (this.type.equals("bst")){
            this.p1BstTree = new BstTree();
            this.p2BstTree = new BstTree();
        }else if (this.type.equals("avl")){
            this.p1AvlTree = new AvlTree();
            this.p2AvlTree = new AvlTree();
        }else if (this.type.equals("spl")){
            this.p1SpTree = new SplayTree();
            this.p2SpTree = new SplayTree();
        }else if (this.type.equals("btr")){
            this.p1BTree = new BTree<Integer, Integer>();
            this.p2BTree = new BTree<Integer, Integer>();
        }else{
            System.out.println("No se recibio un arbol correcto");
        }
    }
    /**
     * Parsea el string entrante y obtiene los nuevos nodos
     * @param added String recibido por los sockets
     */
    public void parseNodes(String added){
        System.out.println(this.type);
        this.current = false;
        System.out.println(added.substring(0, 7));
        if (added.substring(0, 7).equals("player1"))
            this.current = true;
        else if (added.substring(0, 7).equals("player2"))
            this.current = false;
        else
            System.out.println("");
        if (added.substring(8, 9).equals("r")&&this.current){
            this.level1 = 0;
            this.p1BstTree = new BstTree();
            this.p1AvlTree = new AvlTree();
            this.p1SpTree = new SplayTree();
            this.p1BTree = new BTree<Integer, Integer>();
        }else if (added.substring(8, 9).equals("r")&&!this.current){
            this.level2 = 0;
            this.p2BstTree = new BstTree();
            this.p2AvlTree = new AvlTree();
            this.p2SpTree = new SplayTree();
            this.p2BTree = new BTree<Integer, Integer>();
        }
        else{
            String nodeS = "";
            int node;
            for (int i=9; i<9+added.substring(9).length(); i++){
                if (!added.substring(i, i+1).equals(",")){
                    //System.out.println(added.substring(i, i+1));
                    nodeS += added.substring(i, i+1);
                }else{
                    node = Integer.parseInt(nodeS);
                    if (this.type.equals("bst")&&this.current)
                        this.p1BstTree.append(node);
                    else if(this.type.equals("bst")&&!this.current)
                        this.p2BstTree.append(node);
                    else if (this.type.equals("avl")&&this.current)
                        this.p1AvlTree.append(node);
                    else if(this.type.equals("avl")&&!this.current)
                        this.p2AvlTree.append(node);
                    else if (this.type.equals("spl")&&this.current)
                        this.p1SpTree.append(node);
                    else if(this.type.equals("spl")&&!this.current)
                        this.p2SpTree.append(node);
                    else if (this.type.equals("btr")&&this.current)
                        this.p1BTree.put(node, node);
                    else if(this.type.equals("btr")&&!this.current)
                        this.p2BTree.put(node, node);
                    if (this.current)
                        this.level1++;
                    else
                        this.level2++;
                    nodeS = "";
                }
            }
        }
    }
    /**
     * Obtiene el string que representa el árbol actual y lo devuelve
     * @return representación del árbol en caracteres
     */
    public String getCurrentTree(){
        String output1 = "", output2 = "";
        if (this.current && this.level1 < this.elems){
            output1 = "player1:\n";
            if (this.type.equals("bst"))
                output1 += this.p1BstTree.getTree();
            else if(this.type.equals("avl"))
                output1 += this.p1AvlTree.getTree();
            else if(this.type.equals("spl"))
                output1 += this.p1SpTree.getTree();
            else if(this.type.equals("btr"))
                output1 += this.p1BTree.toString();
        }
        if (this.current&&this.level1 >= this.elems){
            //output1 = "player1:f";
            System.out.println("Player 1 won");
            this.won1 = true;
        }
        
        if (!this.current && this.level2 < this.elems){
             output2 = "player2:\n";
            if (this.type.equals("bst"))
                output2 += this.p2BstTree.getTree();
            else if(this.type.equals("avl"))
                output2 += this.p2AvlTree.getTree();
            else if(this.type.equals("spl"))
                output2 += this.p2SpTree.getTree();
            else if(this.type.equals("btr"))
                output2 += this.p2BTree.toString();
        }
        if (!this.current&&this.level2 >= this.elems){
            System.out.println("Player 2 won");
            this.won2 = true;
        }
        
        if (this.current){
            return output1;
        }
        else
            return output2;
    }
}
