Colors = ['RED', 'GREEN', 'BLUE', 'YELLOW','BLACK','PURPLE','WHITE']

def player_choice(name, choices):
    player_has_chosen_ok = False

    while not player_has_chosen_ok:
        print()
        print('choose a ' + name + ':')
        for i in range(0, len(choices)):
            print(choices[i])

        choice = input('--> ')

        player_has_chosen_ok = (choice in choices)

        if not player_has_chosen_ok:
            print('please choose something on the list')

    return choice

colour_choice = player_choice('colour', Colors)

n_letters_in_colour = len(colour_choice)


if n_letters_in_colour in [3, 5]:
    first_number_choices = ['1', '2', '5', '6']
else:
    first_number_choices = ['3', '4', '7', '8']

first_number_chosen = player_choice('number', first_number_choices)



if n_letters_in_colour in [3, 5]:
    
    if first_number_chosen in ['1', '5']:
        second_number_choices = ['3', '4', '7', '8']
    else:
        second_number_choices = ['1', '2', '5', '6']
else:

    if first_number_chosen in ['3', '7']:
        second_number_choices = ['1', '2', '5', '6']
    else:
        second_number_choices = ['3', '4', '7', '8']

second_number_chosen = player_choice('number', second_number_choices)


fortune_number = int(second_number_chosen) - 1
print('There you go:')
print(fortune_number)

fortunes = ['You will become very intelligent!',
            'A year from now you will wish you have started today',
            'You will fall into a big trap!',
            'You will be late in your next online class!',
            'You will lose your umbrella!',
            
            'You will see your classmates soon!',
            'You will get no homework tomorrow!',
            'Your online classes will be cancelled due to holidays',]

player_fortune = fortunes[fortune_number]

print()
print(player_fortune)
print("Disclamer: This is just for fun. Do not believe in this.")
print()
