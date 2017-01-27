def fabo(num=0):
    seq=[0,1]
    index=1
    while index<num:
        seq.append(seq[index]+seq[index-1])
        index+=1
    return seq[1:]
amount=int(input("how many numbers you want?"))
print(fabo(amount))