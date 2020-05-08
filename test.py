n = input ('enter the number: ')
print(n)

data = []
for y in n:
    data.append(y)

print(data)

counts = [False, False, False, False, False, False, False, False, False, False]

i = 0

# print(counts)

for ii in data:

    # print(ii)
    for i in range(0, 10):
        print ("i : " + str (i))
        print ("ii : " + str(ii))
        if str(ii) == str(i):
            print ("equal : " + str(ii))
            counts[i] = True

    

showFlag = False
strMsgNo =  "There is no missing digits : "
strMsgYes = "The missing digits : "

j = 0

print(counts)
for jj in counts:
    
        if bool(jj) == True:
            strMsgYes += str(j) 

        j += 1

print (strMsgYes)