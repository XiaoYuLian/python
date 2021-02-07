import csv
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.font_manager as mf
my_font = mf.FontProperties(fname='C:/Windows/Fonts/simhei.ttf')

filename = 'death_valley_2018_full.csv'
with open(filename, 'r') as f:
    reader = csv.reader(f)
    reader_row = next(reader)
    for index, colum_header in enumerate(reader_row):
        print(index, colum_header)
    # 从文件中提取最低气温和最低气温

    mins = []
    maxs = []
    dates = []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")


        min=int(row[7])
        dates.append(current_date)
        max= int(row[6])
        maxs.append(max)
        mins.append(min)

        # 绘制最低温与最高气温
        plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, mins, c='blue', alpha=0.5)
        ax.plot(dates, maxs, c='red', alpha=0.5)
        ax.fill_between(dates, maxs, mins, facecolor='blue', alpha=0.1)
        # 设置图表格式
        plt.title('2018年最低气温与最高气温图', fontproperties=my_font, fontsize=20)
        plt.xlabel('',  fontproperties=my_font,fontsize=14)
        fig.autofmt_xdate()
        plt.margins(x=0)
        plt.ylabel('温度(F)',  fontproperties=my_font,fontsize=14)
        plt.tick_params(axis='both', which='major',  labelsize=10)
        plt.show()
