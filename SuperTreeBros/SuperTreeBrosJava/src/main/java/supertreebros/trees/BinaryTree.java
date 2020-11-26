package supertreebros.trees;

import java.lang.Math;
/**
 *
 * @author Anthony Chaves
 */
public abstract class BinaryTree {
    protected Node root = null;
    protected int depth = 0;
    protected int elements = 0;
    public abstract void append(int data);
    protected abstract Node append(int data, Node current);

    public void printTree(Node initial){
        String unit = "   ";
        String space = "";
        System.out.println(this.depth);
        for (int i=0; i<this.depth; i++){
            space += unit;
        }
        String result = this.printTree(initial, "", "", space, 1,2,1);
        System.out.println(result);
    }
    
    protected String printTree(Node current, String out, String slashesS, String space, int elems, int slashes ,int currentelems){
        System.out.println("elems"+currentelems);
        currentelems -= 1;
        System.out.println("elemsf"+currentelems);
        if (current == null){
            return "   ";
        }
        else{
            out += space + "("+Integer.toString(current.getData())+")";
            
            if (currentelems == 0){
                currentelems = (int)Math.pow((double)2, (double)elems);
                elems += 1;
            }
            
            boolean sonR = false, sonL = false;
            
            if (current.getLeft() != null){
                slashes--;
                sonL = true;
                slashesS += space+"/ ";
            }else{
                slashes--;
                slashesS += space+"   ";
            }
            if (current.getRight() != null){
                slashes--;
                sonR = true;
                slashesS += "\\";
            }else{
                slashes--;
                slashesS += space+"   ";
            }
            System.out.println("slashes"+slashes);
            if (slashes == 0){
                slashes = (int)Math.pow((double)2, (double)elems);
                System.out.println("slashes"+slashes);
                slashesS += "\n";
                out += "\n"+slashesS;
                slashesS = "";
            }
            
            if (sonL){
                out += this.printTree(current.getLeft(), "",slashesS ,space.substring(3), elems, slashes,currentelems);
            }
            if (sonR){
                out += this.printTree(current.getRight(), "", slashesS, "   ", elems, slashes, currentelems);
            }
        }
        return out;
    }
}
