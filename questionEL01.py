#added the feedback that shows when you get it incorrect
#INT variable
c1 = False
score = int(0)
a1 = int(0)
#while loop 
while a1 == False:
#question was asked and availabe options are shown 
    try:
        print("""How many fingers do you have on one hand?
(1) 7
(2) 5
(3) 9
(4) 4""")
        a1 = int(input())
#acceptable answers are set
        if 0 < a1 < 5:
           c1 = True
#correct input is given a plus one
           if a1 == 2:
               score+=1
#when feedback for when the input is correct
               print("Good job you got the question right.")
#when feedback for when the input is incorrect
           else:
               print("try again your, answer was incorrect.")
#feedback for when the input is not an option 
        else:
            print("wrong input, enter (1), (2), (3), or (4).")
#feedback for when the input is not a number
    except ValueError:
        print("Please pick one of the number that your answer correspond to.")

