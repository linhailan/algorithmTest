# 37、在O（1）时间内删除链表结点
# 题目：给定链表的头指针和一个结点指针，在O(1)时间删除该结点。
# 链表结点的定义如下：
# struct ListNode
# {
#   int m_nKey;
#   ListNode* m_pNext;
# };
# 函数的声明如下：
# void DeleteNode(ListNode* pListHead, ListNode* pToBeDeleted);
# 分析：这道题考察编程基本功和反应速度，更重要的是考察面试者对时间复杂度的理解

import unittest


class ListNode:
    def __init__(self,m_nkey=0,m_pnext=None):
        self.m_nkey = m_nkey
        self.m_pnext = m_pnext

    def __add__(self, other):

        if self.m_pnext is None:
            self.m_pnext = other
            return

        nextnode = self.m_pnext
        while nextnode.m_pnext is not None:
            nextnode = nextnode.m_pnext
        nextnode.m_pnext = other

    def deletenode(self,plisthead,ptobedelete):
        if plisthead is None or ptobedelete is None:
            return

        # 删除头节点
        if plisthead == ptobedelete:
            plisthead = plisthead.m_pnext
            ptobedelete = None
            return

        currentnode = plisthead
        nextnode = plisthead.m_pnext

        while nextnode != ptobedelete:
            if nextnode is None:
                print("找不到待删除的节点")
                return
            currentnode = nextnode
            nextnode = nextnode.m_pnext

        # nextnode是待删除的节点
        currentnode.m_pnext = nextnode.m_pnext
        nextnode.m_pnext = None
        nextnode = None



class DeleteNodeTest(unittest.TestCase):
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test1(self):

        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node1.__add__(node2)
        node1.__add__(node3)

        node1.deletenode(node1,node2)
        assert node1.m_nkey == 1
        assert node1.m_pnext.m_nkey == 3



def suite():
    suite = unittest.TestSuite()
    suite.addTest(DeleteNodeTest("test1"))


    return suite

if __name__ == "__main__":
    unittest.main(defaultTest='suite')

