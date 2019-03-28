
import unittest
'''
32、二元树的深度

题目：输入一棵二元树的根结点，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

分析：这道题本质上还是考查二元树的遍历。
'''

# 定义二叉树的结点
class BinaryTreeNode:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class TreeDepthHelper:
    def gettreedepth(self,root):
        if root:
            left = self.gettreedepth(root.left)
            right = self.gettreedepth(root.right)
            if left >= right:
                result = left + 1
            else:
                result = right + 1
        else:
            result = 0
        return result

class TreeDepthTest:
    helper = TreeDepthHelper()
    def setsubtreenode(self,root,left,right):
        if root:
            root.left = left
            root.right = right
        else:
            print("root is None")
            return

    def cleanuptreenode(self,root):
        if root:
            left = root.left
            right = root.right
            root = None
            self.cleanuptreenode(left)
            self.cleanuptreenode(right)
    def getdepthtest1(self):
        node1 = BinaryTreeNode(1)
        node2 = BinaryTreeNode(2)
        node3 = BinaryTreeNode(3)
        node4 = BinaryTreeNode(4)
        node5 = BinaryTreeNode(5)
        node6 = BinaryTreeNode(6)
        node7 = BinaryTreeNode(7)

        self.setsubtreenode(node1,node2,node3)
        self.setsubtreenode(node2,node4,node5)
        self.setsubtreenode(node3,None,node6)
        self.setsubtreenode(node5,node7,None)

        test1depth = self.helper.gettreedepth(node1)
        print("test1depth: ",test1depth)

        assert test1depth == 4
        self.cleanuptreenode(node1)

    def getdepthtest2(self):
        node1 = BinaryTreeNode(1)
        node2 = BinaryTreeNode(2)
        node3 = BinaryTreeNode(3)
        node4 = BinaryTreeNode(4)
        node5 = BinaryTreeNode(5)

        self.setsubtreenode(node1,node2,None)
        self.setsubtreenode(node2,node3,None)
        self.setsubtreenode(node3,node4,None)
        self.setsubtreenode(node4,node5,None)

        test2depth = self.helper.gettreedepth(node1)
        print("test2depth: ",test2depth)

        assert test2depth == 5
        self.cleanuptreenode(node1)
    def getdepthtest3(self):
        node1 = BinaryTreeNode(1)
        node2 = BinaryTreeNode(2)
        node3 = BinaryTreeNode(3)
        node4 = BinaryTreeNode(4)
        node5 = BinaryTreeNode(5)

        self.setsubtreenode(node1,None,node2)
        self.setsubtreenode(node2,None,node3)
        self.setsubtreenode(node3,None,node4)
        self.setsubtreenode(node4,None,node5)

        test3depth = self.helper.gettreedepth(node1)
        print("test3depth: ",test3depth)

        assert test3depth == 5
        self.cleanuptreenode(node1)
    def getdepthtest4(self):
        node1 = BinaryTreeNode(1)
        test4depth = self.helper.gettreedepth(node1)
        print("test4depth: ",test4depth)

        assert test4depth == 1
        self.cleanuptreenode(node1)

    def getdepthtest5(self):
        test5depth = self.helper.gettreedepth(None)
        print("test5depth: ",test5depth)

        assert test5depth == 0



if __name__ == '__main__':
    test = TreeDepthTest()
    test.getdepthtest1()
    test.getdepthtest2()
    test.getdepthtest3()
    test.getdepthtest4()
    test.getdepthtest5()