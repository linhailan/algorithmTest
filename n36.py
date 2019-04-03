# 36、从尾到头输出链表
#
# 题目：输入一个链表的头结点，从尾到头反过来输出每个结点的值。
#
# 链表结点定义如下：
#
# struct ListNode
#
# {
#
# int m_nKey;
#
# ListNode* m_pNext;
#
# };

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


class Solution:
    def printlistfromtailtohead(self,listnode):
        out = []
        if listnode is None:
            return out
        while listnode.m_pnext is not None:
            out.append(listnode.m_nkey)
            listnode = listnode.m_pnext
        out.append(listnode.m_nkey)
        out.reverse()
        return out


class PrintListFromTailToHeadTest(unittest.TestCase):
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test1(self):
        s = Solution()
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node1.__add__(node2)
        node1.__add__(node3)

        result = s.printlistfromtailtohead(node1)
        assert result == [3,2,1]


def suite():
    suite = unittest.TestSuite()
    suite.addTest(PrintListFromTailToHeadTest("test1"))


    return suite

if __name__ == "__main__":
    unittest.main(defaultTest='suite')

