# 39、找出链表的第一个公共结点
# 题目：两个单向链表，找出它们的第一个公共结点。
# 链表的结点定义为：
# struct ListNode
# {
# int m_nKey;
# ListNode* m_pNext;
# };
# 分析：这是一道微软的面试题，在微软的面试题中，链表出现的概率相当高。

import unittest


class ListNode:
    def __init__(self,m_nkey,m_pnext=None):
        self.m_nkey = m_nkey
        self.m_pnext = m_pnext


class Solution:
    def findfirstcommonnode1(self,headx,heady):
        p1 = headx
        p2 = heady
        while p1 is not None:
            p2 = heady
            while p2 is not None:
                if p1 == p2:
                    print("找到相同的节点：",p1)
                    return p1
                p2 = p2.m_pnext
            p1 = p1.m_pnext
        print("没有相同的节点")
        return None

    # 这种方法找出来的是关键值相同的节点而不是相同的节点，而且顺序也不对
    def findfirstcommonnode2(self, headx, heady):
        print("=========enter findfirstcommonnode2=============  ")
        x = headx
        y = heady
        bitx = 0
        bity = 0

        # 遍历headx节点，对每个节点的值做或运算
        while x is not None:
            # 按位做或运算并赋值
            bitx |= 1 << x.m_nkey
            x = x.m_pnext

        while y is not None:
            bity |= 1 << y.m_nkey
            y = y.m_pnext

        print("bitx:", "{0:b}".format(bitx))
        print("bity:", "{0:b}".format(bity))

        inter = bitx & bity
        print("inter:", "{0:b}".format(inter))

        radix = 0
        while inter > 1:
            inter >>= 1
            radix += 1

        return radix

    def findfirstcommonnode3(self,phead1,phead2):
        print("*********enter findfirstcommonnode3************* ")
        p1 = phead1
        p2 = phead2
        # 1-->2-->3-->6-->(2)-->8
        # 4-->5-->2-->3-->6-->(2)-->8
        while p1 != p2:
            print("p1,p2: ",p1.m_nkey,",",p2.m_nkey)
            if p1 is not None:
                p1 = p1.m_pnext
            if p2 is not None:
                p2 = p2.m_pnext
            if p1 != p2:
                if p1 is None:
                    p1 = phead2
                    #4-->5-->2-->3-->6-->(2)-->8
                    #8
                if p2 is None:
                    p2 = phead1
                    #5-->2-->3-->6-->(2)-->8
                    #1-->2-->3-->6-->(2)-->8

        return p1


class FindFirstCommonNodeTest(unittest.TestCase):
    def tearDown(self):
        print("tearDown")

    def test1(self):
        print("test1")
        result = self.s.findfirstcommonnode1(self.node1,self.node4)
        assert result == self.node2
        self.s = None

    def test2(self):
        print("test2")
        result = self.s.findfirstcommonnode2(self.node1,self.node4)
        #这种方法只能得出两个链表中相同节点中关键值最大的那个节点的值是多少
        assert result == 8

        self.s = None

    def test3(self):
        print("test3")
        result = self.s.findfirstcommonnode3(self.node1,self.node4)
        print("test3, result: ",result)
        assert result == self.node2
        self.s = None

    def setUp(self):
        print("setUp")
        self.node1 = ListNode(1)
        self.node2 = ListNode(2)
        self.node3 = ListNode(3)
        self.node1.m_pnext = self.node2
        self.node2.m_pnext = self.node3
        # 1-->2-->3

        self.node4 = ListNode(4)
        self.node5 = ListNode(5)
        self.node6 = ListNode(6)
        self.node4.m_pnext = self.node5
        self.node5.m_pnext = self.node2
        self.node3.m_pnext = self.node6
        # 4-->5-->2-->3-->6-->(2)-->8

        self.node7 = ListNode(2)
        self.node6.m_pnext = self.node7

        self.node8 = ListNode(8)
        self.node7.m_pnext = self.node8

        self.s = Solution()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(FindFirstCommonNodeTest('test1'))
    print("suite:",suite)
    return suite


if __name__ == '__main__':
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    runner = unittest.TextTestRunner()
    runner.run(suite())