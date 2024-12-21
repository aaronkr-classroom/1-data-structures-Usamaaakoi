# -*- coding: utf-8 -*-
"""bst 4 copy py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12nAIeWtIazyy68ON7B-lerRUL3W8QfZ2
"""

{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "# Binary Search Trees (BST)"
      ],
      "metadata": {
        "id": "d4USoBYZIbMc"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "b6Xnq4-nIVMA"
      },
      "outputs": [],
      "source": [
        "class TreeNode:\n",
        "    def __init__(self, value):\n",
        "        self.value = value\n",
        "        self.left = None\n",
        "        self.right = None\n",
        "        self.parent = None\n",
        "\n",
        "class BinarySearchTree:\n",
        "    def __init__(self):\n",
        "        self.root = None\n",
        "\n",
        "    def find_value(self, current, target):\n",
        "        if current is None:\n",
        "            return None\n",
        "        if current.value == target:\n",
        "            return current\n",
        "        if target < current.value:\n",
        "            return self.find_value(current.left, target)\n",
        "        else:\n",
        "            return self.find_value(current.right, target)\n",
        "\n",
        "    def find_value_itr(self, root, target):\n",
        "        current = root\n",
        "        while current is not None and current.value != target:\n",
        "            if target < current.value:\n",
        "                current = current.left\n",
        "            else:\n",
        "                current = current.right\n",
        "        return current\n",
        "\n",
        "    def find_tree_node(self, target):\n",
        "        if self.root is None:\n",
        "            return None\n",
        "        return self.find_value(self.root, target)\n",
        "\n",
        "    def insert_tree_node(self, new_value):\n",
        "        if self.root is None:\n",
        "            self.root = TreeNode(new_value)\n",
        "        else:\n",
        "            self.insert_node(self.root, new_value)\n",
        "\n",
        "    def insert_node(self, current, new_value):\n",
        "        if new_value == current.value:\n",
        "            return  # Skip inserting duplicates\n",
        "        if new_value < current.value:\n",
        "            if current.left is not None:\n",
        "                self.insert_node(current.left, new_value)\n",
        "            else:\n",
        "                current.left = TreeNode(new_value)\n",
        "                current.left.parent = current\n",
        "        else:\n",
        "            if current.right is not None:\n",
        "                self.insert_node(current.right, new_value)\n",
        "            else:\n",
        "                current.right = TreeNode(new_value)\n",
        "                current.right.parent = current\n",
        "\n",
        "    def remove_tree_node(self, node):\n",
        "        #...\n",
        "\n",
        "    def get_min_value_node(self, node):\n",
        "        current = node\n",
        "        while current.left is not None:\n",
        "            current = current.left\n",
        "        return current\n",
        "\n",
        "    def remove_value(self, target):\n",
        "        node = self.find_tree_node(target)\n",
        "        self.remove_tree_node(node)\n",
        "\n",
        "    def print_tree(self):\n",
        "        # ..."
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Inserting and Printing Tree"
      ],
      "metadata": {
        "id": "GdGqa1nuIiYa"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def print_tree(self):\n",
        "    def in_order_traversal(node):\n",
        "        if node is not None:\n",
        "            in_order_traversal(node.left)\n",
        "            print(node.value, end=\" \")\n",
        "            in_order_traversal(node.right)\n",
        "    in_order_traversal(self.root)\n",
        "    print()  # To add a newline after printing all values\n",
        "def remove_tree_node(self, node):\n",
        "    if node is None:\n",
        "        return\n",
        "\n",
        "    # Case 1: Node has no children\n",
        "    if node.left is None and node.right is None:\n",
        "        if node.parent is None:  # The node is the root\n",
        "            self.root = None\n",
        "        elif node == node.parent.left:\n",
        "            node.parent.left = None\n",
        "        else:\n",
        "            node.parent.right = None\n",
        "\n",
        "    # Case 2: Node has one child\n",
        "    elif node.left is None or node.right is None:\n",
        "        child = node.left if node.left is not None else node.right\n",
        "        if node.parent is None:  # The node is the root\n",
        "            self.root = child\n",
        "        elif node == node.parent.left:\n",
        "            node.parent.left = child\n",
        "        else:\n",
        "            node.parent.right = child\n",
        "        child.parent = node.parent\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "hlS-QXA8OEao"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Searching for Values"
      ],
      "metadata": {
        "id": "BsRYD_sZIoRB"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class TreeNode:\n",
        "    def __init__(self, value):\n",
        "        self.value = value\n",
        "        self.left = None\n",
        "        self.right = None\n",
        "        self.parent = None\n",
        "\n",
        "class BinarySearchTree:\n",
        "    def __init__(self):\n",
        "        self.root = None\n",
        "\n",
        "    def find_value(self, current, target):\n",
        "        if current is None:\n",
        "            return None\n",
        "        if current.value == target:\n",
        "            return current\n",
        "        if target < current.value:\n",
        "            return self.find_value(current.left, target)\n",
        "        else:\n",
        "            return self.find_value(current.right, target)\n",
        "\n",
        "    def find_value_itr(self, root, target):\n",
        "        current = root\n",
        "        while current is not None and current.value != target:\n",
        "            if target < current.value:\n",
        "                current = current.left\n",
        "            else:\n",
        "                current = current.right\n",
        "        return current\n",
        "\n",
        "    def find_tree_node(self, target):\n",
        "        if self.root is None:\n",
        "            return None\n",
        "        return self.find_value(self.root, target)\n",
        "\n",
        "    def insert_tree_node(self, new_value):\n",
        "        if self.root is None:\n",
        "            self.root = TreeNode(new_value)\n",
        "        else:\n",
        "            self.insert_node(self.root, new_value)\n",
        "\n",
        "    def insert_node(self, current, new_value):\n",
        "        if new_value == current.value:\n",
        "            return  # Skip inserting duplicates\n",
        "        if new_value < current.value:\n",
        "            if current.left is not None:\n",
        "                self.insert_node(current.left, new_value)\n",
        "            else:\n",
        "                current.left = TreeNode(new_value)\n",
        "                current.left.parent = current\n",
        "        else:\n",
        "            if current.right is not None:\n",
        "                self.insert_node(current.right, new_value)\n",
        "            else:\n",
        "                current.right = TreeNode(new_value)\n",
        "                current.right.parent = current\n",
        "\n",
        "    def remove_tree_node(self, node):\n",
        "        if node is None:\n",
        "            return\n",
        "\n",
        "        # Node with only one child or no child\n",
        "        if node.left is None:\n",
        "            self.transplant(node, node.right)\n",
        "        elif node.right is None:\n",
        "            self.transplant(node, node.left)\n",
        "        else:\n",
        "            # Node with two children: get the inorder successor\n",
        "            successor = self.get_min_value_node(node.right)\n",
        "            if successor.parent != node:\n",
        "                self.transplant(successor, successor.right)\n",
        "                successor.right = node.right\n",
        "                successor.right.parent = successor\n",
        "            self.transplant(node, successor)\n",
        "            successor.left = node.left\n",
        "            successor.left.parent = successor\n",
        "\n",
        "    def transplant(self, old_node, new_node):\n",
        "        if old_node.parent is None:\n",
        "            self.root = new_node\n",
        "        elif old_node == old_node.parent.left:\n",
        "            old_node.parent.left = new_node\n",
        "        else:\n",
        "            old_node.parent.right = new_node\n",
        "        if new_node is not None:\n",
        "            new_node.parent = old_node.parent\n",
        "\n",
        "    def get_min_value_node(self, node):\n",
        "        current = node\n",
        "        while current.left is not None:\n",
        "            current = current.left\n",
        "        return current\n",
        "\n",
        "    def remove_value(self, target):\n",
        "        node = self.find_tree_node(target)\n",
        "        self.remove_tree_node(node)\n",
        "\n",
        "    def print_tree(self):\n",
        "        def in_order_traversal(node):\n",
        "            if node is not None:\n",
        "                in_order_traversal(node.left)\n",
        "                print(node.value, end=\" \")\n",
        "                in_order_traversal(node.right)\n",
        "\n",
        "        in_order_traversal(self.root)\n",
        "        print()\n"
      ],
      "metadata": {
        "id": "w2t7Z1cAO1uM"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Removing Nodes"
      ],
      "metadata": {
        "id": "4gfBL-_IIth5"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class TreeNode:\n",
        "    def __init__(self, value):\n",
        "        self.value = value\n",
        "        self.left = None\n",
        "        self.right = None\n",
        "        self.parent = None\n",
        "\n",
        "class BinarySearchTree:\n",
        "    def __init__(self):\n",
        "        self.root = None\n",
        "\n",
        "    def find_value(self, current, target):\n",
        "        if current is None:\n",
        "            return None\n",
        "        if current.value == target:\n",
        "            return current\n",
        "        if target < current.value:\n",
        "            return self.find_value(current.left, target)\n",
        "        else:\n",
        "            return self.find_value(current.right, target)\n",
        "\n",
        "    def find_value_itr(self, root, target):\n",
        "        current = root\n",
        "        while current is not None and current.value != target:\n",
        "            if target < current.value:\n",
        "                current = current.left\n",
        "            else:\n",
        "                current = current.right\n",
        "        return current\n",
        "\n",
        "    def find_tree_node(self, target):\n",
        "        if self.root is None:\n",
        "            return None\n",
        "        return self.find_value(self.root, target)\n",
        "\n",
        "    def insert_tree_node(self, new_value):\n",
        "        if self.root is None:\n",
        "            self.root = TreeNode(new_value)\n",
        "        else:\n",
        "            self.insert_node(self.root, new_value)\n",
        "\n",
        "    def insert_node(self, current, new_value):\n",
        "        if new_value == current.value:\n",
        "            return  # Skip inserting duplicates\n",
        "        if new_value < current.value:\n",
        "            if current.left is not None:\n",
        "                self.insert_node(current.left, new_value)\n",
        "            else:\n",
        "                current.left = TreeNode(new_value)\n",
        "                current.left.parent = current\n",
        "        else:\n",
        "            if current.right is not None:\n",
        "                self.insert_node(current.right, new_value)\n",
        "            else:\n",
        "                current.right = TreeNode(new_value)\n",
        "                current.right.parent = current\n",
        "\n",
        "    def remove_tree_node(self, node):\n",
        "        if node is None:\n",
        "            return\n",
        "\n",
        "        # Node has no children\n",
        "        if node.left is None and node.right is None:\n",
        "            if node.parent is None:  # Root node case\n",
        "                self.root = None\n",
        "            elif node.parent.left == node:\n",
        "                node.parent.left = None\n",
        "            else:\n",
        "                node.parent.right = None\n",
        "\n",
        "        # Node has one child\n",
        "        elif node.left is None or node.right is None:\n",
        "            child = node.left if node.left else node.right\n",
        "            if node.parent is None:  # Root node case\n",
        "                self.root = child\n",
        "                child.parent = None\n",
        "            elif node.parent.left == node:\n",
        "                node.parent.left = child\n",
        "            else:\n",
        "                node.parent.right = child\n",
        "            child.parent = node.parent\n",
        "\n",
        "        # Node has two children\n",
        "        else:\n",
        "            successor = self.get_min_value_node(node.right)\n",
        "            node.value = successor.value\n",
        "            self.remove_tree_node(successor)\n",
        "\n",
        "    def get_min_value_node(self, node):\n",
        "        current = node\n",
        "        while current.left is not None:\n",
        "            current = current.left\n",
        "        return current\n",
        "\n",
        "    def remove_value(self, target):\n",
        "        node = self.find_tree_node(target)\n",
        "        self.remove_tree_node(node)\n",
        "\n",
        "    def print_tree(self):\n",
        "        def print_subtree(node, level=0):\n",
        "            if node is not None:\n",
        "                print_subtree(node.right, level + 1)\n",
        "                print(\" \" * 4 * level + f\"-> {node.value}\")\n",
        "                print_subtree(node.left, level + 1)\n",
        "        print_subtree(self.root)\n"
      ],
      "metadata": {
        "id": "Dw6yZC6LPLQu"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Min / Max Value Search"
      ],
      "metadata": {
        "id": "P3HGaLrwIxWq"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class TreeNode:\n",
        "    def __init__(self, value):\n",
        "        self.value = value\n",
        "        self.left = None\n",
        "        self.right = None\n",
        "        self.parent = None\n",
        "\n",
        "class BinarySearchTree:\n",
        "    def __init__(self):\n",
        "        self.root = None\n",
        "\n",
        "    def find_value(self, current, target):\n",
        "        if current is None:\n",
        "            return None\n",
        "        if current.value == target:\n",
        "            return current\n",
        "        if target < current.value:\n",
        "            return self.find_value(current.left, target)\n",
        "        else:\n",
        "            return self.find_value(current.right, target)\n",
        "\n",
        "    def find_value_itr(self, root, target):\n",
        "        current = root\n",
        "        while current is not None and current.value != target:\n",
        "            if target < current.value:\n",
        "                current = current.left\n",
        "            else:\n",
        "                current = current.right\n",
        "        return current\n",
        "\n",
        "    def find_tree_node(self, target):\n",
        "        if self.root is None:\n",
        "            return None\n",
        "        return self.find_value(self.root, target)\n",
        "\n",
        "    def insert_tree_node(self, new_value):\n",
        "        if self.root is None:\n",
        "            self.root = TreeNode(new_value)\n",
        "        else:\n",
        "            self.insert_node(self.root, new_value)\n",
        "\n",
        "    def insert_node(self, current, new_value):\n",
        "        if new_value == current.value:\n",
        "            return  # Skip inserting duplicates\n",
        "        if new_value < current.value:\n",
        "            if current.left is not None:\n",
        "                self.insert_node(current.left, new_value)\n",
        "            else:\n",
        "                current.left = TreeNode(new_value)\n",
        "                current.left.parent = current\n",
        "        else:\n",
        "            if current.right is not None:\n",
        "                self.insert_node(current.right, new_value)\n",
        "            else:\n",
        "                current.right = TreeNode(new_value)\n",
        "                current.right.parent = current\n",
        "\n",
        "    def remove_tree_node(self, node):\n",
        "        if node is None:\n",
        "            return\n",
        "\n",
        "        # Case 1: Node has no children (leaf node)\n",
        "        if node.left is None and node.right is None:\n",
        "            if node.parent is None:  # Node is the root\n",
        "                self.root = None\n",
        "            elif node.parent.left == node:\n",
        "                node.parent.left = None\n",
        "            else:\n",
        "                node.parent.right = None\n",
        "\n",
        "        # Case 2: Node has one child\n",
        "        elif node.left is None or node.right is None:\n",
        "            child = node.left if node.left is not None else node.right\n",
        "            if node.parent is None:  # Node is the root\n",
        "                self.root = child\n",
        "            elif node.parent.left == node:\n",
        "                node.parent.left = child\n",
        "            else:\n",
        "                node.parent.right = child\n",
        "            child.parent = node.parent\n",
        "\n",
        "        # Case 3: Node has two children\n",
        "        else:\n",
        "            successor = self.get_min_value_node(node.right)\n",
        "            node.value = successor.value\n",
        "            self.remove_tree_node(successor)\n",
        "\n",
        "    def get_min_value_node(self, node):\n",
        "        current = node\n",
        "        while current.left is not None:\n",
        "            current = current.left\n",
        "        return current\n",
        "\n",
        "    def get_max_value_node(self, node):\n",
        "        current = node\n",
        "        while current.right is not None:\n",
        "            current = current.right\n",
        "        return current\n",
        "\n",
        "    def remove_value(self, target):\n",
        "        node = self.find_tree_node(target)\n",
        "        self.remove_tree_node(node)\n",
        "\n",
        "    def print_tree(self):\n",
        "        def inorder_traversal(node):\n",
        "            if node is not None:\n",
        "                inorder_traversal(node.left)\n",
        "                print(node.value, end=' ')\n",
        "                inorder_traversal(node.right)\n",
        "\n",
        "        print(\"Inorder traversal of the tree:\")\n",
        "        inorder_traversal(self.root)\n",
        "        print()\n",
        "\n",
        "    def print_min_max(self):\n",
        "        if self.root is None:\n",
        "            print(\"The tree is empty.\")\n",
        "        else:\n",
        "            min_node = self.get_min_value_node(self.root)\n",
        "            max_node = self.get_max_value_node(self.root)\n",
        "            print(f\"Minimum value: {min_node.value}\")\n",
        "            print(f\"Maximum value: {max_node.value}\")\n"
      ],
      "metadata": {
        "id": "PiD3XtakPhiy"
      },
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Explanation\n",
        "\n",
        "1. InsertNode:\n",
        "  - Adds a new node with a given value to the tree.\n",
        "  - Checks if the current node should go left or right and recursively finds the position.\n",
        "  - Sets parent pointer for maintaining references.\n",
        "2. RemoveTreeNode:\n",
        "  - Handles three cases:\n",
        "    - Leaf Node: Simply deletes the node.\n",
        "    - One Child: Promotes the child node.\n",
        "    - Two Children: Finds the successor (smallest value in the right subtree), splices it, and replaces the node to be deleted.\n",
        "3. PrintTree:\n",
        "  - Uses breadth-first traversal to display the tree structure by levels.\n",
        "\n",
        "These examples and explanations illustrate the common operations in a binary search tree and provide insights into tree manipulation, making it easier to visualize how insertions and deletions work."
      ],
      "metadata": {
        "id": "XhhSBexTM7tu"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "9hvq3ROYI0dD"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}