names = ['inode', 'gen_num', 'parent_inode']
print(names[0])
names.append('parentGenNum')
print(len(names))  # 4
print(names[2:])  
for name in names:
    print(name)
#if you need to see the index also with element, it can start with 100 to if you specify in enumerate as initial value
for  i, name in enumerate(names,100):\
    print("name = ",name, i)
