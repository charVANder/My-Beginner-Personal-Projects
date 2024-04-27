# Doubly Linked List'
*2/23/2024*<br>

This project involved creating a Python class DLList for a doubly-linked list data structure similar to what was implemented [here](https://observablehq.com/@mbostock/linked-lists#cell-214). A tutorial on how to use it is included with the demo code.

## Dependencies
* Python 3

## Instructions for Use
### *How to use DLList and Running the Demo Code*
#### <u>*What is DLList?*</u>
`DLList` stands for *doubly-linked list*. A doubly linked list is a linked data structure that contains of a set of linked records called nodes. Each node contains three parts--The data, and two pointers/references to the other nodes(the previous and next nodes in the sequence).

#### <u>*Using the Demo Code*</u>
If you go into the `src` directory, you will find a script called `demo_code.py` which includes examples on using `class DLList` to create your own doubly-linked list objects. Running this code will should display the following instructions:
1. **How to Create Nodes and DLList Objects**
    * To create your nodes, you can use the notation:
        ```
        node1 = DLList.Node('A')
        node2 = DLList.Node('B')
        node3 = DLList.Node('C')
        ```
        This example will create 3 nodes.
    * Next, to create your DLList with those nodes, you use the `of()` method. For example, to create a DLList of the previous 3 nodes, enter:
        ```
        lst = DLList.of(node1, node2, node3)
        print(">>>Initial DLList:", lst)
        ```
        This creates a doubly-linked list containing node1, node2, and node3 with an expected output of `A B C`
2. **How to Insert New Nodes into your DLList**
    * To insert new nodes into your doubly-linked list, you can use the `insert()` method. Remember to specify the location of where you're inserting.
    * For example, if you wanted to insert a new node into location 2, you would enter:
        ```
        new_node = DLList.Node('D')
        lst.insert(new_node, location=node2)
        print(">>>DLList after insertion:", lst)
        ```
        After insertion, your new DLList would go from `A B C` to `A D B C`
3. **How to Remove a Node from your DLList**
    * To remove nodes from your doubly-linked list, you can use the `remove()` method and enter the node to be removed as an argument. For example, if you wanted to remove the first node from your DLList, you would enter:
        ```
        lst.remove(node1)
        print(">>>DLList after removal:", lst)
        ```
        After removing `node1`, your DLList would go from `A D B C` to `D B C`
4. **Displaying your DLList as a Python List**
    * If at any point you would like to view your DLList as a Python list of node values, you can use the additional `make_list()` method.
    * For example, if you would like to convert the previous DLList as a Python list, just enter:
        ```
        python_list = lst.make_list()
        print(">>>DLList converted to a Python list:", python_list)
        ```
        Doing so will should an output of `['D', 'B', 'C']`

Doubly-linked lists can be useful whenever you need to efficiently insert/delete items from both ends of a list, or when you need to traverse the list from both  directions. However, keep in mind that they also require more memory per item compared to singly linked lists due to the additional previous node pointer!

## References/Acknowledgements
**Documentation Sources:**
* Python
  * https://www.python.org/downloads/
* GNU make
  * https://www.gnu.org/software/make/manual/make.html

**Online Sources:**
* Doubly-linked list example - https://observablehq.com/@mbostock/linked-lists#cell-214
* Tutorial on Unit tests - https://www.youtube.com/watch?v=6tNS--WetLI
* Tutorial on linked list structures - https://www.youtube.com/watch?v=N6dOwBde7-M

**Class Sources:**
* git-intro: http://github.com/ds5110/git-intro
* unittest.md: https://github.com/ds5010/spring-2024/blob/main/unittest.md