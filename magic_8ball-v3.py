import random

"""
    magic_8_ball-v3.py
    Rehan Kodekar
    date-2017-04-21
"""

def main():
    """
       python does not have swicth case but it has list, tuples and dictionary
       we can either use a dictionary or a list 
       int this case i am using a dicionary mapping
       :return: 
       """
    print('The magic 8 ball game !')
    answers = {0: "Yes", 1: " Maybe", 2: "Not Likely !", 3: "No !"}
    question = input('Please ask a question: \n')
    if question[0].lower() == 'h':
        print('Not a valid question')
    else:
        rand_value = int(random.random() * len(answers))
        # print(str(answers.get(rand_value)))
        print(answers.get(rand_value))


if __name__ == '__main__':
    main()
