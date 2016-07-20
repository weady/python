#!/usr/bin/python
#-*-coding:utf8-*-
#   by wangdd 2016/07/20
#
#   实现从excel文件中读取数据,然后插入的数据库中

import xlrd
import sys
import MySQLdb

reload(sys)
sys.setdefaultencoding('utf8')
    
    #xlrd模块读取excel文件的基础知识

    #打开一个excel文件
    #data = xlrd.open_workbook('auto_operation.xlsx')

    #table = data.sheets()[0] #通过索引顺序获取一个工作表

    #table = data.sheet_by_index(0) #通过索引顺序获取一个工作表

    #table = data.sheet_by_name(u'sheet1') #通过名字获取

    #table.row_values(i) #获取整行的值
    #table.col_values(i) #获取整列的值

    #nrows = table.nrows #获取行数
    #ncols = table.ncols #获取列数

    #循环行列表数据
    #for i in range(nrows):
        #print table.row_values(i)

    #使用行列索引

    #cell_A1 = table.row(0)[0].value
    #cell_A2 = table.col(1)[0].value 


#打开excel文件函数
def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

#根据名称获取excel表格中的数据 参数:file excel文件名 colnameindex 表头列名所在行的索引  sheet_name:sheet的名称

def excel_data_byname(file,sheet_name):
    data = open_excel(file)
    table = data.sheet_by_name(sheet_name)
    nrows = table.nrows #行数 
    colnameindex = 0
    colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(1,nrows):
        row = table.row_values(rownum)
        if row:
            list.append(row)
            #为每一个行数据加上对应的列标识
            #app = {}
            #for i in range(len(colnames)):
            #    app[colnames[i]] = row[i]
            #list.append(app)
    return list

def data_to_db():
    user="root"
    db_name="auto_operation"
    passwd="xxxxx"
    host="xxxxxx"
    db = MySQLdb.connect(host,user,passwd,db_name,charset='utf8')
    #cursor()方法获取操作游标
    cursor = db.cursor()
    server_list_sql = '''
        insert into t_service_distribution(cluster_name,server_name,hostname,server_id,status,note,server_function) 
        value(%s,%s,%s,%s,%s,%s,%s)
    '''
    host_info_sql = '''
        insert into t_host_info value(%s,%s,%s,%s,%s,%s,%s)
    '''
    #从excle文件中读取出信息，然后插入到数据库中
    file = sys.argv[1]
    sheet_name = sys.argv[2]
    if file and sheet_name:
        param = excel_data_byname(file,sheet_name)
    
    try:
        #cursor.execute(sql) #执行单条sql语句
        if sheet_name == "server_list":
            cursor.executemany(server_list_sql,param) #使用executemany 批量插入数据,param为列表或元组类型
            db.commit()
        if sheet_name == "host_info":
            cursor.executemany(host_info_sql,param)
            db.commit()
    except Exception,e:
        db.rollback()
        print str(e)
    db.close()

def main():
    data_to_db()


if __name__ == "__main__":
    main()

