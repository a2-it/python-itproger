str_list = [["some", "special"], ["text", "for", "you"], ["-", 50]]
a =''
for item in str_list:
    for iitem in item:
        a = a +' '+ str(iitem)
print(a)