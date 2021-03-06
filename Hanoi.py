def move(n,A,B,C):
    if n==1:             # 1个盘子，直接打印出移动动作
        print(A,'--->',C)
    else:                # n > 1时，用抽象出的3步来移动
        move（n-1，A，C，B) #step1.  把除了最大的盘子之外的盘子从A移到B
        print(A,'--->',C)  #step2.  把最大的盘子从A移到C
        move（n-1，B，A，C）#step3.  把除了最大的盘子之外的盘子从B移到C

'''首先，题主你需要先理解n=2的情况，
非常简单：n=2时：
执行move(1,a,c,b)，
打印出A-->B；执行A-->C；
执行move(1,b,a,c)，打印出B-->C；
因此n=2时，相当于是将A中的两个盘子按照规则搬到了C中。
n=3时：执行move(2,a,c,b)，
带入我们之前所理解的结果，
即将A中的上面2个盘子按照规则搬到了B中，
并且打印出过程；将A中最下面的盘子搬到c中，打印A-->C；
 执行move(2,b,a,c)，即将B中的2个盘子按规则搬到C中，并且打印出过程。
 n=4时程序基于n=3上运行，一层套一层，这就是递归。


'''