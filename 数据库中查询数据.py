import sys,sqlite3
"""在数据库中查询数据"""

con_find = sqlite3.connect('test')
curs_find = con_find.cursor()
text = input('请输入要查询的字段名：')
query_find = 'select * from phone where ' + text
print(query_find)
curs_find.execute(query_find)
names = [name[0] for name in curs_find.description]  # description 由列组成的序列
for row in curs_find.fetchall():
    for pairs in zip(names, row):
        print('{}:{}'.format(*pairs))
