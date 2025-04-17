#元组（不可变，不可以加或删除）
'''
1、用圆括号括起
2、只包含一个值的元组，必须在后面加上逗号
3、tuple转化为元组
4、元组可以是不同类型的元素
5、修改元组，先将元组转化为列表，再修改列表，再用tuple变回元组
'''
tup=(1,2,3,3)
a=list(tup)
print(a)
a[3]=4
tup=tuple(a)
print(tup)
#分装和解包
c=(1,2,3,4)
(one,two,three,four)=c
print(one)
print(two)
print(three)
print(four)
(one,two,*three)=c #放入list
print(three)
#乘法
c=c*2
print(c)
