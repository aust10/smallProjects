

# import random
# import string
# def can_get_preggers(jackelope):
#     print(jackelope)
#     if 3 < jackelope["age"] < 9 and jackelope["sex"] == "f" and jackelope["preggo"] == False:
#         return True
#     else:
#         return False

# # #mine
# #     return 3 < jackelope["age"] < 9 and jackelope["sex"] == "f" and jackelope["preggo"] == False

#     #make sure female
#     #is already preggers

# def make_new_jackelope():
#     list_vowels = ["a", "e", "i", "o", "u", "y"]
#     # list_alphabet = string.ascii_lowercase
#     list_constanants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
#     name = random.choice(list_constanants) + random.choice(list_vowels) + random.choice(list_constanants)
#     age = 0
#     sex = random.choice(["m","f"])
#     preggo = False
#     return {"name":name, "age":age, "sex":sex, "preggo":preggo}

# print("Welcome to the Jackelope mating simulator!")

# jack_lists = [{"name":"Adam", "age":0, "sex":"m", "preggo":False},{"name":"Eve", "age":0, "sex":"f", "preggo":False}]

# fallen_jackelopes = []
# year_counter = 0
# #year couner is me

# while len(jack_lists) <= 10:

#     #increase age
#     for jackelope in jack_lists:
#         jackelope["age"] += 1
#         # print(jack_lists)
        
#     # #remove if too old
#     # for i in range(len(jack_lists)):
#     #     if jack_lists[i]["age"] == 10:
#     #         jack_lists.remove(i)


#     #making preggo
#     for j in range(len(jack_lists)):
#         print(can_get_preggers(jack_lists[j]))
#         # print(jack_lists[j-1]["sex"])
#         # print(jack_lists[j+1]["sex"])
#         if can_get_preggers(jack_lists[j]) and (jack_lists[j-1]["sex"] == "m" or jack_lists[j+1]["sex"] == "m"):
#         # if can_get_preggers(jack_lists[j]):
#             jack_lists[j]["preggo"] = True
 
#     #counting births
#     num_births = 0
#     for jackelope in jack_lists:
#         if jackelope["preggo"] == True:
#             num_births += 1
#             jackelope["preggo"] == False
#     # print(num_births)


#     new_jackelope = {}
#     for i in range(num_births):
#         print("Im here")
#         new_jackelope = make_new_jackelope()
#         jack_lists.append(new_jackelope)

#     year_counter +=1

# print("i am new jackalope", new_jackelope)
#     # for jackelope in jack_lists:
#     #     if jackelope["age"] >= 10:
#     #         fallen_jackelopes.append(jackelope["name"])
#     #         print(fallen_jackelopes)
#     # for jackelope in jack_lists:
#     #     if jack_lists["age"] == 10:
#     #         remove(10)
# print("i am jacklist", jack_lists)
# print(year_counter)

# '''
# year = 0
# age = 0

# while len(jackelope_dictionary) <= 1000:
  
#     num_births = 0

#     for index in range(len(jackelope_age)):
#         jackelope_age[index] += 1
#         if 3 < jackelope_age[index] < 9 :
#             num_births += 1

#     # num_births = num_births//2

#     while jackelope_age.count(10) > 0:
#         jackelope_age.remove(10)

#     for i in range(num_births):
#         jackelope_age.append(0)
    
#     print(jackelope_age)
    
#     year += 1
# else: 
#     print("meow")
#     print(year)

#     '''

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peak(data):
    peaks_data = []
    for i in range(1,len(data)-1):
        if data[i-1] < data[i] and data[i+1]< data[i]:
            peaks_data.append(i)
    return peaks_data

print(peak(data))

def valley(data):
    valley_data = []
    for i in range(1, len(data)-1):
        if data[i-1] > data[i] and data[i+1] > data[i]:
            valley_data.append(i)
    return valley_data

print(valley(data))

def peaks_vallys(data):
    # peaks_valley_data = list(zip(valley(data),peak(data)))
    peaks = peak(data)
    valleys = valley(data)
    peaks_valley_data = peaks + valleys
    peaks_valley_data.sort()
    return peaks_valley_data

print(peaks_vallys(data))

def heighest_point(data):
    height = 0
    for point in data:
        if point > height:
            height = point

    return height



def print_stuff(data):

    for y in range(heighest_point(data)+1,0,-1):
        
        for x in range(len(data)):
            if data[x] < y:
                print('  ',end='')
            elif data[x] >= y:
                print('X ',end='')
        print()
print_stuff(data)



# [1,2,3,4] == [5,6,9,3]
# counter = 0
# ballance = 0
# while counter <= 100000:

#     [(1,5),(2,6)]
#     match = 0
#     for x,y in numbers:
#         if x == y:
#             match += 1
#         else:
#             pass
        
#     if match == 1:
#         ballance += 4
#     elif match == 2:
#         ballanch += 100
#     counter += 1


# hello = "hello this is ."

# hello2 = hello.replace(".","")
# hello3 = hello.replace(' ', '')
# print(hello3)


# need to find all the words in a paragraph
# need to get rid of puct 

# need to fined all the sentences in a paragraph
# need to find all the instances of end of sentance . , ? !
# .count(".")

# need to find the characters in a paragraph
# need to get rid of puct 


# hello = "hello this. is the. sentence."

# new = hello.count('.')
# print(new)









# ages = (counter[2]['ages'])
# new = (counter[1][1]['ageee'])


# print(f'hello this is {new} you know right')
list_stuff = ['name','fav color', 'food']

user_input2 = [input('what is your name'), input('what is yoru fav color'), input('what is your fav food')]

print(user_input2)


new2 = dict(zip(list_stuff,user_input2))
print(new2)


test_card = [int(input("enter a number"))]
[1]