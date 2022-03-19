order = input("Alphabet order/number order? yes/no: ")
ans = input("eneter word/letter: ")
print('seperating ' +(ans))

#seperates word into a list or alphabet/number order
if order == "no":
    word = list(ans)
    print(word)
    
if order == "yes":
    word = list(ans)
    list.sort(word)
    print(word)


