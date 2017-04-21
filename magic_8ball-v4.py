import random

"""
    magic_8_ball-v4.py
    Rehan Kodekar
    date-2017-04-21
"""


def main():
    print('The magic 8 ball game !')
    answers = ["Yes !", "Maybe", "Not Likely!", "No !"]
    while True:
        question = input('Please ask a question: \n')
        if question[0].lower() == 'h':
            print('Not a valid question')
        else:
            rand_value = int(random.random() * len(answers))
            print(answers[rand_value])
            question2 = input('Would you like to ask another question ?\n')
            if question2[0].lower() == 'n':
                break

    print('Good bye ')

if __name__ == '__main__':
    main()
