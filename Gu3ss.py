print('Choose your number 0-10')
print('Is your number 5?(y/n)')
guess_1=input()
if guess_1 == 'y' or guess_1 == 'Y':
 print('Your number is 5')
else:
 print('is your number greater than 5?(y/n)')
 guess_2=input()
 if guess_2 == 'Y' or guess_2 == 'y':
  print('Is your number 7?(y/n)')
  guess_3=input()
  if guess_3 == 'y' or guess_3 == 'Y':
   print('Your number is 7')
  else:
    print('Is your number greater than 7?(y/n)')
    guess_4=input()
    if guess_4 == 'n' or guess_4 == 'N':
     print('Your number is 6')
    else:
     print('Is your number 8?(y/n)')
     guess_5=input()
     if guess_5 == 'y' or guess_5 == 'Y':
      print('Your number is 8')
     else:
      print('Is your number greater than 8?(y/n)')
      guess_6=input()
      if guess_6 == 'y' or guess_6 == 'Y':
       print('is your number 9?(y/n)')
       guess_7=input()
       if guess_7 == 'y' or guess_7 == 'Y':
        print('Your number is 9')
       else:
        print('Your number is 10')

 else:
  print('Is your number 2?(y/n)')
  guess_8=input()
  if guess_8 == 'Y' or guess_8 == 'y':
   print('Your number is 2')
  else:
   print('Is your number greater than 2?(y/n)')
   guess_9=input()
   if guess_9 == 'y' or guess_9 == 'Y':
    print('Is  your number 3?(y/n)')
    guess_10=input()
    if guess_10 == 'y' or guess_10 == 'Y':
     print('Your number is 3')
    else:
     print('Your number is 4')
   else:
    print('Is your number 1?(y/n)')
    guess_11=input()
    if guess_11 == 'y' or guess_11 == 'Y':
     print('Your number is 1')
    else:
     print('Your number is 0')
