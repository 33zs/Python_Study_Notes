#集合
#无序性、唯一性、可删可加
#可包含任何数据类型
#用花括号{}
a={1,2,'three','true'}
a=set((1,2,'three','true'))
#access items
for item in a:
    print(item)
#add()
a.add('4')
print(a)
#update(iterable)
b=[5,67,7,9]
a.update(b)
print(a)
#删除元素，不存在则出错
#1
a.remove(5)
print(a)
#2
a.remove(7)
print(a)
#并集
b=[9,10,11]
a.union(b)
print(b)
print(a)
#交集
#1
c={'x','y','z'}
d={'x',1,2,3}
c.intersection_update(d)
print(c)
#2
e=c.intersection(d)
print(e)
#找出不同元素
#1
i={1,2,3,4,5,9,10,11}
p={1,2,3,4,5,6,7}
i.symmetric_difference_update(p)
print(i)
#2
f={1,2,3,4,5,9}
g={2,3,4,5,6,7}
o=f.symmetric_difference(g)
print(o)