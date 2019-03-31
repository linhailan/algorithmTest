import unittest
# 34、调整数组顺序使奇数位于偶数前面
#
# 题目1：输入一个整数数组，调整数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。要求时间复杂度为O(n)。

def reorderarray(oarray):
    left = 0
    right = len(oarray) - 1
    while left < right:
        while left < right and ((oarray[left] & 1) == 1):
            left += 1  #oarray[left]为奇数，自增至偶数为止
        while left < right and ((oarray[right] & 1) != 1):
            right -= 1 #oarray[right]为偶数，自减直至为奇数为止
        if left < right:
            temp = oarray[left]
            oarray[left] = oarray[right]
            oarray[right] = temp

# oarray = [1,2,3,4,5,2,3,5,4,6,7,9,11,12]
# print(oarray)
# reorderarray(oarray)
# print("===",oarray)

#1,2,3,4,5,2,3,5,4,6,7,9,11,12
#1,11,3,9,5,7,3,5,4,6,2,4,2,12

def reorderarray1(oarray):
    left = 0
    right = len(oarray) - 1
    while left < right:
        while left < right and (not isEven(oarray[left])):
            left += 1
        while left < right and (isEven(oarray[right])):
            right -= 1
        if left < right:
            temp = oarray[left]
            oarray[left] = oarray[right]
            oarray[right] = temp

def isEven(n):
    return (n&1) == 0


# oarray = [1,2,3,4,5,2,3,5,4,6,7,9,11,12]
# reorderarray1(oarray)
# print("***",oarray)


# 题目2：输入一个整数数组，调整数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分，
#       并保证奇数和奇数，偶数和偶数之间的相对位置不变。
def reorderarray2(oarray):
    olength = len(oarray)
    oddnumber = 0 # 奇数
    evennumber = 0 # 偶数
    oddindex = 0
    evenindex = 0
    while (oddindex < olength) and (evenindex < olength):
        #奇数指针从左往右走，找到第一个偶数后停下来
        while oddindex < olength:
            if isEven(oarray[oddindex]):
                evennumber = oarray[oddindex]
                break
            oddindex += 1

        # 如果奇数指针走到最后都没有找到偶数，指针指向最后一个数
        if oddindex >= olength:
            print("最后一个数是奇数，oddindex溢出")



        evenindex = oddindex + 1
        # 如果奇数指针下次到最后了，下面这个循环不会被执行，evenindex也溢出了
        while evenindex < olength:
            if not isEven(oarray[evenindex]):
                oddnumber = oarray[evenindex]
                break
            evenindex += 1

        #如果偶数指针走到最后都没有找到奇数
        if evenindex > olength:
            print("最后一个数是偶数,evenindex溢出")

        if oddindex < olength:    # 这个时候奇数指针指向了一个偶数
            if evenindex < olength:   #这个时候偶数指针指向一个奇数
                    oarray[oddindex] = oddnumber  # 把偶数指针指向的奇数赋给奇数指针所在的位置
                    for j in range(evenindex,oddindex,-1):
                        oarray[j] = oarray[j-1]
                    oarray[oddindex+1] = evennumber

        oddindex = oddindex + 1
        evenindex = evenindex + 1
    return oarray





class Reorderarray2Test(unittest.TestCase):
    def setUp(self):
        print("setUp")
    def tearDown(self):
        print("tearDown")
    def test1(self):
        print("数组中全是偶数")
        toBeTestArray=[2,4,6]
        reorderarray2(toBeTestArray)
        assert toBeTestArray == [2,4,6]
    def test2(self):
        print("数组中全是奇数")
        toBeTestArray=[1,3,5]
        reorderarray2(toBeTestArray)
        assert toBeTestArray == [1,3,5]
    def test3(self):
        print("奇偶间隔")
        toBeTestArray=[1,2,3,4,5]
        reorderarray2(toBeTestArray)
        assert toBeTestArray == [1,3,5,2,4]
    def test4(self):
        print("偶数在前面，奇数在后面")
        toBeTestArray=[2,4,6,1,3,5]
        reorderarray2(toBeTestArray)
        assert toBeTestArray == [1,3,5,2,4,6]
    def test5(self):
        print("一个偶数")
        toBeTestArray=[2]
        reorderarray2(toBeTestArray)
        assert toBeTestArray == [2]
    def test6(self):
        print("一个奇数")
        toBeTestArray=[1]
        reorderarray2(toBeTestArray)
        assert toBeTestArray == [1]

    def test7(self):
        print("普通")
        toBeTestArray=[1,2,3,4,5,2,3,5,4,6,7,9,11,12]
        reorderarray2(toBeTestArray)
        assert toBeTestArray == [1,3,5,3,5,7,9,11,2,4,2,4,6,12]



def suite():
    suite = unittest.TestSuite()
    suite.addTest(Reorderarray2Test("test1"))
    suite.addTest(Reorderarray2Test("test2"))
    suite.addTest(Reorderarray2Test("test3"))
    suite.addTest(Reorderarray2Test("test4"))
    suite.addTest(Reorderarray2Test("test5"))
    suite.addTest(Reorderarray2Test("test6"))
    suite.addTest(Reorderarray2Test("test7"))
    return suite

if __name__ == "__main__":
    unittest.main(defaultTest='suite')

