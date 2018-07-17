#!/usr/bin/python
# -*- coding: utf-8 -*- 

#利用pyecharts进行绘图 http://pyecharts.org/#/zh-cn/prepare 

from pyecharts import Bar, Line, Grid, Scatter, EffectScatter, Pie, Overlap, Page, Scatter3D

'''
    add() 方法用于添加图表的数据和设置各种配置项
    bar.use_theme('dark') 更换主题色
    echarts-themes-pypkg 提供了 vintage, macarons, infographic, shine 和 roma 主题
    pip install echarts-themes-pypkg 安装插件
    更换运行环境内所有图表主题
    from pyecharts import configure
    #将这行代码置于首部
    configure(global_theme='dark')
    如果想直接将图片保存为 png, pdf, gif 格式的文件，可以使用 pyecharts-snapshot。使用该插件请确保你的系统上已经安装了 Nodejs 环境
    安装 phantomjs  $ npm install -g phantomjs-prebuilt
    安装 pyecharts-snapshot  $ pip install pyecharts-snapshot
    调用 render 方法  bar.render(path='snapshot.png') 文件结尾可以为 svg/jpeg/png/pdf/gif。请注意，svg 文件需要你在初始化 bar 的时候设置 renderer='svg'
    
    绘制图形步骤:
    chart_name = Type() 初始化具体类型图表。
    add() 添加数据及配置项。
    render() 生成本地文件（html/svg/jpeg/png/pdf/gif）。
    add() 数据一般为两个列表（长度一致）。如果你的数据是字典或者是带元组的字典。可利用 cast() 方法转换。
    @staticmethod
    cast(seq)
    转换数据序列，将带字典和元组类型的序列转换为 k_lst,v_lst 两个列表
'''

def py_bar():
    bar = Bar("我的第一个图表", "这里是副标题")
    bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
    bar.add("收入", ["衬", "衫", "纺衫", "裤子", "高跟鞋", "袜子"], [50, 12, 26, 30, 55, 60])
    # bar.print_echarts_options() # 该行只为了打印配置项，方便调试时使用
    bar.render()    # 生成本地 HTML 文件

def more_picture():
    '''一次生成多个图表文件'''
    from pyecharts.engine import create_default_environment

    bar = Bar("我的第一个图表", "这里是副标题")
    bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])

    line = Line("我的第一个图表", "这里是副标题")
    line.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])

    env = create_default_environment("html")
    # 为渲染创建一个默认配置环境
    # create_default_environment(filet_ype)
    # file_type: 'html', 'svg', 'png', 'jpeg', 'gif' or 'pdf'

    env.render_chart_to_file(bar, path='bar.html')
    env.render_chart_to_file(line, path='line.html')

def py_pie():
    x_data = ['裤子','鞋子','连衣裙']
    y_data = [100,130,200]
    p = Pie('饼图',title_pos='center',width=900)
    p.add('供应商A',x_data,y_data,center=[25,50],is_random=True, radius=[30,75],rosetype='radius')
    #p.add('供应商B',x_data,y_data,center=[75,50],is_random=True, radius=[30,75],rosetype='area',is_legend_show=False,is_lable_show=True)
    p.render()

def py_3d():
    bar3d = Bar3D("3D 柱状图示例", width=1200, height=600)
    x_axis = [
    "12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a",
    "12p", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p"
    ]
    y_axis = [
    "Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"
    ]
    data = [
    [0, 0, 5], [0, 1, 1], [0, 2, 0], [0, 3, 0], [0, 4, 0], [0, 5, 0],
    [0, 6, 0], [0, 7, 0], [0, 8, 0], [0, 9, 0], [0, 10, 0], [0, 11, 2],
    [0, 12, 4], [0, 13, 1], [0, 14, 1], [0, 15, 3], [0, 16, 4], [0, 17, 6],
    [0, 18, 4], [0, 19, 4], [0, 20, 3], [0, 21, 3], [0, 22, 2], [0, 23, 5],
    [1, 0, 7], [1, 1, 0], [1, 2, 0], [1, 3, 0], [1, 4, 0], [1, 5, 0],
    [1, 6, 0], [1, 7, 0], [1, 8, 0], [1, 9, 0], [1, 10, 5], [1, 11, 2],
    [1, 12, 2], [1, 13, 6], [1, 14, 9], [1, 15, 11], [1, 16, 6], [1, 17, 7],
    [1, 18, 8], [1, 19, 12], [1, 20, 5], [1, 21, 5], [1, 22, 7], [1, 23, 2],
    [2, 0, 1], [2, 1, 1], [2, 2, 0], [2, 3, 0], [2, 4, 0], [2, 5, 0],
    [2, 6, 0], [2, 7, 0], [2, 8, 0], [2, 9, 0], [2, 10, 3], [2, 11, 2],
    [2, 12, 1], [2, 13, 9], [2, 14, 8], [2, 15, 10], [2, 16, 6], [2, 17, 5],
    [2, 18, 5], [2, 19, 5], [2, 20, 7], [2, 21, 4], [2, 22, 2], [2, 23, 4],
    [3, 0, 7], [3, 1, 3], [3, 2, 0], [3, 3, 0], [3, 4, 0], [3, 5, 0],
    [3, 6, 0], [3, 7, 0], [3, 8, 1], [3, 9, 0], [3, 10, 5], [3, 11, 4],
    [3, 12, 7], [3, 13, 14], [3, 14, 13], [3, 15, 12], [3, 16, 9], [3, 17, 5],
    [3, 18, 5], [3, 19, 10], [3, 20, 6], [3, 21, 4], [3, 22, 4], [3, 23, 1],
    [4, 0, 1], [4, 1, 3], [4, 2, 0], [4, 3, 0], [4, 4, 0], [4, 5, 1],
    [4, 6, 0], [4, 7, 0], [4, 8, 0], [4, 9, 2], [4, 10, 4], [4, 11, 4],
    [4, 12, 2], [4, 13, 4], [4, 14, 4], [4, 15, 14], [4, 16, 12], [4, 17, 1],
    [4, 18, 8], [4, 19, 5], [4, 20, 3], [4, 21, 7], [4, 22, 3], [4, 23, 0],
    [5, 0, 2], [5, 1, 1], [5, 2, 0], [5, 3, 3], [5, 4, 0], [5, 5, 0],
    [5, 6, 0], [5, 7, 0], [5, 8, 2], [5, 9, 0], [5, 10, 4], [5, 11, 1],
    [5, 12, 5], [5, 13, 10], [5, 14, 5], [5, 15, 7], [5, 16, 11], [5, 17, 6],
    [5, 18, 0], [5, 19, 5], [5, 20, 3], [5, 21, 4], [5, 22, 2], [5, 23, 0],
    [6, 0, 1], [6, 1, 0], [6, 2, 0], [6, 3, 0], [6, 4, 0], [6, 5, 0],
    [6, 6, 0], [6, 7, 0], [6, 8, 0], [6, 9, 0], [6, 10, 1], [6, 11, 0],
    [6, 12, 2], [6, 13, 1], [6, 14, 3], [6, 15, 4], [6, 16, 0], [6, 17, 0],
    [6, 18, 0], [6, 19, 0], [6, 20, 1], [6, 21, 2], [6, 22, 2], [6, 23, 6]
    ]
    range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    bar3d.add("", x_axis, y_axis, [[d[1], d[0], d[2]] for d in data],
          is_visualmap=True, visual_range=[0, 20],
          visual_range_color=range_color, grid3d_width=200,
          grid3d_depth=80, is_grid3d_rotate=True)
    bar3d.render()


def up_down_left_right():
    '''
    Grid 类的使用

    引入 Grid 类，from pyecharts import Grid
    实例化 Grid 类，grid = Grid() ，可指定 page_title, width, height, jhost 参数。
    使用 add() 向 grid 中添加图，至少需要设置一个 grid_top, grid_bottom, grid_left, grid_right 四个参数中的一个
    grid_width 和 grid_height 一般不用设置，默认即可。
    使用 render() 渲染生成 .html 文件
    Note： Overlap 可类放入 Grid 类中，不过有个前提，Overlap 不可为多 x 轴或者多 y 轴，否则会出现坐标轴索引混乱问题

    Grid 类中其他方法：

    render_embed()：在 Flask&Django 中可以使用该方法渲染
    show_config()：打印输出所有配置项
    chart：chart 属性返回图形实例
    '''
    from pyecharts import Bar, Line, Scatter, EffectScatter, Grid
    
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar("柱状图示例",height="100%", width="100%", title_pos="65%",title_top="50%")
    bar.add("商家A", attr, v1)
    bar.add("商家B", attr, v2,legend_pos="80%")
    line = Line("折线图示例")
    attr = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    line.add(
        "最高气温",
        attr,
        [11, 11, 15, 13, 12, 13, 10],
        mark_point=["max", "min"],
        mark_line=["average"],
    )
    line.add(
        "最低气温",
        attr,
        [1, -2, 2, 5, 3, 2, 0],
        mark_point=["max", "min"],
        mark_line=["average"],
        legend_pos="20%",
    )
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    scatter = Scatter("散点图示例", title_top="50%", title_pos="65%")
    scatter.add("scatter", v1, v2, legend_top="50%", legend_pos="80%")
    es = EffectScatter("动态散点图示例", title_top="50%")
    es.add(
        "es",
        [11, 11, 15, 13, 12, 13, 10],
        [1, -2, 2, 5, 3, 2, 0],
        effect_scale=6,
        legend_top="50%",
        legend_pos="20%",
    )
    

    #pie
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [11, 12, 13, 10, 10, 10]
    pie = Pie("饼图示例", title_pos="55%")
    pie.add("",attr,v1,radius=[45, 65],center=[65, 50])

    grid = Grid()
    grid.add(bar, grid_bottom="60%", grid_left="60%")
    grid.add(line, grid_bottom="60%", grid_right="60%")
    #grid.add(scatter, grid_top="60%", grid_left="60%")
    #grid.add(es, grid_top="60%", grid_right="60%")
    grid.render()


#多个类型的图整合在一张图上 overlap
def bar_line():
    '''
    overlap 可以在一个图上整合多种图形
    用户可以自定义结合 Line/Bar/Kline, Scatter/EffectScatter 图表，将不同类型图表画在一张图上。利用第一个图表为基础，往后的数据都将会画在第一个图表上
    render_embed() ＃django flask 中进行渲染
    '''
    from pyecharts import Bar, Line, Overlap

    attr = ['A', 'B', 'C', 'D', 'E', 'F']
    v1 = [10, 20, 30, 40, 50, 60]
    v2 = [38, 28, 58, 48, 78, 68]
    bar = Bar("Line - Bar 示例")
    bar.add("bar", attr, v1)
    line = Line()
    line.add("line", attr, v2)

    overlap = Overlap()
    overlap.add(bar)
    overlap.add(line)
    overlap.render()

#利用page() 实现多种图表在同一页上
def put_one_page():
    from pyecharts import Page,Bar,Line,Pie
    page = Page()
    bar = Bar("我的第一个图表", "这里是副标题")
    bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])

    line = Line("我的第一个图表", "这里是副标题")
    line.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
    page.add(bar)
    page.add(line)
    page.render()
    
#grid的用法
def echart_grid():

    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar("柱状图示例", title_pos="60%")
    bar.add("商家A", attr, v1, is_stack=True, toolbox=False)
    bar.add("商家B", attr, v2, is_stack=True,  toolbox=False,  is_toolbox_show=False, legend_pos="70%")
    line = Line("折线图示例", title_pos="10%")
    attr = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    line.add(
        "最高气温",
        attr,
        [11, 11, 15, 13, 12, 13, 10],
        mark_point=["max", "min"],
        mark_line=["average"],
    )
    line.add(
        "最低气温",
        attr,
        [1, -2, 2, 5, 3, 2, 0],
        mark_point=["max", "min"],
        mark_line=["average"],
        is_toolbox_show=False,
        legend_pos="20%"
    )

    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    scatter = Scatter("散点图示例", title_top="450px", title_pos="10%")
    scatter.add("scatter", v1, v2, legend_top="50%", legend_pos="20%")
    es = EffectScatter("动态散点图示例", title_top="420px", title_pos="10%")
    es.add(
        "es",
        [11, 11, 15, 13, 12, 13, 10],
        [1, -2, 2, 5, 3, 2, 0],
        effect_scale=6,
        legend_top="420px",
        legend_pos="20%",
    )

    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [11, 12, 13, 10, 10, 10]
    pie = Pie("饼图示例", title_top="800px", title_pos="10%")
    pie.add(
        "",
        attr,
        v1,
        radius=[20, 30],
        center=[20, 85],
        legend_pos="40%",
        legend_orient="vertical", #配置竖型备注信息 attr属性竖型分布
        legend_top="830px",
    )

    #overlap 的使用，结合不同类型的图表叠加画在同张图上
    attr = ['A', 'B', 'C', 'D', 'E', 'F']
    v1 = [10, 20, 30, 40, 50, 60]
    v2 = [38, 28, 58, 48, 78, 68]
    bar_overlap = Bar("Line-Bar overlap", title_top="420px",title_pos="60%")
    bar_overlap.add("bar", attr, v1, is_toolbox_show=False, legend_top="420px", legend_pos="70%")
    line_overlap = Line()
    line_overlap.add("line", attr, v2, is_toolbox_show=False)

    overlap = Overlap()
    overlap.add(bar_overlap)
    overlap.add(line_overlap)

    grid = Grid(page_title="Python", width="100%", height="1200px")
    grid.add(bar,  grid_left="55%", grid_height="300px")
    grid.add(line, grid_right="55%", grid_height="300px")
    grid.add(es, grid_top="460px", grid_right="55%", grid_height="300px")
    grid.add(overlap, grid_top="460px", grid_left="55%", grid_height="300px")
    grid.add(pie, grid_top="800px", grid_right="55%", grid_height="300px")
    grid.render()

#page的用法
def echart_page():
    '''
    同一页面按顺序展示多图
    Grid/Timeline/Overlap 都可在 Page 中正常展示，把其当做一个图加入到 Page 中即可
    引入 Page 类，from pyecharts import Page
    实例化 Page 类，page = Page() ，可指定 page_title, jhost 参数。
    使用 add() 向 page 中添加图，可以是单个图实例，也可以是一个图实例列表。
    使用 render() 渲染生成 .html 文件
    render_embed() 在 Flask&Django 中可以使用该方法渲染
    '''

    page = Page()  # step 1

    # bar
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar("柱状图数据堆叠示例")
    bar.add("商家A", attr, v1, is_stack=True)
    bar.add("商家B", attr, v2, is_stack=True, is_toolbox_show=False)
    page.add(bar)  # step 2

    # scatter3D
    import random
    data = [
        [random.randint(0, 100),
         random.randint(0, 100),
         random.randint(0, 100)] for _ in range(80)
    ]
    range_color = [
        '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
        '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    scatter3D = Scatter3D("3D 散点图示例", width=1200, height=600)
    scatter3D.add("", data, is_visualmap=True, visual_range_color=range_color, is_toolbox_show=False)
    page.add(scatter3D)  # step 2

    page.render('echart_page.html')  # step 3

if __name__ == '__main__':
    up_down_left_right()
