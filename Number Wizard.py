
# Initial set up
high = 200
low = 0 
ans = (high+low)/2
ind = 'h'
print('Please think of a number between 0 and 100!')


while ind != 'c':
    if ind == 'h':
        high = ans
    elif ind == 'l':
        low = ans
    else:
        print('Sorry, I did not understand your input.') 
    ans = (high+low)/2    
    print('Is your secret number '+ str(ans)+ ' ?')   
    ind = raw_input('Enter h to indicate the guess is too high. Enter l to indicate the guess is too low. Enter c to indicate I guessed correctly. ')
    
    
print('Game over. Your secret number was: ' + str(ans))

