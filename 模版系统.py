# 模版系统.py
import re, fileinput

# 使用方括号括起的字段匹配
file_pat = re.compile(r'\[(.+?)\]')

# 把变量收集到命名空间中
scope = {}


# 调用re.sub()的函数
def replacement(match):
    code = match.group(1)
    try:
        return str(eval(code, scope))
    except SyntaxError:
        exec(code, scope)
        return ''


text = ''
for line in fileinput.input():
    text += line


print(file_pat.sub(replacement, text))




