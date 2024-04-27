'''
Evangeline Kim
February 23rd, 2024
DS5010: Demo code script
'''
# Necessary Imports
from dllist import DLList

# Creating nodes
print(f"\nCREATING NODES:")
print(f"• To create your nodes, you can use the notation...\nnode1 = DLList.Node('A')\nnode2 = DLList.Node('B')\nnode3 = DLList.Node('C')")
node1 = DLList.Node('A')
node2 = DLList.Node('B')
node3 = DLList.Node('C')

# Creating a DLList with the nodes
print(f"\nCREATING DLLIST WITH THE NODES USING OF():")
print(f"• To create your DLList, use the notation 'lst = DLList.of(node1, node2, node3)'")
lst = DLList.of(node1, node2, node3)
print(">>>Initial DLList:", lst) # Showing the initial DLList

# Inserting a new node after node2 using the insert() method.
print(f"\nINSERTING A NEW NODE USING THE INSERT() METHOD:")
print(f"• Make sure to specify the location to be inserted!")
print(f"• For example, to insert a new node (DLList.Node('D)) into location 2, use the notation 'lst.insert(new_node, location=node2)'")
new_node = DLList.Node('D')
lst.insert(new_node, location=node2)
print(">>>DLList after insertion:", lst) # Showing DLList after insertion

# Removing node2 from the list
print(f"\nREMOVING A NODE USING THE REMOVE() METHOD:")
print(f"• For example, to remove node1 use the notation 'lst.remove(node1)'")
lst.remove(node1)
print(">>>DLList after removal:", lst) # Showing DLList after removal

# Converting the list to a Python list using make_list()
print(f"\nDISPLAY DLLIST AS A PYTHON LIST USING THE MAKE_LIST() METHOD:")
print(f"• For example, you can display your DLList as a python list by using the notation 'lst.make_list()'")
python_list = lst.make_list()
print(">>>DLList converted to a Python list:", python_list)