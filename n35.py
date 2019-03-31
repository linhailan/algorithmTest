import unittest

# 35、最长公共字串
#
# 题目：如果字符串一的所有字符按其在字符串中的顺序出现在另外一个字符串二中，则字符串一称之为字符串二的子串。
# 注意，并不要求子串（字符串一）的字符必须连续出现在字符串二中。
# 请编写一个函数，输入两个字符串，求它们的最长公共子串，并打印出最长公共子串。
def longestCommonSubstring(str1,str2):
    print("str1:",str1)
    print("str2:",str2)

    str1length = len(str1)
    str2length = len(str2)
    if str1length == 0 or str2length == 0:
        return 0
    start1 = -1
    start2 = -1
    longest = 0
    comparisons = 0

    for i in range(0,str1length):
        for j in range(0,str2length):
            length = 0
            m = i
            n = j
            while m < str1length and n < str2length:
                comparisons += 1
                if str1[m] != str2[n]:
                    break # 两个字符不等的时候终止循环
                length += 1  #两个字符相等的时候，length加一
                m += 1
                n += 1

            if longest < length:
                longest = length
                start1 = i
                start2 = j
    print("comparisons:", comparisons)
    return longest,start1,start2


class LongestCommonSubstringTest(unittest.TestCase):
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test1(self):
        print("")
        tobeteststr1 = "abcde"
        tobeteststr2 = "1234abc456789"

        longestresult,start1,start2 = longestCommonSubstring(tobeteststr1,tobeteststr2)
        print("longestresult:",longestresult)
        assert longestresult == 3
        assert tobeteststr1[start1:start1+longestresult] == tobeteststr2[start2:start2+longestresult]

    def test2(self):
        print("")
        tobeteststr1 = "abcde"
        tobeteststr2 = "1234456789"

        longestresult,start1,start2 = longestCommonSubstring(tobeteststr1,tobeteststr2)
        print("longestresult:",longestresult,",start1",start1,",start2",start2)
        assert longestresult == 0
        assert start1 == -1
        assert start2 == -1

def suite():
    suite = unittest.TestSuite()
    suite.addTest(LongestCommonSubstringTest("test1"))
    suite.addTest(LongestCommonSubstringTest("test2"))

    return suite

if __name__ == "__main__":
    unittest.main(defaultTest='suite')

