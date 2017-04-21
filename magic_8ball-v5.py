import random

"""
    magic_8_ball-v4.py
    Rehan Kodekar
    date-2017-04-21
"""


class Magic8Ball:
    """ a class that defines objects of the same class"""

    def __init__(self):
        self.answers = ["Yes !", "Maybe", "Not Likely!", "No !"]
        self.reply = ''
        self.shake()

    def shake(self):
        rand_value = int(random.random() * len(self.answers))
        self.reply = self.answers[rand_value]

    def getReply(self):
        return self.reply


def main():
    magic = Magic8Ball()
    print('The magic 8 ball game ')
    while True:
        question = input('Please ask a question : \n')
        if question[0].lower() == 'h':
            print('Not a valid question')
        else:
            magic.shake()
            print(magic.getReply())
            question2 = input('Would you like to ask another question ?\n')
            if question2[0].lower() == 'n':
                break

    print('Good bye ')

if __name__ == '__main__':
    main()