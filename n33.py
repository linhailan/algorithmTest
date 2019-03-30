# 33、字符串的排列
#
# 题目：输入一个字符串，打印出该字符串中字符的所有排列。
#
# 例如输入字符串abc，则输出由字符a、b、c 所能排列出来的所有字符串abc、acb、bac、bca、cab 和cba。
#
# 分析：这是一道很好的考查对递归理解的编程题。

# 输入描述：
# 输入一个字符串，长度不超过9（可能有字符重复），字符只包括大小写字母
# 解题思路：
# 求整个字符串的全排列可以看做两步
# （1）首先求出所有可能出现在第一位置的字母，即begin与后面所有与它不同的字母进行交换
# （2）固定第一个字母，求后面字母的全排列，即递归此时begin = begin + 1


class Solution:
    def permutation(self, pstr):
        print("需要找出所有排列的字符串：",pstr)
        resultlist = set()
        if pstr is None:
            return resultlist

        self.permutation1(resultlist,pstr,0)

        # sort(a.begin(), a.end()); // 按照字典序输出
        return sorted(resultlist)

    def permutation1(self, rarray, pstr, begin):

        print("**************************begin: ",begin,",***pstr:",pstr,",***rarray:",rarray ,"**************")

        if begin == (len(pstr) -1):
            rarray.add(pstr)
            print("添加新组合：",pstr)
            return

        for i in range(begin,len(pstr)):
            print("=========begin:",begin,"====,i:",i,"====,   rarray:",rarray,"===,  pstr:",pstr,"=====")

            # 与begin位重复的字符串不进行交换，跳过
            if i != begin and pstr[i] == pstr[begin]:
                print("与begin位重复的字符串不进行交换，跳过")
                continue

            # 把字符str[i]和字符str[begin]交换
            if i != begin:
                # 将字符串转换成数组
                strlist = list(pstr)
                # 将begin保存到temp中
                temp = pstr[begin]
                # 将str[i]赋给begin
                strlist[begin] = strlist[i]
                # 将temp赋给str[i[
                strlist[i] = temp
                # 将数组联结成字符串
                pstr = ''.join(strlist)

            print("下一级排序前的pstr:",pstr)
            self.permutation1(rarray,pstr,begin+1)

            # 把字符str[i]和字符str[begin]交换
            if i != begin:
                # 将字符串转换成数组
                strlist = list(pstr)
                # 将begin保存到temp中
                temp = pstr[begin]
                # 将str[i]赋给begin
                strlist[begin] = strlist[i]
                # 将temp赋给str[i[
                strlist[i] = temp
                # 将数组联结成字符串
                pstr = ''.join(strlist)

            print("i:",i,",begin:",begin,"换回来的字符串：",pstr)


if __name__ == '__main__':
    pstr = 'abb'
    s = Solution()
    result = s.permutation(pstr)
    print("结果：",result)