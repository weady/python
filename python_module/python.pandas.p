Pandas使用一个二维的数据结构DataFrame来表示表格式的数据
DataFrame有四个重要的属性： 
index：行索引。 
columns：列索引。 
values：值的二维数组。 
name：名字
data = pd.DataFrame(rec, columns = [u"姓名",u"业绩" ])
DataFrame方法函数的第一个参数是数据源，第二个参数columns是输出数据表的表头，或者说是表格的字段名
DataFrame(sequence)，通过序列构建，序列中的每个元素是一个字典
data.groupby([u'业绩']).sum() 以业务为分组统计某一列的总和size()：就是count  sum()：分组求和 
导出数据csvdata.to_csv(u"D:\scripts\learn\Result.csv", index= True, header=[u'雇员', u'销售业绩'], encoding="utf_8_sig")
解决保存csv文件后，中文乱码问题。encoding="utf_8_sig"
Sorted = data.sort_values([u"业绩"], ascending=False) 以某列进行排序，然后取前几的值 Sorted.head(3)
pd.read_csv('f:\1024.csv') 读取CSV文件
print df.head() 读取前几行数据,默认5
print df.dtypes 读物数据类型
print df.describe(include='all')  读取统计信息
print df.columns 打印出列的信息
print df.index 打印出行的索引信息
print df.T 行列互置
