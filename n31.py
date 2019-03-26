# 和为n连续正数序列
# 输入一个正数n,输出所有和为n的连续正数序列
# 例如输入15，由于1+2+3+4+5=4+5+6=7+8=15,所以输出三个连续序列1-5.4-6,7-8

"""
public static  void getAns(int n)
{
    int beg=1;
    int sum=1;
    int cur=1;

    while (beg <= n / 2 + 1)
    {
        if (sum == n)
        {
            for (int k=beg;k <= cur;k++)
            {
                System.out.print(k + " ");
            }
            System.out.println();
            sum=sum-beg;
            beg++;
            cur++;
            sum += cur;
        }
        if (sum > n)
        {
            sum=sum-beg;
            beg++;
        }else
        {
            cur++;
            sum += cur;
        }
    }
}
"""

def n31(number):

    '''
    从第一个数开始加，每次左移一位，直到过了中间那个数
    :param number:
    :return:
    '''
    beg = 1
    sum = 1
    cur = 1

    list = []
    temp = []
    middle = number // 2 + 1

    print("middle:",middle)

    while beg <= middle:
        print("****************************")
        print("beg:",beg)
        print("cur:",cur)
        print("sum:",sum)
        if sum == number:
            print("sum == number")
            # 求和等于number的时候，将begin到cur的数添加到序列中
            for kk in range(beg,cur+1):
                temp.append(kk)
            print("得到的序列是",temp)
            # 将得到的序列添加到汇总的序列中
            list.append(temp)

            # 准备查找下一条符合条件的序列
            # 从sum中减去beg的值
            sum = sum - beg
            # beg值加一
            beg = beg + 1
            # 当前值加一
            cur = cur + 1
            # sum加上当前值得到新的sum
            sum = sum + cur
            print("~~~~~~~~~~~~~~~~~~~~")
            print("beg:", beg)
            print("cur:", cur)
            print("sum:", sum)
            print("~~~~~~~~~~~~~~~~~~~~")

        # 检查新计算出来的sum，如果大于number,计算的个数减掉一个
        # 如果小于number,计算的个数增加一个
        # 肯定不会等于number
        if sum > number:
            # 新的sum大于number,减去第一个值，beg 右移一位，此时cur不变，意味着相加的数据的数目会少一个
            print("计算的个数减少一个")
            sum = sum - beg
            beg = beg + 1
        else:
            # 新的sum小于number，当前值右移一位，再加一位数
            print("计算的个数增加一个")
            cur = cur + 1
            sum = sum + cur


        print("====================================")

    return list


flag = True
while True:
    number = input("number:")
    if number == "0":
        flag = False;
        break
    print("result:",n31(int(number)))
