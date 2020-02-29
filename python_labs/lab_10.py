
nums = []
total = 0

while True:
    # take in user input
    user_input = input('enter a number, or enter *done*: ')
    # append user input to nums
    nums.append(user_input) #after talking we discussed this could go by break
    # if statemt to get user input 'done'
    if user_input == 'done':
        nums.pop() #un needed in if you put the .append() by the break
        print (nums)
        break
    # if user input is not done then do the for loop below to get numbers add numbers and divide by total
for num in nums:
    total += int(num)
print('sum is', total)

average = total / len(nums)
print('the average is', average)


# check if they are done first then go and continue so switch line 7 and 8 and get rid of the break

# on line 17 you need to put str(average) so that you can concatinate if you leave it as a float then it just adds it. also you should have put a + insted of the , 

# another example of line 17 is print(f'average: {average}')
    
