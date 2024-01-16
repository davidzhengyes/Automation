myset=set()

myset.add(1)
myset.add(2)
myset.add(1)
myset.add("ooo")
print(myset)

if "ooo" in myset:
    print("ooo in myset")