c1 = False
score = int(0)
a1 = int(0)
while a1 == False:
    try:
        print("""How many fingers do you have on one hand?
(1) 7
(2) 5
(3) 9
(4) 4""")
        a1 = int(input())
        if 0 < a1 < 5:
           c1 = True
           if a1 == 2:
               score+=1
               print("Good job you got the question right.")
        else:
            print("wrong answer try, please enter a different answer.")
    except ValueError:
        print("Please pick one of the number that your answer correspond to.")

