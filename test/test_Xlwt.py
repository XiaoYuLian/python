import xlwt 

"""
workbook = xlwt.Workbook(encoding="utf-8")              #创建workbook对象
worksheet = workbook.add_sheet('sheet1')                #创建工作表
worksheet.write(0,0,'hello')                            #填入数据 行 列 内容
worksheet.write(0,1,'world')
workbook.save('student.xls')                            #键在内存中生成的文件保存到硬盘上
"""

#输出乘法表
workbook = xlwt.Workbook(encoding="utf-8")              #创建workbook对象
worksheet = workbook.add_sheet('sheet1')                #创建工作表
for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,"%dX%d=%d" %(i+1,j+1,(i+1)*(j+1)))
workbook.save('student.xls')                            #键在内存中生成的文件保存到硬盘上