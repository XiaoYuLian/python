"""
第一步，点击键盘 win+r，打开运行窗口.
第二步，在运行窗口中输入“cmd"，点击确定，打开windows命令行窗口。
第三步，输入"pip install sympy",进行安装.
第四步，验证是否安装成功，在cmd命令行窗口中输入"python"，进入python交互窗口，
第五步，在python命令交互窗口中，输入"import sympy"，点击enter键，如果没有出错，表明安装成功。
"""

#第三题
import sympy                        #引入方程变量
TQ=sympy.symbols("TQ")              #定义未知数（自变量）TQ
AVC=(1+TQ/1500+150/TQ)              #AVC
AFC=180/TQ
ATC=AVC+AFC
a= sympy.solve([ATC*(1+0.05)/(1-0.056)-2.5],[TQ])   #解方程命令，（[Fx=0],[未知量]）
print(a)
