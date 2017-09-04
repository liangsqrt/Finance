# def iget_no_of_instance(ins_obj):
#     return ins_obj.__class__.no_inst
# class Kls(object):
#     no_inst = 0
#     def __init__(self):
#         Kls.no_inst = Kls.no_inst + 1
# ik1 = Kls()
# ik2 = Kls()
# print iget_no_of_instance(ik1)


# class A:
#     def __init__(self,url):
#         self.url = url
#     def out(self):
#         return self.url
#
#
# a = A('news.163.com')
# print a.out()
#
# b = a.__class__('www.bccn.net')
# print b.out()
# print a.out()
#
#
# print A
# print a.__class__
# print

a=[1,2,3,4,5]
b=[6,7,8,9,0]
c=[[1,2],[3,4],[5,6],[7,8]]

aa=[x+y for x in a for y in b]
cc=[x for i in c for x in i]
print cc
