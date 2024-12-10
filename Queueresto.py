stack = []
# push elemen ke stack
stack.append(10)
stack.append(20)
stack.append(30)
print("stack setelah push:",stack)

# proses pop pertama : pop elemen dari stack
elemen = stack.pop()
print("elemen yang di-pop pertama:",elemen)
print("stack stelah pop pertama:",stack)

# peak elemen teratas
if stack:
    print("elemen teratas:",stack[-1])
else :
    print("stack kosong")

# proses pop kedua : pop elemen dari stack
elemen = stack.pop()
print("elemen yang di-pop kedua:",elemen)
print("stack stelah pop kedua:",stack)
