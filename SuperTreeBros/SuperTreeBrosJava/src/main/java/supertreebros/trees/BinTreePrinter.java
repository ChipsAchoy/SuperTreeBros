package supertreebros.trees;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;

/**
 *
 * @author A
 */
class BinTreePrinter {
    private static String result = "";
    public static String printGetTree(Node root) {
        int maxLevel = BinTreePrinter.maxLevel(root);
        result = "";
        printNodeInternal(Collections.singletonList(root), 1, maxLevel);
        return result;
    }
    

    private static void printNodeInternal(List<Node> nodes, int level, int maxLevel) {
        if (nodes.isEmpty() || BinTreePrinter.isAllElementsNull(nodes))
            return;

        int floor = maxLevel - level;
        int endgeLines = (int) Math.pow(2, (Math.max(floor - 1, 0)));
        int firstSpaces = (int) Math.pow(2, (floor)) - 1;
        int betweenSpaces = (int) Math.pow(2, (floor + 1)) - 1;

        BinTreePrinter.printWhitespaces(firstSpaces);

        List<Node> newNodes = new ArrayList<Node>();
        for (Node node : nodes) {
            if (node != null) {
                System.out.print(node.getData());
                result += node.getData();
                newNodes.add(node.getLeft());
                newNodes.add(node.getRight());
            } else {
                newNodes.add(null);
                newNodes.add(null);
                System.out.print(" ");
                result += " ";
            }

            BinTreePrinter.printWhitespaces(betweenSpaces);
        }
        System.out.println("");
        result += "\n";

        for (int i = 1; i <= endgeLines; i++) {
            for (int j = 0; j < nodes.size(); j++) {
                BinTreePrinter.printWhitespaces(firstSpaces - i);
                if (nodes.get(j) == null) {
                    BinTreePrinter.printWhitespaces(endgeLines + endgeLines + i + 1);
                    continue;
                }

                if (nodes.get(j).getLeft() != null){
                    System.out.print("/");
                    result += "/";
                }
                else
                    BinTreePrinter.printWhitespaces(1);

                BinTreePrinter.printWhitespaces(i + i - 1);

                if (nodes.get(j).getRight() != null){
                    System.out.print("\\");
                    result += "\\";
                }
                else
                    BinTreePrinter.printWhitespaces(1);

                BinTreePrinter.printWhitespaces(endgeLines + endgeLines - i);
            }

            System.out.println("");
            result += "\n";
        }

        printNodeInternal(newNodes, level + 1, maxLevel);
    }

    private static void printWhitespaces(int count) {
        for (int i = 0; i < count; i++){
            System.out.print(" ");
            result += " ";
        }
    }

    private static int maxLevel(Node node) {
        if (node == null)
            return 0;
        return Math.max(BinTreePrinter.maxLevel(node.getLeft()), BinTreePrinter.maxLevel(node.getRight())) + 1;
    }

    private static <T> boolean isAllElementsNull(List<T> list) {
        for (Object object : list) {
            if (object != null)
                return false;
        }
        return true;
    }

}
