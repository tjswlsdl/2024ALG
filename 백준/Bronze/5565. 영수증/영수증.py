price = int(input())
lst=[]

for i in range(9):
    book = int(input())
    lst.append(book)
    
print(price - sum(lst))
    