import sqlite3

"""建立数据库并将文件中的数据导入数据库中"""

# 使用connect()函数创建连接对象con，同时创建一个数据库test
con = sqlite3.connect('test')
# 使用连接对象con方法 cursor()函数创建游标对象curs
curs = con.cursor()
# 使用游标对象方法execute()创建表格phone
curs.execute('''
create table phone(
name char(10),
tel char(11),
id char(6),
high char(3),
weight float)''')

# 进入文件data.txt(/Users/junliliu/Desktop/data.txt)将文件中的行导入数据库中
file = '/Users/junliliu/Desktop/data.txt'
query = 'insert into phone values(?,?,?,?,?)'  # 导入数据库数据语句
with open(file) as f:
    line_number = 0
    for line in f:
        if line_number == 0:
            line_number += 1
        else:
            line_number += 1
            new_line = line.split('|')
            format_line = [el.strip() for el in new_line]
            curs.execute(query, format_line)

# 使用连接对象的commit()方法，提交导入的数据，不提交数据不能进入数据库
con.commit()
# 使用连接对象close()方法关闭连接
con.close()







