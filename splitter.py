order = input("Alphabet order/number order? yes/no: ")
ans = input("eneter word/letter: ")
print('seperating ' +(ans))
word = list(ans)

#seperates word into a list or alphabet/number order

if order == "no":
    print(word)
    
if order == "yes":
    list.sort(word)
    print(word)
