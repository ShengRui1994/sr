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
