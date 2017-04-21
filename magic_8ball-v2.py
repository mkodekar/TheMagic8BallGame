import random

"""
    magic_8_ball-v2.py
    Rehan Kodekar
    date-2017-04-21
"""


def main():
    """
    python does not have swicth case but it has list, tuples and dictionary
    we can either use a dictionary or a list 
    int this case i am using a list
    :return: 
    """

    print("The magic 8 ball game!")
    answers = ["Yes !", "Maybe", "Not Likely!", "No !"]
    question = input("Please ask a question : \n")
    if question[0].lower() == 'h':
        print("Not something we can answer")
    else:
        rand_value = int(random.random() * len(answers))
        print(answers[rand_value])


if __name__ == '__main__':
    main()
