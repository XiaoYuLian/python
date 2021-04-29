import pandas.io.excel._xlrd
import pandas.io.excel._xlwt            #进行excel操作
import xlwt


workbook = xlwt.Workbook(encoding="utf-8")                                      #创建workbook对象
worksheet = workbook.add_sheet('交通出行调查表',cell_overwrite_ok=True)                #创建工作表
clo = ("出发地","到达地","出行量")
workbook.write

# workbook = xlrd.open_workbook("student.xls")
# sheet_name = workbook.sheet.name()
