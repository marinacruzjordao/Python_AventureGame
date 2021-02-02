# Aventure Game
# Diferent ends to depending of the previous answers.

# environment: War between two nations, side North, sigh South
#
from PySimpleGUI import PySimpleGUI as sg

class Aventure:
    def __init__(self):
        self.q1='Where you born? North ou South?'
        self.q2='What weapon do you prefer? Sword or Shield ?' # sword= north, shield =south
        self.q3= 'What is your skill? Combat or Tactic'
        self.end1= 'You are a hero in combat!'
        self.end2 = 'You are a hero who protects all our troops!'
        self.end3 = 'You are a hero in the shadows!'
        self.end4 = 'You are not able to fight in this battle!'

    def data(self):
        self.event, self.value = self.w1.read()

    def start(self):
        # create layout
        sg.theme('Reddit')

        layout = [
            [sg.Text('Question:'),sg.Output(key='question')],  # line1
            [sg.Text('Your answer:'),sg.Input(key='answer')],  # line 2
            [sg.Button('Start'),sg.Button('Play')]  # Line 3
        ]

        # create a window in GUI
        self.w1 = sg.Window('Adventure Game').layout(layout)

        while True:
            
            #obtain data
            self.data()
            if self.event== sg.WINDOW_CLOSED:
                break
            
            #start program
            if self.event=='Start':
                print(self.q1)
                self.data()

                #adventure selection and respetive end
                if self.value['answer']=='North' or self.value['answer']=='north':
                    print(self.q2)
                    self.data()

                    if self.value['answer'] == 'Sword' or self.value['answer'] == 'sword':
                        print(self.end1)
                    elif self.value['answer'] == 'Shield' or self.value['answer'] == 'shield':
                        print(self.end2)
                    else:
                        print('This option is not valid.')
                if self.value['answer']=='South' or self.value['answer']=='south':
                    print(self.q3)
                    self.data()
                    if self.value['answer'] == 'Combat' or self.value['answer'] == 'combat':
                        print(self.end3)
                    elif self.value['answer']== 'Tactic' or self.value['answer']== 'tactic':
                        print(self.end4)
                    else:
                        print('This option is not valid.')

a=Aventure()
a.start()