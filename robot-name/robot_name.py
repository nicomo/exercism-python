from random import randint

class Robot(object):

    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    names = set()

    def __init__(self):
        while True:
            self.name = self.letters[randint(0,25)]+self.letters[randint(0,25)]+str(randint(0,10))+str(randint(0,10))+str(randint(0,10))
            if self.name not in self.names:
                self.names.add(self.name)
                break

    def reset(self):
        self.__init__()
        