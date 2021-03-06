import re
'''
'''
#给你一串字符串，判断是否是手机号码


def check_phone(str):
    pat = r'(1(([35789]\d)|(47))\d{8})'
    res = re.findall(pat,str)
    return res


print(check_phone('asdfsdfdsafs139123456785afdasfafs139123451234afs '))
print(check_phone('139123456785'))
print(check_phone('1391234a677'))
print(check_phone('239123456785'))

print('-------------------哈哈哈哈哈哈------------------')

'''
Python自1.5以后增加了re模块，提供了正则表达式模式
'''

'''
re.match函数
原型：match(pattern,string,flags=0)

参数：
pattern: 匹配的正则表达式
string： 要匹配的字符串
flags：  标志位，用于控制正则表达式的匹配方式
re.I ：  忽略大小写   （常用）
re.L ：  做本地化识别
re.M :   多行匹配，影响 ^ 和 $
re.S :   是 . 匹配包括换行符在内的所有字符  （常用）
re.U :   根据Unicode字符集解析字符，影响 \w \W \b \B
re.X :   使我们以更灵活的格式理解正则表达式

功能：尝试从字符串的起始位置匹配一个模式，如果不是起始位置却匹配成功的话，返回None，其他情况也返回None

'''

#www.baidu.com
print(re.match('www','www.baidu.com'))
print(re.match('www','ww.baidu.com'))
print(re.match('www','baidu.www.com'))
print(re.match('www','Www.baidu.com',flags = re.I))

#扫描整个字符串，返回从起始位置成功的匹配

print('---------------------------')

'''
re.search函数
原型：search(pattern,string,flags=0)

参数：
pattern: 匹配的正则表达式
string： 要匹配的字符串
flags：  标志位，用于控制正则表达式的匹配方式

功能：扫描整个字符串，并返回第一个成功的匹配
'''
print(re.search('xuhan','a good man is xuhan heihei xuhan!'))


'''
re.findall函数
原型：findall(pattern,string,flags=0)

参数：
pattern: 匹配的正则表达式
string： 要匹配的字符串
flags：  标志位，用于控制正则表达式的匹配方式

功能：扫描整个字符串，并返回结果列表
'''
print(re.findall('xuhan','a good man is xuhan heihei xuhan!'))




print("----------------------匹配单个字符与数字----------------------------")
r'''
. :   匹配除换行符以外的任意字符  
[0123456789] :          []是字符集合，表示匹配方括号中所包含的任意一个字符
[xuhan]      :          匹配'x','u','h','a','n'中任意一个字符
[a-z]        :          匹配任意小写字母
[A-Z]        :          匹配任意大写字母
[0-9]        :          匹配任意数字，类似[0123456789]
[0-9a-zA-Z]  :          匹配任意的数字和字母
[^xuhan]     :          匹配xuhan这几个字母以外的所有字符，中括号里的^称为脱字符，表示不匹配集合中的字符
\d           :          匹配所有数字
\D           :          匹配非数字字符
\w           :          匹配数字，字母和下划线,效果同[0-9a-zA-z_]
\s           :          匹配任意的空白符(空格，换行，回车，换页，制表),效果同[ \f\n\r\t]
\S           :          匹配任意的非空白符
'''
print(re.search('.','xuhan is a good man 6'))
print(re.search('[0123456789]','xuhan is a good man 6'))
print(re.findall('\w','xuhan is a good man 6'))


print('-----------------------锚字符（边界字符）---------------------')
'''
^            :          行首匹配，和在[]里的^不是一个意思
$            :          行尾匹配

\A           :          匹配字符串开始，它和^的区别是，'\A'只匹配整个字符串的开头，即使在re.M模式下，也不会匹配它行的行首
\Z           :          匹配字符串的结尾，同上区别

\b           :          匹配一个单词的边界，指单词和空格间的位置
                        r'er\b'可以匹配：可以匹配never，不能匹配nerve
\B           :          匹配非单词边界，与上面相反
'''
print(re.search('^xuhan','xuhan is a okay man!'))
print(re.search('man$','xuhan is a okay man'))
print(re.findall('^xuhan','xuhan is a okay man\nxuhan is a okay man',re.M))
print(re.findall('\Axuhan','xuhan is a okay man\nxuhan is a okay man',re.M))

print(re.search(r'ma\b','xuhan is a okay man'))
print(re.search(r'ma\B','xuhan is a okay man'))

print('-------------------------匹配多个字符——--------------------')
'''
说明:   下方的x，y，z均为假设的普通字符，不是正则表达式的元字符
(xyz)   匹配小括号内的xyz作为一个整体去匹配
x?      匹配0个或1个x
x*      匹配0个或者任意多个x
x+      匹配至少一个x
x{n}    匹配确定的n个x(n是一个非负整数)5
x{n,}   匹配至少n个x
x{n,m}  匹配至少n个最多m个x。注意：n<=m
x|y     匹配x或y
'''
print(re.findall(r'(xuhan)','xuhan is a good ,xuhan is nice man !'))
print(re.findall(r'a*','aaaabcdf')) #贪婪
print(re.findall(r'a?','abbbbbbbba')) #非贪婪，尽可能少的匹配
print(re.findall(r'a+','aaaabcdf'))
print(re.findall(r'a{3}','aabcdfaaaa,aaaaaa')) 
print(re.findall(r'a{3,}','aabcdfaaaa,aaaaaa')) 
print(re.findall(r'a{3,5}','aabcdfaaaa,aaaaaa')) 
print(re.findall(r'x|X','xxxxx,XXXX,adafaX')) 
print(re.findall(r'((x|X)uhan)','xuhan--Xuhan')) 

#需求，提取xuhan。。。。man
str1 = 'xuhan is a good man!xuhan is a nice man!'
print(re.findall(r'^xuhan.*man!$',str1))
print(re.findall(r'xuhan.*man!',str1))
print(re.findall(r'xuhan.*?man!',str1))



print('----------------------------特殊-------------------------')
'''
*?  +？  x?     最小匹配
通常 都是尽可能多的匹配，可以使用这种解贪婪匹配
(?:x)       类似(xyz),但不表示一个组
'''
#注释：   /*part1*/
print(re.findall(r'//*.*?/*/',r'/* part1 */        /* part2 */'))



print('--------------------------------------re模块深入------------------------------------------')
'''
切割字符串
'''
str2  = 'xuhan si  fda fas f       !'
print(re.split(r' +',str2))

'''
re.finditer函数
原型：  finditer(pattern,string,flags=0)
参数:
patter: 匹配的正则表达式
string：要匹配的字符串
flags： 标志位，用于控制正则表达式的匹配方式
功能：  与findall类似，扫描整个字符串，返回的是一个迭代器
'''
str3 = 'xuhan is a good man!xuhan is a nice man!'
d = re.finditer(r'xuhan',str3)
while True:
    try:
        l = next(d)  #迭代器， 用next返回每一个对象
        print(l)
    except StopIteration as e:
        break

'''
字符串的替换和修改
sub(pattern,repl,string,count=0,flags=0)
subn(pattern,repl,string,count=0,flags=0)

pattern:    正则表达式(规则)
repl:       指定的用来替换的字符串
string:     目标字符串
count:      最多替换次数
flags:      模式

功能：      在目标字符串中以正则表达式的规则匹配字符串，可以指定替换的次数
区别：      返回类型不同，sub为字符串类型，subn为元组
'''
str4 = 'xuhan is a good man!xuhan is a nice man!'
print(re.sub(r'good','nice',str4))
print(re.subn(r'good','nice',str4))


'''
分组：
概念：  除了简单的判断是否匹配之外，正则表达式还有提取子串的功能。用()表示的就是分组
'''
str5 = '010-53247654'
m = re.match(r'(?P<first>\d{3})-(?P<last>\d{8})',str5)
#使用序号获取对应组的信息，group(0)代表原始字符串,真正的组内容是1和2
print(m.group(0))
print(m.group(1))
print(m.group('first'))
print(m.group(2))
#查看匹配的各组的情况
print(m.groups())



'''
编译：  当我们使用正则表达式时，re模块会干两件事
1.   编译正则表达式，如果正则表达式本身不合法，会报错
2.   用编译后的正则表达式去匹配对象
compile(pattern,flags=0)
pattern:  要编译的正则表达式
'''  
pat = r'(1(([35789]\d)|(47))\d{8})'
#编译成正则对象
re_telephone = re.compile(pat)
print(re_telephone.match('13911980114'))




'''
re.match()
re_telephone.match(string)#少了参数,下同
re.search()
re.findall()
re.finditer()
re.split()
re_telephone.split(string,maxsplit=0) #下同
re.sub()
re.subn()
'''

re_QQ = re.compile(r'^[1-9]\d{5,9}$')  #开头是1-9后面有5-9个数字
print(re_QQ.search('123456789'))












