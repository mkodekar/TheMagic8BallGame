import random

"""
    magic_8_ball-v1.py
    Rehan Kodekar
    date-2017-04-21
"""


def main():
    print("The magic 8 ball game !")
    question = input("Please ask a question: \n")
    if question[0].lower() == 'h':
        print("This type of questions are not allowed")
    else:
        # this will always give out a round up value which will be less than 4
        rand_value = int(random.random() * 4)
        if rand_value == 0:
            print("Yes!")
        elif rand_value == 1:
            print("May be")
        elif rand_value == 2:
            print("Not Likely!")
        else:
            print("No !")

if __name__ == '__main__':
    main()
