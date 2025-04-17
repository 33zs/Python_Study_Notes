#直接赋值、浅拷贝、深拷贝
#直接赋值
'''
b=a
其实就是对对象的引用,a和b指向同一对象
'''
#浅拷贝copy
'''
b=a.copy()
拷贝父对象，不会拷贝对象内部的子对象
a,b是一个独立的对象，但子对象还是指向同一对象
'''
#深拷贝deepcopy
'''
a,b完全拷贝父对象及其子对象
两者完全独立
'''
import copy
a=[1,2,3,4,['a','b']]
b=a
c=copy.copy(a)
d=copy.deepcopy(a)
a.append(5)
a[4].append('c')
print('a=',a)
print('b=',b)
print('c=',c)
print('d=',d)
print(id(a))
print(id(b))
print(id(c))
print(id(d))
#id（a)=b不等于c/d