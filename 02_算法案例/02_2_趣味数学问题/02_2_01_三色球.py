"""
一个袋子中有3个红球，3个黄球以及6个黑球，从中取出8个，问去除的求种颜色组合有几种
"""
for a in range (0,4):
    for b in range (0,4):
            if(8-a-b<=6):
                print("红球的个数为%d，黄球的个数为%d，黑球的个数为%d" %(a,b,8-a-b))