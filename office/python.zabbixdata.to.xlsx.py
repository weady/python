#!/usr/bin/env python
#-*- encoding: UTF-8 -*-

#这个脚本主要是从zabbix监控数据库中获取出数据然后生成具体的图形报表

import sys, os, re, time
try:
    import MySQLdb, xlsxwriter
except:
    print "Can't import module MySQLdb or xlsxwriter. Please execute shell script install_pymodule_xlsxwriter_mysqldb.sh first."
    sys.exit(1)

class db_sql(object):

        def __init__(self,user,passwd,host,db_name):

            self.user = user
            self.passwd = passwd
            self.host = host
            self.db_name = db_name

        def db_deal_data(self,sql,param=0):
            '''
            定义了数据库查询和插入的方法
            @sql 是传入的sql语句
            @param 是在进行批量插入数据时，传入的数据列表或元组
            '''
            self.sql = sql
            self.param = param

            db = MySQLdb.connect(self.host,self.user,self.passwd,self.db_name,charset='utf8')
            #cursor()方法获取操作游标
            cursor = db.cursor()
            if param:
                try:
                    cursor.executemany(sql,param) #使用executemany 批量插入数据,param为列表或元组类型
                    db.commit()
                    return "数据插入成功"
                except Exception,e:
                    db.rollback()
                    return str(e)
                finally:
                    db.close()  
            else:
                cursor.execute(sql) #执行单条sql语句，得到查询结果并返回
                result = cursor.fetchall()
                cursor.close()
                return result  


class CustomizationXLSX(object):
    def __init__(self,filename):
        self.workbook = xlsxwriter.Workbook(filename,{"strings_to_numbers":True})

    def disconnect(self,status,info,end=True):
        if end:
            self.workbook.close()
        return {'result':status,'result_info':info}

    def add_sheet(self,sheetname):
        self.worksheet = self.workbook.add_worksheet(sheetname)
        
    def define_format(self,format_name,**kwargs):
        self.format_name = self.workbook.add_format(kwargs)
        
    def fun_trans(self,num):
            list_a = range(26)
            list_b = range(ord('A'),ord('Z')+1)
            if num < 26:
                ind = list_a.index(num)
                result = chr(list_b[ind])
            else:
                num_1 = (num)%26
                num_2 = (num)/26
                ind = list_a.index(num_1)
                result = self.fun_trans(num_2-1)+chr(list_b[ind])
            return result

    def insert_value(self,value,valuetype="",*args,**kwargs):
        if kwargs.has_key('pos_col') and kwargs.has_key('pos_row'):
            position = self.fun_trans(kwargs['pos_col'])+str(kwargs['pos_row'])
            kwargs.pop('pos_row')
            kwargs.pop('pos_col')
        else:
            if not kwargs.has_key('position'):
                return self.disconnect(False,"Invalidate value with position.")
            position = kwargs['position']
            kwargs.pop('position')

        if not valuetype:
            self.worksheet.write(position,"%s" % value,args[0]) if args else self.worksheet.write(position,"%s" % value)
        elif valuetype == "string":
            self.worksheet.write_string(position,"%s" % value,args[0]) if args else self.worksheet.write_string(position,"%s" % value)
        elif valuetype == "number":
            self.worksheet.write_number(position,"%s" % value,args[0]) if args else self.worksheet.write_number(position,"%s" % value)
        elif valuetype == "blank":
            self.worksheet.write_blank(position,"%s" % value,args[0]) if args else self.worksheet.write_blank(position,"%s" % value)
        elif valuetype == "formula":
            self.worksheet.write_formula(position,"%s" % value,args[0]) if args else self.worksheet.write_formula(position,"%s" % value)
        elif valuetype == "datetime":
            self.worksheet.write_datetime(position,"%s" % value,args[0]) if args else self.worksheet.write_datetime(position,"%s" % value)
        elif valuetype == "boolean":
            self.worksheet.write_boolean(position,"%s" % value,args[0]) if args else self.worksheet.write_boolean(position,"%s" % value)
        elif valuetype == "url":
            self.worksheet.write_url(position,"%s" % value,args[0]) if args else self.worksheet.write_url(position,"%s" % value)
        elif valuetype == "image":
            self.worksheet.insert_image(position,"%s" % value,kwargs) if kwargs else self.worksheet.insert_image(position,"%s" % value)
        else:
            return self.disconnect(False,"Invalidate value with value type.")

        return self.disconnect(True,"",False)

    def set_property(self,positiontype,position,precision,custom_format,**kwargs):
        if len(position.split(":")) > 2 or len(position.split(":")) < 1:
            return self.disconnect(False,"Invalidate value with position.")
        else:
            for ele in position.split(":"):
                if positiontype == "column" and not ele.isalpha() :
                    return self.disconnect(False,"Invalidate value with position.")
                elif positiontype == "row" and not ele.isdigit():
                    return self.disconnect(False,"Invalidate value with position.")

        if positiontype == "column":
            self.worksheet.set_column(position,precision,custom_format,kwargs)
        elif positiontype == "row":
            self.worksheet.set_row(position,precision,custom_format,kwargs)
        else:
            return False
        return True

    def create_chart(self,set_type,data_dict,set_pos,set_sheetname,pos_sheetname,y_unit,sheet_title,size='normal'):
        if not data_dict:
            return False
        try:
            newchart = self.workbook.add_chart({'type': set_type})
            for key in data_dict.keys():
                for value in data_dict[key]:
                    newchart.add_series({
                        'categories': '=%s!%s:%s' %(set_sheetname,key[0],key[1]),
                        'values': '=%s!%s:%s' %(set_sheetname,value[1],value[2]),
                        #'data_labels': {'value': True,'position': 'center'},
                        'name': value[0],
                        })
            if size == 'normal':
                newchart.set_size({'width': 1000, 'height': 576})
            elif size == 'small':
                newchart.set_size({'width': 550, 'height': 338})
            newchart.set_title({'name': sheet_title})
            newchart.set_y_axis({'name': u'单位（%s）' % y_unit})
            if not pos_sheetname in self.workbook.sheetnames.keys():
                self.add_sheet(pos_sheetname)
            self.workbook.get_worksheet_by_name(pos_sheetname).insert_chart(set_pos, newchart)
        except Exception,e:
            print e
            return False

def query_detail_data(time_start,time_end,item_key, query_table, time_step, use_jin=False, query_key="clock,value"):
    global database_sql
    data_dict = {}
    key_list = []
    start_time = time.mktime(time.strptime(time_start,"%Y-%m-%d %H:%M:%S"))
    end_time = time.mktime(time.strptime(time_end,"%Y-%m-%d %H:%M:%S"))
    sql_01 = "select itemid from items where key_=\"%s\" and templateid is not NULL;" % item_key
    if use_jin:
        sql_01 = "select itemid from items where key_=\"%s\";" % item_key
    tmp_result = database_sql.db_deal_data(sql_01)
    if tmp_result and tmp_result[0]:
        item_id = tmp_result[0][0]
    else:
        return False,False
    sql_02 = "select %s from %s where clock >= %d and clock <= %d and itemid = \"%d\";" %(query_key,query_table,start_time,end_time,item_id)
    result = database_sql.db_deal_data(sql_02)
    result = list(result)
    if result and result[0]:
        tmp_start_time = start_time
        tmp_end_time = start_time + time_step - 1
        while tmp_end_time < end_time+1200:
            result_sub_list = []
            for ele in result:
                if ele[0] >= tmp_start_time and ele[0] <= tmp_end_time:
                    result_sub_list.append(ele)
            if result_sub_list:
                tmp_list = [sum(x[y] for x in result_sub_list)/len(result_sub_list) for y in range(len(result_sub_list[0]))]
                local_time = time.strftime('%H:%M:%S',time.localtime(tmp_list[0]))
                key_list.append(local_time)
                data_dict[local_time]=tmp_list[1:]
            tmp_start_time += time_step
            tmp_end_time += time_step
    return key_list,data_dict

def auto_create_xlsx(xlsxfile,set_sheetname,key_list,data,index_list,init_pos):
    if not data:
        return False,False
    if not set_sheetname in xlsxfile.workbook.sheetnames.keys():
        xlsxfile.add_sheet(set_sheetname)
    else:
        xlsxfile.workbook.get_worksheet_by_name(set_sheetname)
    pos_start = xlsxfile.fun_trans(1+init_pos[0])
    pos_end = xlsxfile.fun_trans(len(key_list)+init_pos[0])
    insert_pos_list = []
    tmp_length = 1
    for ele in index_list:
        tmp_length += 1
    try:
        for i in range(1,len(key_list)+1):
            xlsxfile.insert_value(value=key_list[i-1],pos_row=init_pos[1]+1,pos_col=init_pos[0]+i)
            tmp_pos_row = init_pos[1] + 2
            for ele in data[key_list[i-1]]:
                xlsxfile.insert_value(value="%.2f"% ele,pos_row=tmp_pos_row,pos_col=init_pos[0]+i)
                if i == 1 :
                    if len(index_list) > tmp_pos_row-2-init_pos[1]:
                        xlsxfile.insert_value(value=index_list[tmp_pos_row-2-init_pos[1]],pos_row=tmp_pos_row,pos_col=init_pos[0]+0)
                        insert_pos_list.append([index_list[tmp_pos_row-2-init_pos[1]],pos_start+str(tmp_pos_row),pos_end+str(tmp_pos_row)]) 
                tmp_pos_row += 1
    except Exception,e:
        print e
    insert_data_dict = {(pos_start+str(init_pos[1]+1),pos_end+str(init_pos[1]+1)):insert_pos_list}
    return (tmp_length,insert_data_dict)

def main(start_time,end_time):
    anoymous_func = lambda x: "".join(["%02d" % int(i) for i in x.split("-")])
    filename_brief = "/usr/local/zabbix/Brief_report_data_%s_%s.xlsx" %("".join(start_time.split("-")[1:]),"".join(end_time.split("-")[1:]))
    filename_detail = "/usr/local/zabbix/Detail_report_data_%s_%s.xlsx" %("".join(start_time.split("-")[1:]),"".join(end_time.split("-")[1:]))
    if os.path.isfile("/usr/local/zabbix/etc/zabbix_server.conf"):
        db_host = os.popen("egrep \"^DBHost=\" /usr/local/zabbix/etc/zabbix_server.conf").readlines()[0].strip().split("=")[1]
        db_username = "zabbix"
        db_passwd = "zabbixpass"
        db_dbname = "zabbix"
    else:
        print "Failed to get zabbix information from /usr/local/zabbix/etc/zabbix_server.conf."
        return False
    global database_sql
    database_sql = db_sql(db_username,db_passwd,db_host,db_dbname)
    local_date = time.strftime("%Y-%m-%d",time.localtime())
    for tmp_date in [start_time,end_time]:
        try:
            tmp_result = time.strptime(tmp_date,"%Y-%m-%d")
            database_sql.db_deal_data("show variables;")
        except Exception,e:
            print "With invalidate date format, or failed to connect with MySQL server."
            print e
            return False
    if (anoymous_func(start_time) > anoymous_func(end_time)) or (anoymous_func(local_date) <= anoymous_func(end_time)):  return False
    date_zone = " "+start_time+"/"+end_time
    start_time += " 00:00:00"
    end_time += " 23:59:59"
    kk = lambda x: x/1024/float(1024)
    is_err = 0
    cluster_dict={
        u"Device[smartcard] 集群并发推流下载总量":"cluster.sum[smartcard,d]",
        u"Device[stb] 集群并发推流电影总量":"cluster.sum[stb,movie]",
        u"Device[total] 集群并发推流总量":"cluster.sum[total,total]",
        u"Device[stb] 集群并发推流时移总量":"cluster.sum[stb,ts_total]",
        u"Device[pad] 集群并发推流一键时移总量":"cluster.sum[pad,kts]",
        u"Device[total] 集群并发推流普通时移总量":"cluster.sum[total,ts]",
        u"Device[total] 集群并发推流下载总量":"cluster.sum[total,d]",
        u"Device[smartcard] 集群并发推流电影总量":"cluster.sum[smartcard,movie]",
        u"Device[mobile] 集群并发推流普通时移总量":"cluster.sum[mobile,ts]",
        u"Device[mobile] 集群并发推流一键时移总量":"cluster.sum[mobile,kts]",
        u"Device[total] 集群并发推流一键时移总量":"cluster.sum[total,kts]",
        u"Device[mobile] 集群并发推流直播总量":"cluster.sum[mobile,live]",
        u"Device[mobile] 集群并发推流电影总量":"cluster.sum[mobile,movie]",
        u"Device[stb] 集群并发推流直播总量":"cluster.sum[stb,live]",
        u"Device[smartcard] 集群并发推流直播总量":"cluster.sum[smartcard,live]",
        u"Device[pc] 集群并发推流下载总量":"cluster.sum[pc,d]",
        u"Device[pc] 集群并发推流电影总量":"cluster.sum[pc,movie]",
        u"Device[pad] 集群并发推流下载总量":"cluster.sum[pad,d]",
        u"Device[total] 集群并发推流电影总量":"cluster.sum[total,movie]",
        u"Device[pad] 集群并发推流回看总量":"cluster.sum[pad,tr]",
        u"Device[stb] 集群并发推流一键时移总量":"cluster.sum[stb,kts]",
        u"Device[total] 集群并发推流直播总量":"cluster.sum[total,live]",
        u"Device[pc] 集群并发推流回看总量":"cluster.sum[pc,tr]",
        u"Device[stb] 集群并发推流普通时移总量":"cluster.sum[stb,ts]",
        u"Device[stb] 集群并发推流回看总量":"cluster.sum[stb,tr]",
        u"Device[mobile] 集群并发推流下载总量":"cluster.sum[mobile,d]",
        u"Device[pad] 集群并发推流直播总量":"cluster.sum[pad,live]",
        u"Device[pc] 集群并发推流一键时移总量":"cluster.sum[pc,kts]",
        u"Device[stb] 集群并发推流下载总量":"cluster.sum[stb,d]",
        u"Device[pc] 集群并发推流普通时移总量":"cluster.sum[pc,ts]",
        u"Device[smartcard] 集群并发推流时移总量":"cluster.sum[smartcard,ts_total]",
        u"Device[mobile] 集群并发推流回看总量":"cluster.sum[mobile,tr]",
        u"Device[smartcard] 集群并发推流回看总量":"cluster.sum[smartcard,tr]",
        u"Device[pc] 集群并发推流直播总量":"cluster.sum[pc,live]",
        u"Device[mobile] 集群并发推流时移总量":"cluster.sum[mobile,ts_total]",
        u"Device[mobile] 集群并发推流总量":"cluster.sum[mobile,total]",
        u"Device[smartcard] 集群并发推流总量":"cluster.sum[smartcard,total]",
        u"Device[smartcard] 集群并发推流一键时移总量":"cluster.sum[smartcard,kts]",
        u"Device[pad] 集群并发推流电影总量":"cluster.sum[pad,movie]",
        u"Device[total] 集群并发推流时移总量":"cluster.sum[total,ts_total]",
        u"Device[pc] 集群并发推流总量":"cluster.sum[pc,total]",
        u"Device[pad] 集群并发推流普通时移总量":"cluster.sum[pad,ts]",
        u"Device[total] 集群并发推流回看总量":"cluster.sum[total,tr]",
        u"Device[smartcard] 集群并发推流普通时移总量":"cluster.sum[smartcard,ts]",
        u"Device[pc] 集群并发推流时移总量":"cluster.sum[pc,ts_total]",
        u"Device[pad] 集群并发推流总量":"cluster.sum[pad,total]",
        u"Device[pad] 集群并发推流时移总量":"cluster.sum[pad,ts_total]",
        u"Device[stb] 集群并发推流总量":"cluster.sum[stb,total]",
        u"每天新增用户":"cluster.reg_online[register_day_num]",
        u"注册用户总数":"cluster.reg_online[register_sum_num]",
        u"mobile设备实时在线用户总数":"monitor.online[mobile_all]",
        u"pad设备实时在线用户总数":"monitor.online[pad_all]",
        u"pc设备实时在线用户总数":"monitor.online[pc_all]",
        u"stb设备实时在线用户总数":"monitor.online[stb_all]",
        u"实时在线用户总数":"monitor.online[device_all]",
        u"推流总带宽趋势统计":"zabbix.data[get_push_bandwith]",}
    device_total_list=[
        u"Device[total] 集群并发推流总量",
        u"Device[total] 集群并发推流电影总量",
        u"Device[total] 集群并发推流直播总量",
        u"Device[total] 集群并发推流回看总量",
        ]
    device_mobile_list = [
        u"Device[mobile] 集群并发推流总量",
        u"Device[mobile] 集群并发推流电影总量",
        u"Device[mobile] 集群并发推流直播总量",
        u"Device[mobile] 集群并发推流回看总量",
        ]
    device_pad_list=[
        u"Device[pad] 集群并发推流总量",
        u"Device[pad] 集群并发推流电影总量",
        u"Device[pad] 集群并发推流直播总量",
        u"Device[pad] 集群并发推流回看总量",
        ]
    device_pc_list=[
        u"Device[pc] 集群并发推流总量",
        u"Device[pc] 集群并发推流电影总量",
        u"Device[pc] 集群并发推流直播总量",
        u"Device[pc] 集群并发推流回看总量",
        ]
    device_smartcard_list=[
        u"Device[smartcard] 集群并发推流总量",
        u"Device[smartcard] 集群并发推流电影总量",
        u"Device[smartcard] 集群并发推流直播总量",
        u"Device[smartcard] 集群并发推流回看总量",
        ]
    device_stb_list=[
        u"Device[stb] 集群并发推流总量",
        u"Device[stb] 集群并发推流电影总量",
        u"Device[stb] 集群并发推流直播总量",
        u"Device[stb] 集群并发推流回看总量",
        ]
    query_all_list = [
        u"注册用户总数",
        u"推流总带宽趋势统计",
        u"Device[total] 集群并发推流总量",
        u"Device[mobile] 集群并发推流总量",
        u"Device[pad] 集群并发推流总量",
        u"Device[pc] 集群并发推流总量",
        u"Device[smartcard] 集群并发推流总量",
        u"Device[stb] 集群并发推流总量",
        u"实时在线用户总数",
        u"mobile设备实时在线用户总数",
        u"pad设备实时在线用户总数",
        u"pc设备实时在线用户总数",
        u"stb设备实时在线用户总数",
        ]
    device_all_total_list = [
        u"Device[total] 集群并发推流总量",
        u"Device[mobile] 集群并发推流总量",
        u"Device[pad] 集群并发推流总量",
        u"Device[pc] 集群并发推流总量",
        u"Device[smartcard] 集群并发推流总量",
        u"Device[stb] 集群并发推流总量",
        ]
    monitor_all_online_list = [
        u"实时在线用户总数",
        u"stb设备实时在线用户总数",
        u"mobile设备实时在线用户总数",
        u"pc设备实时在线用户总数",
        u"pad设备实时在线用户总数",
        ]

    newxlsx = CustomizationXLSX(filename_detail)
    y_pos = 0
    key_list,data = query_detail_data(start_time,end_time,"cluster.reg_online[register_sum_num]", "history_uint", 1200,query_key="clock,value")
    if not data:
        print "Failed to query data about  cluster.reg_online[register_sum_num]."
        is_err = 1
    else:
        (tmp_length,tmp_insert_data_dict) = auto_create_xlsx(newxlsx,u"用户数统计",key_list,data,[u"注册用户总数"],[0,y_pos])
        y_pos += (tmp_length+3)
        newxlsx.set_property("column","A:A",28,None)
        newxlsx.create_chart('line',tmp_insert_data_dict,'A'+str(y_pos),u"用户数统计",u"用户数统计",u"个",u"注册用户总数"+date_zone)
        y_pos += 30

    for ele in monitor_all_online_list:
        key_list,data = query_detail_data(start_time,end_time,cluster_dict[ele],"history_uint", 1200)
        if not data:
            print "Failed to query data about  %s." % (cluster_dict[ele])
            is_err = 1
        else:
            (tmp_length,tmp_insert_data_dict) = auto_create_xlsx(newxlsx,u"用户数统计",key_list,data,[ele],[0,y_pos])
            y_pos += (tmp_length+3)
            newxlsx.set_property("column","A:A",19,None)
            newxlsx.create_chart('line',tmp_insert_data_dict,'A'+str(y_pos),u"用户数统计",u"用户数统计",u"个",ele+date_zone)
            y_pos += 30


    key_list,data = query_detail_data(start_time,end_time,"zabbix.data[get_push_bandwith]", "history_uint", 1200)
    if not data:
        print "Failed to query data about  zabbix.data[get_push_bandwith]."  
        is_err = 1 
    else:
        for i in key_list:
            tmp_list = []
            for ele in data[i]:
                tmp_list.append(kk(ele))
            data[i] = tmp_list
        (tmp_length,tmp_insert_data_dict) = auto_create_xlsx(newxlsx,u"推流总带宽趋势统计",key_list,data,[u"推流总带宽趋势统计"],[0,0])
        newxlsx.set_property("column","A:A",10,None)
        newxlsx.create_chart('line',tmp_insert_data_dict,'A'+str(3+tmp_length),u"推流总带宽趋势统计",u"推流总带宽趋势统计","Mbytes",u"推流总带宽趋势统计"+date_zone)

    key_list,data = query_detail_data(start_time,end_time,"hdfs.resource[dfs.pused]", "history", 1200)
    if not data:
        print "Failed to query data about  hdfs.resource[dfs.pused]."   
        is_err = 1
    else:
        (tmp_length,tmp_insert_data_dict) = auto_create_xlsx(newxlsx,u"HDFS使用率",key_list,data,[u"HDFS使用率"],[0,0])
        newxlsx.set_property("column","A:A",11,None)
        newxlsx.create_chart('line',tmp_insert_data_dict,'A'+str(3+tmp_length),u"HDFS使用率",u"HDFS使用率","%",u"HDFS使用率"+date_zone)


    for sub_list in [device_total_list,device_mobile_list,device_pad_list,device_pc_list,device_smartcard_list,device_stb_list]:
        tmp_sheetname = re.split('[\[\]]',sub_list[0].split(" ")[0])[1]+u"集群并发推流量"
        insert_data_dict = {}
        y_pos = 0
        for key in sub_list:
            key_list,data = query_detail_data(start_time,end_time,cluster_dict[key], "history_uint", 1200, use_jin=True)
            if not data:
                print "Failed to query data about  %s." % cluster_dict[key]  
                is_err = 1
                sub_list.remove(key)
            else:
                (tmp_length,tmp_insert_data_dict) = auto_create_xlsx(newxlsx,tmp_sheetname,key_list,data,[key],[0,y_pos])
                y_pos += tmp_length
                insert_data_dict[key]=tmp_insert_data_dict
                newxlsx.set_property("column","A:A",41,None)
        y_pos += 3
        for key in sub_list:
            if key in insert_data_dict.keys():
                newxlsx.create_chart('line',insert_data_dict[key],'A'+str(y_pos),tmp_sheetname,tmp_sheetname," ",key+date_zone)
                y_pos += 30
            else:
                print "Failed to get data from xlsx file."
                is_err = 1
    newxlsx.disconnect(True,"")


    newxlsx = CustomizationXLSX(filename_brief)
    newxlsx.add_sheet(u"数据图表展示")
    newxlsx.add_sheet(u"数据内容来源")
    data_y_pos = 0
    insert_data_dict = {}
    for query_key in query_all_list :
        use_jin = False if query_key in [u"注册用户总数",u"推流总带宽趋势统计"]+monitor_all_online_list else True
        key_list,data = query_detail_data(start_time,end_time,cluster_dict[query_key], "trends_uint", 3600, use_jin=use_jin,query_key="clock,value_avg")
        if not data:
            print "@@Failed to query data about %s." % cluster_dict[query_key]  
            is_err = 1
            tmp_length,tmp_insert_data_dict = 0,False
        else:
            if query_key == u'推流总带宽趋势统计':
                for i in key_list:
                    tmp_list = []
                    for ele in data[i]:
                        tmp_list.append(kk(ele))
                    data[i] = tmp_list
            (tmp_length,tmp_insert_data_dict) = auto_create_xlsx(newxlsx,u"数据内容来源",key_list,data,[query_key],[0,data_y_pos])
        if query_key in device_all_total_list:
            try:
                insert_data_dict[u'集群并发推流总量'].update(tmp_insert_data_dict)
            except:
                insert_data_dict[u'集群并发推流总量'] = tmp_insert_data_dict
        elif query_key in monitor_all_online_list:
            try:
                insert_data_dict[u'分平台实时在线总人数'].update(tmp_insert_data_dict)
            except:
                insert_data_dict[u'分平台实时在线总人数'] = tmp_insert_data_dict
        else:
            insert_data_dict[query_key] = tmp_insert_data_dict
        data_y_pos += tmp_length

    newxlsx.set_property("column","A:A",44,None)

    chart_y_pos = '1'
    chart_x_pos = 'A'
    anoymous_func = lambda x,y: ('A',str(int(y)+18)) if x == 'J' else ('J',y)
    for query_key in query_all_list :
        if query_key in device_all_total_list or query_key in monitor_all_online_list: continue
        display_unit = "Mbytes" if query_key == u'推流总带宽趋势统计' else u"个"
        newxlsx.create_chart('line',insert_data_dict[query_key],chart_x_pos+chart_y_pos,u"数据内容来源",u"数据图表展示",display_unit,query_key+date_zone,size='small')
        chart_x_pos,chart_y_pos = anoymous_func(chart_x_pos,chart_y_pos)
    newxlsx.create_chart('line',insert_data_dict[u'集群并发推流总量'],chart_x_pos+chart_y_pos,u"数据内容来源",u"数据图表展示",u"个",u'集群并发推流总量'+date_zone,size='small')
    chart_x_pos,chart_y_pos = anoymous_func(chart_x_pos,chart_y_pos)
    newxlsx.create_chart('line',insert_data_dict[u'分平台实时在线总人数'],chart_x_pos+chart_y_pos,u"数据内容来源",u"数据图表展示",u"个",u'分平台实时在线总人数'+date_zone,size='small')
        
    newxlsx.disconnect(True,"")

    if is_err == 1:
        return 2
    return True

if __name__ == '__main__':
    if len(sys.argv) < 3 :
        if len(sys.argv) > 1:
            if sys.argv[1] != "auto":
                print "Failed with less variables."
                sys.exit(1)
        else:
            print "Failed with less variables."
            sys.exit(1)

    if sys.argv[1] == "auto":
        start_time = time.strftime("%Y-%m-%d",time.localtime(time.time()-3600*24))
        end_time = time.strftime("%Y-%m-%d",time.localtime(time.time()-3600*24))
    else:
        start_time = sys.argv[1]
        end_time = sys.argv[2]
    tmp_result = main(start_time,end_time)
    if tmp_result == 2:
        sys.exit(2)
    elif not tmp_result:
        sys.exit(1)