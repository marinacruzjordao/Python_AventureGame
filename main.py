# Aventure Game
# Diferent ends to depending of the previous answers.

# environment: War between two nations, side North, sigh South
#

class Aventure:
    def __init__(self):
        self.q1='Where you born? North ou South?'
        self.q2='What weapon do you prefer? Sword or Shield ?' # sword= north, shield =south
        self.q3= 'What is your skill? Combat or Tactic'
        self.end1= 'You are a hero in combat!'
        self.end2 = 'You are a hero who protects all our troops!'
        self.end3 = 'You are a hero in the shadows!'
        self.end4 = 'You are not able to fight in this battle!'


    def start(self):
        a1=input(self.q1)

        if a1=='North' or a1=='north':
            a2=input(self.q2)
            if a2 == 'Sword' or a2 == 'sword':
                print(self.end1)
            elif a2 == 'Shield' or a2 == 'shield':
                print(self.end2)
            else:
                print('This option is not valid.')
        elif a1=='South' or a1=='south':
            a3=input(self.q3)
            if a2 == 'Combat' or a2 == 'combat':
                print(self.end3)
            elif a2 == 'Tactic' or a2 == 'tactic':
                print(self.end4)
            else:
                print('This option is not valid.')

a=Aventure()
a.start()