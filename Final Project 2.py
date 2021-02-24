import random

word = "false"
# Parts 1 and 2
phrases = ['Wait and See','Third Time Is the Charm','The End Justifies the Means','The Apple Doesnt Fall Far From the Tree', 'Talk is Cheap','Rome Wasnt Built in a Day','Revenge Is a Dish Best Served Cold','Pride Goes Before a Fall','Only Fools and Horses Work','Once Bitten Twice Shy','No News is Good news','No Man is an Island','Misery Loves Company','Might is Right','Less is More','Its Never Too Late','It Takes Two to Tango','Ignorance is Bliss','Hunger is the Best Sauce','haste Makes Waste','Good Things Come to Those Who Wait','Good Things Come in Threes','Curiosity killed the Cat','Clothes Make the Man','Blood is thicker Than Water','Better late Than Never','Bad News travels Fast','bad Money Drives Out Good','A Stitch in Time Saves Nine','A Problem Shared is a Problem Halved','A Picture Paints a Thousand Words','A Penny Saved is a Penny Earned','A New Broom Sweeps Clean','A House Divided Against Itself Cannot Stand','A Good Man is Hard to Find','A Friend in Need is a Friend indeed','A fool and His MOney Are Soon Parted','A Bird in The Hand is Worth Two in the Bush']

# used this for practicing the code
# ran = ('Wait and See').lower()

ran = random.choice(phrases).lower()
length = len(ran)
dash = ''
for i in ran:
    if i !=' ':
        dash = dash + '-'
    else:
        dash = dash + ' '
print('This is the hidden phrase: ')
print(dash)

# Parts 3 and 4
Spin = input('Press Enter to Spin the Wheel: ')
Outcomes = ['$100','$150','$250','$400','$650','$1,000','$2,500','$5,000','bankrupt','lose a turn']
Winnings = print(random.choice(Outcomes))
while True: 
    if Outcomes == ['bankrupt,lose a turn']:
        print('Spin the Wheel Again')
        input('Press Enter to Spin the Wheel: ')
    else:
        break

# Parts 5 and 6

def guess():
    L =''
    L = input('User Pick a letter: ')
    return L

# parts 7 and 8

def check(dash):
    T = ''
    count = 0
    for i in ran:
        if i == L: 
            T = T + i + ' '
        else:
            T = T + dash[(count)] + ' '
        count = count + 1
        
    return(T)

while word == "false":
    
    L = guess()

    dash = check(dash)

    print(dash)

    Z = ''
    Z = input('User Guess the phrase: ')
    if ran == Z:
        print('Correct! The phrase is:', ran, ' You Win!')
        break
    else:
        print('This is not the right phrase, next users turn')




# letters = ''
# for j in ran:
    # if  == '-':
        # letters = letters 
    # else:
        # letters = letters + '-'

# print(letters)


    









        
    






        
    
