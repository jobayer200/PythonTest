# mystring1 = "Hello"
# mystring2 = " World"
#
# print(mystring1.lower())
# # print(mystring.split())
#
# # value = 5
# #
# # print(len(mystring1))
# print(mystring1.__add__(mystring2))

# # Prob-1
# result = 0
# import importlib
# import time

a = 10
b = 20
c = 15
# result = a + b
# print('Sum of two number: {}'.format(result))
# print(f'Sum of two number: {result}')
# print("Sum of two number:", result)


# if and else

# if a > b:
#     print("a is grater than b and c")
# elif b > a:
#     print("b is grater than a and c")
# else:
#     print("c is grater than a and b")


# Loop

# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for count in mylist:
#     print(count)

# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = 0
# for count in mylist:
#     result = result + count
# print("Sum of list:", result)

# count = 0
# while count < 10:
#     print(count)
#     count += 1

# for count in range(1, 11):
#     print(count)


# prob no:1
# str = 'Print only the words that start with s in this sentence'
# for word in str.split():
#     if word[0] == 's':
#      print(word)


# prob no:2
# for num in range(0, 11, 2):
#     print(num)
# or
# print(list(range(0, 11, 2)))


# prob no:3
# mylist = [num for num in range(1, 51) if num % 3 == 0]
# print(mylist)


# prob no:4
# str = 'Print every word in this sentence that has an even number of letters'
# for word in str.split():
#     if len(word) % 2 == 0:
#         print(word+"  is even")


# prob no:5
# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         #print(num)
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         # print(num)
#         print("Fizz")
#     elif num % 5 == 0:
#         #print(num)
#         print("Buzz")
#     else:
#         print(num)


# prob no:6
# str = "Create a list of the first letters of every word in this string"
# mylist = [word[0] for word in str.spllflt()]
# print(mylist)


# def fact(n):
#     f = 1
#     for i in range(1, n):
#         f = f * i
#
# n = input("Enter a number: ")
# result = fact(n)
# print("Factorial is ", result)


# def fun(num):
#     for i in range(1, num+1):
#      print(i)
#
# num = (int)(input("Enter a number: "))
# fun(num)

# num = int(input("Enter a input for N:"))
# sum = 0
# for i in range(1, num+1):
#     x = int(input())
#     sum = sum + x
#
# avg = sum / num
# print(avg)

# arr = [1, 4, 9, 3, 2, 5, 7]
# print(arr.pop())
# num = arr.copy()
# print(arr.copy())

# arr.clear()

##########################

# import colorama
# from colorama import Fore
#
# print(Fore.YELLOW + "Hello world")
# print(Fore.BLUE + "Hello world")
# print(Fore.MAGENTA + "Hello world")

######################################

# import pyttsx3
#
# friend = pyttsx3.init()
# # friend.say("Hey what's your name?")
# speech = input("Say something: ")
# friend.say(speech)
# friend.runAndWait()


##############################

# import rotatescreen
# import time
#
# screen = rotatescreen.get_primary_display()
# # screen.rotate_to(0)
# for i in range(13):
#     time.sleep(1)
#     screen.rotate_to(i * 90 % 360)


###################

# import pyttsx3
# import PyPDF2
#
# book = open('test.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(book)
# pages = pdfReader.numPages
# print(pages)
# speaker = pyttsx3.init()
# page = pdfReader.getPage(0)
# text = page.extractText()
# speaker.say(text)
# speaker.runAndWait()


#########################

import cv2

cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret, frame1 = cam.read()
    re, frame2 = cam.read()
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_RGBA2GRAY)
    if cv2.waitKey(10) == ord('c'):
        break
    cv2.imshow("Camera", diff)

