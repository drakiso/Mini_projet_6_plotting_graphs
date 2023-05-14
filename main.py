"""a multi-file application that allows users to create graphs (or charts) for the file iris.csv"""

import data_storage as ds
from graphing import create_scatter


def charting_menu():
    menu = """Enter the column you'd like to chart:
    1: sepal_length
    2: sepal_width
    3: petal_length
    4: petal_width
    
    """

    try:
        selection = int(input(menu).strip())
    except ValueError:
        print("Error !!! You should enter an integer")
    else:
        if selection not in [1, 2, 3, 4]:
            print("Choice not valid !! Choose between 1, 2, 3 and 4")
        else:
            return selection


user_menu = """Please choose an option:

C: Chart a new graph
Q: Quit

"""

option = input(user_menu).strip().title()[0]

while option != 'Q':
    if option == 'C':
        column = charting_menu()
        name = ''
        if column is not None: name = input("Enter the name of the chart:  ")

        if column == 1:
            create_scatter(ds.data_reader('sepal_length'), name)
        elif column == 2:
            create_scatter(ds.data_reader('sepal_width'), name)
        elif column == 3:
            create_scatter(ds.data_reader('petal_length'), name)
        elif column == 4:
            create_scatter(ds.data_reader('petal_width'), name)
    else:
        print(f"{option} is not valid !!")

    option = input(user_menu).strip().title()[0]
