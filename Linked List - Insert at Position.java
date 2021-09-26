import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class SinglyLinkedListNode {
    public int data;
    public SinglyLinkedListNode next;

    public SinglyLinkedListNode(int nodeData) {
        this.data = nodeData;
        this.next = null;
    }
}

class SinglyLinkedList {
    public SinglyLinkedListNode head;
    public SinglyLinkedListNode tail;

    public SinglyLinkedList() {
        this.head = null;
        this.tail = null;
    }

    public void insertNode(int nodeData) {
        SinglyLinkedListNode node = new SinglyLinkedListNode(nodeData);

        if (this.head == null) {
            this.head = node;
        } else {
            this.tail.next = node;
        }

        this.tail = node;
    }
}

class SinglyLinkedListPrintHelper {
    public static void printList(SinglyLinkedListNode node, String sep, BufferedWriter bufferedWriter) throws IOException {
        while (node != null) {
            bufferedWriter.write(String.valueOf(node.data));

            node = node.next;

            if (node != null) {
                bufferedWriter.write(sep);
            }
        }
    }
}

class Result {

    /*
     * Complete the 'insert_at_position' function below.
     *
     * The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
     * The function accepts following parameters:
     *  1. INTEGER_SINGLY_LINKED_LIST head
     *  2. INTEGER val
     *  3. INTEGER pos
     */

    /*
     * For your reference:
     *
     * SinglyLinkedListNode {
     *     int data;
     *     SinglyLinkedListNode next;
     * }
     *
     */

    public static SinglyLinkedListNode insert_at_position(SinglyLinkedListNode head, int val, int pos) {
    // Write your code here
        SinglyLinkedListNode node = new SinglyLinkedListNode(val);
         SinglyLinkedListNode temp = head;
 
         if(head == null){
             return node;
         }
        int i=0;
        while(i < pos-1) {
            temp = temp.next;
            i++;
        }
        node.next = temp.next;
        temp.next = node;
        return head;

    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        SinglyLinkedList input_sll = new SinglyLinkedList();

        int input_sllCount = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, input_sllCount).forEach(i -> {
            try {
                int input_sllItem = Integer.parseInt(bufferedReader.readLine().trim());

                input_sll.insertNode(input_sllItem);
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        int input_value_for_insertion = Integer.parseInt(bufferedReader.readLine().trim());

        int input_position_for_insertion = Integer.parseInt(bufferedReader.readLine().trim());

        SinglyLinkedListNode inserted_head = Result.insert_at_position(input_sll.head, input_value_for_insertion, input_position_for_insertion);

        SinglyLinkedListPrintHelper.printList(inserted_head, ",", bufferedWriter);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}