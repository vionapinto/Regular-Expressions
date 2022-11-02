import re

############# TASK 1

def task_1():
    print('---Task 1---')

    text = 'Berlin is a world city of culture, politics, media and science.'
    white_space = re.search('\s',text)

    print('The first white-space character is located at position: ' ,white_space.start())


############# TASK 2

def task_2():
    print('---Task 2---')

    text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
    word = re.search('Frankfurt',text)
    print(word)

############# TASK 3

def task_3():
    print('---Task 3---')
    text = "Berlin is a city of culture."
    dash = re.sub(' ','-', text)
    print(dash)


############# TASK 4

def task_4():
    print('---Task 4---')
    text = "Berlin is a city of culture."
    x = re.search('in',text)
    print(x)


############### TASK 5

def task_5():
    print('---Task 5---')
    text = "Berlin is a city of culture."
    b = re.search(r'\bB\w+',text)
    print(b.span())


############### TASK 5

def task_6():
    print('---Task 6---')
    text = "The rain in Spain."
    count = re.findall('ai',text)
    print(len(count))