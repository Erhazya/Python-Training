strs = ["rtower","flow","flight"]

pre = strs[0]



for i in strs :
    while not i.startswith(pre):
        pre = pre[:-1]


print(pre)


