
#comprehensions
#ask the user what you want them to enter 
user_input = input('Enter 16 numbers between 1-9: ')
# this is a example of hard coding the it in so you dont have to enter it every tim 
# user_input = '4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5'.replace(' ', '')
#change the users input str into a list using the list function of user_input
#also use the map function to allow you to put multiple functions within a single function. in this case it allowed me to use list and int, without map it gave me a error for int
user_input = list(map(int,user_input))
# this is the starting numbers that were inputed
print (user_input)
# use the .pop() function to take off the last number and store it for later 
last_num = user_input.pop()
print(last_num, "the number that is .pop()")
# starting number again 
print(user_input)
# use the reverse() function to reverse the list user_input
user_input.reverse()
# this puts  the numbers in reverse
print (user_input)

for i in range (0, len(user_input), 2):
    user_input[i] *=2
    if user_input[i] >= 9: # have the computer check if the numbers in the list are more than 9
        user_input[i] -= 9 # take those numbers and minus 9 from them 
#create a new variable and set it equal to the sum(of the old variable), then print the new one
print(user_input)
new = sum(user_input)
print ("new sum is",new)

new1 = list(str(new))
print (new1)
'5'
new2 = int(new1.pop())
print (new2)

if (last_num == new2):
    print ('Your card is valid')
else:
    print ('Your card is invalid')


'''
RE-WRITE OF THE CREDIT CARD VALIDATOR USING LIST COMPREHENSIONS 

card_number = list(map(int,input('what is your card number')))

print(card_number)

last_number = card_number.pop()

print(last_number)

card_number.reverse()

print(card_number)
doubled = [card_number[x]*2 if x %2 == 0 else card_number[x] for x in range(0, len(card_number))]
print(doubled, 'this is doubled ')

doubled = [x-9 if x > 9 else x for x in doubled]
print(doubled, 'this is subtract 9 if over 9')

card_number = sum(doubled)
print(card_number)

card_number = list(str(card_number)).pop()
print(card_number)

if last_number == int(card_number):
    print('Valid')
else:
    print('False')

'''