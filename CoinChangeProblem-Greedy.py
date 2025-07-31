
coins = [1,2,5,10,20,50,100,200,500]

count, myMoney = 0, 182 
coins.sort(reverse = True) 
for coin in coins:
    while myMoney >= coin:
        myMoney -= coin
        count += 1 
    
    if myMoney == 0:
        break 
    
print(f"{count}")
