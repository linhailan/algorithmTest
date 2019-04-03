# 38、找出数组中两个只出现一次的数字
# 题目：一个整型数组里除了两个数字之外，其他的数字都出现了两次。
# 请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
# 分析：这是一道很新颖的关于位运算的面试题

import unittest

class Solution:
    def getoncenumber1(self,lista,listb):
        listsum = lista + listb
        result = set()
        checked = set()
        for i in range(0,len(listsum)):

            # 已经检查过的数字不再检查
            if listsum[i]  in checked:
                continue

            count_i = listsum.count(listsum[i])
            if count_i == 1:
                result.add(listsum[i])
            else:
                # 保存已经检查过的数字
                checked.add(listsum[i])
        return result


class GetOnceNumber1Test(unittest.TestCase):
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test1(self):
        lista = [1,2,3,4]
        listb = [1,3]
        s = Solution()
        result = s.getoncenumber1(lista,listb)
        assert result == {2,4}



def suite():
    suite = unittest.TestSuite()
    suite.addTest(GetOnceNumber1Test("test1"))


    return suite

if __name__ == "__main__":
    unittest.main(defaultTest='suite')


