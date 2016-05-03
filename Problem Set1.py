#Problem 1 
s = 'bobssssaee'

nvowel = 0

for char in s:
    if char in 'aeiou':
        nvowel += 1
print("Number of vowels: " + str(nvowel))

#Problem 2
nbob = 0 

for i in range(1,len(s)-1):
    if s[i-1:i+2] == 'bob':
        nbob += 1
    
print("Number of times bob occurs is: " + str(nbob))


#Problem 3
def item_order(order): 
    nsa = 0
    nha = 0
    nwa = 0
    for i in range(1,len(order)-1):
        if order[i-1:i+2] == 'sal':
            nsa += 1
        elif order[i-1:i+2] == 'ham':
            nha += 1
        elif order[i-1:i+2] == 'wat':
            nwa += 1
    print("salad:" + str(nsa) + " hamburger:" + str(nha) + " water:" + str(nwa))
    return 
    
item_order("hamburger water hamburger")



