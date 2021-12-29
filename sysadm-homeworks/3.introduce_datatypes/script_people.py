boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

boys = sorted(boys)
girls = sorted(girls)

num_boys = len(boys)
num_girls = len(girls)

if num_boys == num_girls:
    print('Идеальные пары:')
    for boy,girl in zip (boys, girls):
        print(boy,girl)
else:
    print('Не равное колличество людей')