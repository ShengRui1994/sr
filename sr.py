import re
s='adad123123sad21w12w211'
def zzz():
    print('i am a boy')
print('hello')
zzz()
print(s)
print(re.findall('[0-9]',s))
#'.'可以匹配任意一个字符
#'^'可以匹配开头任意字符
print(re.search('^aa','aaaycy'))
#'$'匹配字符结尾
#'*'匹配前面一个字符零次或多次
print(re.search('aa*','aaa211sada'))
#"+'匹配任意一个字符1次或多次
#\A,\d,\D,\w,\W,\s
ss='340803199401092877'
print(re.search('(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<born_year>[0-9]{8})',ss).groupdict())
