with open('test_contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    lines = [item.lower() for item in lines]
    # print(lines)

things = [] 

for i in range(len(lines)):
    key_things = lines[0]
    key_things = key_things.split(',')
    print('this is key_things',key_things)
    row = lines[i]
    row = row.split(',')
    row = dict(zip(key_things,row))
    things.append(row)
print(things)

def export_list():
    global things
    mylist = []
    
    things[0].values()
    list(things[0].values())
    list(things[1].values())
    things[0].keys()
    ','.join(things[0].keys())
    ','.join(things[0].values())
    mylist.append(','.join(things[0].keys()))

    for i in range(len(things)):# this for loop makes it loop through everything and not just line one and two
        mylist.append(','.join(things[i].values()))
    '\n'.join(mylist)
    print('this is mylist', mylist)
    # print (mylist)
    with open('test_contacts.csv', 'w') as contact_list:
       contact_list.write('\n'.join(mylist))

def input_stuff():
    #user = []
    user = input('what is your name? '), input('what is your favorite fruit? '), input('what is your favorite color?')
    print('this is orgininal user', user)
    # new_row = ''.join(user_input).split(',')
    # user.append(user_input)
    # user = [list(x) for x in user]
    # print('this is user 1', user)
    # user = [value for sec_list in user for value in sec_list]
    # print('this is user 2', user)
    # print('this is user print', user)
    new_row = dict(zip(key_things, user))
    things.append(new_row)
    print('this is things print', things)
    export_list()
    return new_row

while True:
    what_to_do = input('\nWhat would you like to do? (create,find,update,delete)\nenter [c, f, u, d] or done: ')

    if what_to_do == 'c':
        input_stuff()
    # elif what_to_do == 'f':
    #     find()
    # elif what_to_do == 'u':
    #     update()
    # elif what_to_do == 'd':
    #     delete()
    # elif what_to_do == 'done':
    #     break
    else:
        print(f'please enter a valid responce.')
        