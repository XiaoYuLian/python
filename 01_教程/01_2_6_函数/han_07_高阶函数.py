# coding=UTF-8
#告诫韩式是指作用于一个函数或者返回一个函数的函数，使用functools,需要先导入函数库functools
import functools                        #导入函数库
###################################例一:partial()##############################################
#功能：为某个函数复制一些参数，返回一个新的函数
print(int('100101',2))                  #int('a',b)     把b进制数字a转换为十进制

int2=functools.partial(int,base=2)      
#定义新函数int2，内容是由partial函数对int函数调整而来，调整内容是int函数的第二个参数base默认为2

