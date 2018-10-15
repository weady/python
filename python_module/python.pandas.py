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
print df.ix[:, 0].head() ix[行,列] 读取指定的行列数据, head() 默认读取前5行
df.drop(df.columns[[1, 2]], axis = 1).head() 删除指定的列
bric = pd.read_excel('/usr/test.xlsx') 处理xlsx文件
print bric.loc['Br'] #读取行用函数.loc,但显示是以列显示的
#显示'Br'这行的'language'的值有下面几种方法：
  1.一起选择
    print bric.loc['Br','language']
  2.取列再取行
    print bric['language'].loc['Br']
  3.取行再取列
    print bric.loc['Br']['language']
  4.值就直接['列名']
    print bric['language']
插入列：直接bric['要插入的列名']=[要插入的列表数据] ric['aa']=['123','kk','123','mm']
#插入行：bric.loc['Afric']=[25,20,'english','aa']
数据清洗
loandata=pd.DataFrame(pd.read_excel('loandata.xlsx'))
1.数据表中的重复值
  	loandata.duplicated() 判断重复值
    loandata.drop_duplicates() 删除重复值
2.数据表中的空值/缺失值
  loandata.isnull() 空值 loandata['列名'].isnull().value_counts() #统计某个列的非空值数量
  loandata.notnull() 非空值
  空值有两种处理的方法，第一种是使用fillna函数对空值进行填充，可以选择填充0值或者其他任意值。第二种方法是使用dropna函数直接将包含空值的数据删除
  loandata.fillna(0) 填充空值
  loandata.dropna() 删除空值
3.数据间的空格
  loandata['term']=loandata['term'].map(str.strip) 利用strip 进行清查数据间的空格
  loandata['term']=loandata['term'].map(str.upper) 大写
  loandata['term']=loandata['term'].map(str.lower) 小写
  loandata['term']=loandata['term'].map(str.title) 首字母大写
  loandata['emp_length'].apply(lambda x: x. isalnum ())判断是否是数字
  loandata['emp_length'].apply(lambda x: x. isdigit ())
  loandata['emp_length'].apply(lambda x: x.isalpha())
4更改数据格式
  loandata['loan_amnt']=loandata['loan_amnt'].astype(np.int64)
6.数据分组
  bins = [0, 5, 10, 15, 20]
  group_names = ['A', 'B', 'C', 'D']
  loandata['categories'] = pd.cut(loandata['open_acc'], bins, labels=group_names)
  对某一列的值进行等级分类
7.数据分列
  grade_split = pd.DataFrame((x.split('-') for x in loandata.grade),index=loandata.index,columns=['grade','sub_grade']) 指定分列的数据行所有保持不变
  loandata=pd.merge(loandata,grade_split,right_index=True, left_index=True) 合并数据
