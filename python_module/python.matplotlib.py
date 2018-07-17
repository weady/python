# -*- coding:utf-8 -*-
from matplotlib import pyplot as plt
import sys
reload(sys)
sys.setdefaultencoding('utf8')
plt.rcParams['font.family'] = 'SimHei'  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

#主要函数说明
'''
    np.linspace(-1,1 50) 范围(-1,1) 个数是50
    plt.figure() 定义一个图像窗口
    plt.plot(x,y) 绘图
    plt.show() 显示图像
    plt.savefig('test.pdf', dpi=900) 将绘制的图画保存成pdf格式,命名为test.pdf
    plt.ylabel('y轴标签') Y轴标签
    plt.xlabel('x轴标签') X轴标签
        eg:plt.xlabel('横轴:时间'， fontproperties = 'SimHei',fontsize = 20)
    plt.axis([-1, 10, 0, 6]) X轴启始于-1， 终止与10， Y轴启始于0，终止于6
    plt.subplot(3,2,4) 分成3行2列，工6个绘制区域,在第四区域绘图。排序为行优先。也可以plt.subplot(324)
    plt.show()  # 展示图形
    plot(x, y, color='green', marker='o', linestyle='dashed',linewidth=2, markersize=12)
    plt.plot(x,y,format_string,**kwargs)
    plt.title() 图形的文本标签
    plt.text() 在任意位置增加文本
        eg:plt.text(-3.7,3,r'$This is a test$')
    plt.annotate(s,xy= arrow_crd,xytext = text_crd, arrowprops = dict) 标注
        eg: plt.annotate(r'注释信息',xy=(1,2),xycoords='data', xytext=(+30,-30), textcoords='offset points') 
        xy=(x0,y0) 对哪个位置点进行注释  xytext() 注释信息的位置相对于注释点的位置
    plt.subplot2grid((3,3),(1,0),colspan = 2) (3,3) 表示为3行3列, (1, 0) 表示选择第1行，第0列的区域进行绘图, colspan =2 表示跨列, rowspan =2 表示跨行
    plt.xlim() x 轴的取值范围
    plt.ylim((-2,3)) y轴的取值范围
    plt.xticks(new_ticks) 设置X轴刻度
    plt.yticks([-2, -1.8, -1],[r'$really$', r'$good$', r'$best$']) 设置y轴刻度以及名称
    调整坐标轴
    ax = plt.gca() #gca get current axis
    ax.spines['right'].set_color('none') 图像的右边框取消
    ax.spines['top'].set_color('none') 上边框取消
    ax.xaxis.set_ticks_position('bottom') 把下边框设置为X轴刻度
    ax.yaxis.set_ticks_position('left') 把下边框设置为X轴刻度
    ax.spines['bottom'].set_position(('data',0)) X轴移动到y=0的位置 axes 表示移动到Y轴的百分比
    ax.spines['left'].set_position(('data',0)) Y轴移动到x=0的位置 axes 表示移动到X轴的百分比
    plt.legend(handles[L1,L2],label['aaa','bbb',loc='upper right']) 图例就是为了帮助我们展示出每个数据对应的图像名称 loc:best upper left
    ax.get_xticklabels() X轴的刻度标
'''
#线型图
def py_plot():
    plt.plot(['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日'] , [1, 12, 3, 4, 5, 16, 7], color='green', label=u'曲线图')  # plot(x, y, color='green', marker='o', linestyle='dashed',linewidth=2, markersize=12)
    plt.plot(['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日'] , [11, 12, 13, 14, 15, 18, 17], 'r--', label=u'成绩表')
    plt.plot([3, 3], [20, 0], 'b--')  # 画一条直线
    plt.scatter(3, 4)
    plt.text(3, 4, r'$This\ is\ a\ test$', fontdict={'size':16, 'color': 'red'})
    plt.ylabel(u"x轴标签")  # X轴标签
    plt.ylabel(u"y轴标签")  # Y轴标签
    # plt.axis([0, 100, 0, 20])
    plt.legend()  # 显示注释标签
    plt.savefig('test.pdf', dpi=800)  # 将输出图形存储为文件，默认为png格式。可以通过dpi修改输出质量
    plt.show()  # 展示图形

#子图
def py_subplot():
    '''
    plot.subplot(nrows,ncols,plot_number) 在全局绘制区域创建一个分区体系,并定位到一个绘图区域
    '''
    import numpy as np
    a = np.arange(0.0, 5.0, 0.02)
    plt.subplot(211)
    plt.plot(a, np.exp(-a)*np.cos(2*np.pi*a))
    plt.subplot(2, 1, 2)
    plt.plot(a, np.cos(2*np.pi * a), 'r--')
    plt.show()

#饼图
def py_plot_pie():
    labels = ['Tomcat', 'Jboss', 'Nginx', 'MySQL']
    sizes = [12, 20, 34, 90]
    explode = (0, 0, 0.1, 0)
    plt.figure('Pie')
    plt.title(u'测试数据饼图数据')
    plt.text(1, 1, u'注释信息', color='red')
    plt.axis('equal')
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
    plt.show()

#多种曲线图合并在一起
def py_add_picture():
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    # 通过rcParams设置全局横纵轴字体大小
    mpl.rcParams['xtick.labelsize'] = 24
    mpl.rcParams['ytick.labelsize'] = 24

    np.random.seed(42)

    # x轴的采样点
    x = np.linspace(0, 5, 100)

    # 通过下面曲线加上噪声生成数据，所以拟合模型就用y了……
    y = 2*np.sin(x) + 0.3*x**2
    y_data = y + np.random.normal(scale=0.3, size=100)

    # figure()指定图表名称
    plt.figure('data')

    # '.'标明画散点图，每个散点的形状是个圆
    plt.plot(x, y_data, '.')

    # 画模型的图，plot函数默认画连线图
    plt.figure('model')
    plt.plot(x, y)

    # 两个图画一起
    plt.figure('data & model')

    # 通过'k'指定线的颜色，lw指定线的宽度
    # 第三个参数除了颜色也可以指定线形，比如'r--'表示红色虚线
    # 更多属性可以参考官网：http://matplotlib.org/api/pyplot_api.html
    plt.plot(x, y, 'k', lw=3)

    # scatter可以更容易地生成散点图
    plt.scatter(x, y_data)

    # 将当前figure的图保存到文件result.png
    # plt.savefig('result.png')

    # 一定要加上这句才能让画好的图显示在屏幕上
    plt.show()

def py_mul_pic():
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    mpl.rcParams['axes.titlesize'] = 20
    mpl.rcParams['xtick.labelsize'] = 16
    mpl.rcParams['ytick.labelsize'] = 16
    mpl.rcParams['axes.labelsize'] = 16
    mpl.rcParams['xtick.major.size'] = 0
    mpl.rcParams['ytick.major.size'] = 0

    # 包含了狗，猫和猎豹的最高奔跑速度，还有对应的可视化颜色
    speed_map = {
        'dog': (48, '#7199cf'),
        'cat': (45, '#4fc4aa'),
        'cheetah': (120, '#e1a7a2')
    }

    # 整体图的标题
    fig = plt.figure('Bar chart & Pie chart')

    # 在整张图上加入一个子图，121的意思是在一个1行2列的子图中的第一张
    ax = fig.add_subplot(121)
    ax.set_title('Running speed - bar chart')

    # 生成x轴每个元素的位置
    xticks = np.arange(3)

    # 定义柱状图每个柱的宽度
    bar_width = 0.5

    # 动物名称
    animals = speed_map.keys()

    # 奔跑速度
    speeds = [x[0] for x in speed_map.values()]

    # 对应颜色
    colors = [x[1] for x in speed_map.values()]

    # 画柱状图，横轴是动物标签的位置，纵轴是速度，定义柱的宽度，同时设置柱的边缘为透明
    bars = ax.bar(xticks, speeds, width=bar_width, edgecolor='none')
    #添加箭头注释信息
    ax.annotate(u'注释', xy=(0, 90), xytext=(1, 100), arrowprops=dict(facecolor='g', shrink=0.01), color='r')
    # 设置y轴的标题
    ax.set_ylabel('Speed(km/h)')

    # x轴每个标签的具体位置，设置为每个柱的中央
    ax.set_xticks(xticks+bar_width/2)

    # 设置每个标签的名字
    ax.set_xticklabels(animals)

    # 设置x轴的范围
    ax.set_xlim([bar_width/2-0.5, 3-bar_width/2])

    # 设置y轴的范围
    ax.set_ylim([0, 125])

    # 给每个bar分配指定的颜色
    for bar, color in zip(bars, colors):
        bar.set_color(color)

    # 在122位置加入新的图
    ax = fig.add_subplot(122)
    ax.set_title('Running speed - pie chart')

    # 生成同时包含名称和速度的标签
    labels = ['{}\n{} km/h'.format(animal, speed) for animal, speed in zip(animals, speeds)]

    # 画饼状图，并指定标签和对应颜色
    ax.axis('equal')
    ax.pie(speeds, labels=labels, colors=colors
           )
    plt.savefig(u'数据报表.pdf', dpi=1000)
    plt.show()

#条形图
def py_plot_bar():
    X1 = [1, 3, 5, 7, 9]
    Y1 = [5, 8, 10, 19, 21]
    X2 = [2, 4, 6, 8, 10]
    Y2 = [8, 18, 20, 31, 38]
    plt.bar(X1, Y1, label=u'曲线图1', facecolor='#ff9999') # facecolor 修改条形柱颜色
    plt.bar(X2, Y2, label=u'曲线图2', facecolor='#9999ff')
    plt.legend(loc='upper left')
    plt.xlim((0, 15))
    #添加标注在条形图上方, 把Y的值添加到条形图上方
    for x, y in zip(X1, Y1):
        plt.text(x + 0.05, y + 0.3, '%.2f' % y, ha='center', va='bottom')

    for x, y in zip(X2, Y2):
        plt.text(x + 0.05, y + 0.3, '%.2f' % y, ha='center', va='bottom')

    plt.plot([0, 15], [18, 18], 'r--') #添加了一条平均线
    plt.text(13, 17.5, u'基准线', color='b') #为基准线添加注释
    plt.xlabel(u'X轴')
    plt.ylabel(u'Y轴')
    plt.title(u'直方图')
    plt.savefig(u'条形图报表.pdf', dpi=1000)
    plt.show()

#实现动态图 数据从外部文件读取
def py_plot_auto():
    from matplotlib import animation as animation
    from matplotlib import style
    style.use('fivethirtyeight')

    fig = plt.figure() #定义一个画布
    ax1 = fig.add_subplot(1, 1, 1)
    data_list = ['1,2', '2,4', '3,6', '4,8', '5,9', '6,3', '7,4', '8,1', '9,3', '10,7', '13,12']
    xs = []
    ys = []
    def animate(i):
        for line in data_list:
            if len(line) >1:
                x, y = line.split(',')
                xs.append(x)
                ys.append(y)
        ax1.clear()
        ax1.plot(xs, ys)


    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()

#  子图,一个画布上添加多个子图 利用add_subplot()进行子图添加
def py_sub_plot():
    fig = plt.figure(u'子图') #定义一个画布
    import random
    xs = []
    ys = []

    for i in xrange(1, 10):
        x = i
        y = random.randint(1, 10)
        xs.append(x)
        ys.append(y)

    labels = ['Tomcat', 'Jboss', 'Nginx', 'MySQL']
    sizes = [12, 20, 34, 90]
    explode = (0, 0, 0.1, 0)

    #利用add_subplot()进行子图添加
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(212)

    #利用subplot2grid() 进行子图添加
    ax1 = plt.subplot2grid((75, 2), (0, 0), rowspan=15, colspan=2)
    ax2 = plt.subplot2grid((75, 2), (20, 0), rowspan=15, colspan=2)
    ax3 = plt.subplot2grid((75, 2), (40, 0), rowspan=15, colspan=2)
    ax4 = plt.subplot2grid((75, 2), (55, 0), rowspan=15, colspan=1)


    L1, = ax1.plot(xs, ys, 'r--', label='line01')  # L1 在plt.legend(handles=[L1,L2,L3],label=['aa','bb','cc'])
    L2, = ax2.plot(xs, ys, 'g', label='line02')
    L3, = ax3.plot(xs, ys, label='line03')
    ax4.axis('equal')
    ax4.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)

    plt.legend(loc='upper left')

    plt.savefig(u'子图.pdf', dpi=1000)
    plt.show()

#散点图
def py_scatter():
    import numpy as np
    n = 1024
    X = np.random.normal(0, 1, n)
    Y = np.random.normal(0, 1, n)
    C = np.arctan2(Y, X) # 值的颜色
    plt.scatter(X, Y, s=50, c=C, alpha=0.6)
    plt.xlim((-3, 3))
    plt.ylim((-3, 3))
    plt.xticks(())  # 取消X轴的刻度标
    plt.yticks(())  # 取消Y轴的刻度标
    plt.show()

if __name__ == '__main__':
    # py_plot()
    # py_subplot()
    # py_plot_pie()
    # py_add_picture()
    # py_mul_pic()
    py_plot_bar()
    # py_plot_auto()
    # py_sub_plot()
    # py_scatter()