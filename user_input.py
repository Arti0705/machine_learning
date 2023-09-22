'''user = input("what is your highest qualification? :")
print(user)'''

#string are immutable

'''
Person_name=input("Type your name here : ")
print(Person_name)
print("Length of your name is : ",len(Person_name))
print(Person_name.upper())
print(Person_name.lower())
'''



'''........if else.......'''

"""
num= int(input("Enter the value of num :"))
if(num<0):
    print("inputed number is negative....")
elif(num >0):
    if(num<=10):
        print('number is between 1 to 10')
    elif(num>10 and num <=20):
        print("number is between 11 and 20")
    else:
        print("number is greater than 20")
else:
    print("you pressed other than  number......")
    """

'''
apple_Price= 10
budget= 200

if(budget-apple_Price > 50):
    print("Alexa , we don't need apple....")
else:
    print("Alexa,add 1kg apple to the cart....")
    '''

#..............for loop ..................
# languages =['Javascript', 'Python', 'C', 'C++','Swift', 'Go', 'Java']
# print(languages)

# run a loop for each item of the list

'''
for language in languages:
    print(language)


'''
'''
fav_language=input("Your favorite language:  ")
for lang in fav_language:
    print(lang)
    '''

# print("August starting soon",25,"see you soon" ,sep=".") 
# print('Programiz is '+"awesome.....")
# x=5
# y=10
# print('The value of x is {} and y is {}'.format(y,y))

# input("the value of x and y is ")

# user_age= int(input("Enter your age here : "))

# if(user_age>=18):
#     user_name=input("What's your name : ")
#     print("{},you can drive now as your age i.e {} matches to the eligibility age.".format(user_name,user_age))

# else:
#     user=input('Enter your name bruhh : ')
#     print("{} bruhhh...,you are not eligible to drive bruhhh!!!!".format(user))

import json

my_dict = {'name': 'Alice', 'age': 30}
json_string = json.dumps(my_dict)  # Convert to JSON
print(json_string)
ttypeee= type(json_string)
print(ttypeee)





    

