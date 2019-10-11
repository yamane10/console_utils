"""
A collection of utility functions for building CLI scripts.
"""

def query_select(question, choices, default=None, max_columns=3, multi=True):
    """
    Function for creating prompt to select a choice from a list of choices.

    Based on the provided max_columns, the function will determine the best
    column arrangement and create columns of numbered choices, prompting the
    user to enter a choice (by number).

    The function will return the value of the selected choice.

    Usage:
        >>> favorite_color = query_select(
            "What's your favorite color?",
            ["Red", "Orange", "Yellow",
                "Green", "Blue", "Indigo",
                "Violet", "Brown", "Black",
                "White"],
            max_columns=2,
            multi=False)

        prints:
            What's your favorite color?
             1) Red      6) Indigo
             2) Orange   7) Violet
             3) Yellow   8) Brown
             4) Green    9) Black
             5) Blue    10) White
            Enter selection (by number):

        If the user enters "10", the function will return "White".
    """
    number_of_choices = len(choices)
    columns = []
    longest_choice = sorted(choices, key=lambda c: len(c), reverse=True)[0]

    while True:
        number_of_rows = number_of_choices // max_columns
        modulus = number_of_choices % max_columns
        if modulus == 0:
            break
        elif max_columns - modulus > 1:
            max_columns -= 1
        elif max_columns > number_of_choices:
            max_columns = number_of_choices
        else:
            break

    column = []
    count = 0
    choice_number = 1
    choice_dict = {}
    while len(choices) > 0:
        choice = choices.pop(0)
        choice_dict[choice_number] = choice
        column.append((choice_number, choice))
        count += 1
        choice_number += 1

        if count == number_of_rows:
            if modulus > 0:
                choice = choices.pop(0)
                choice_dict[choice_number] = choice
                column.append((choice_number, choice))
                count = 0
                choice_number += 1
                modulus -= 1

                columns.append(column)
                column = []
            else:
                count = 0
                columns.append(column)
                column = []
    if len(column) > 0:
        columns.append(column)

    print(question)

    for i in range(len(columns[0])):
        row = []
        for column in columns:
            try: row.append(column[i])
            except: pass
        print("\t".join(["{}) {}".format(str(number).rjust(2), choice).ljust(len(longest_choice) + 5) for (number, choice) in row]))

    plural = ''
    if multi:
        print("\nYou can enter multiple selections by giving a comma-separated (e.g. 1, 5)")
        plural = "(s)"
    selections = input("Enter selection{} (by number): ".format(plural))

    valid_choice = False
    while not valid_choice:
        valid_choice = True

        if (not multi) and (len(selections.split(',')) > 1):
            selections = input("ERROR: Please make only one selection: ")
            break
        else:
            try:
                for selection in selections.split(','):
                    if int(selection.strip(' ')) not in choice_dict:
                        selections = input("ERROR: selection {} not a valid choice. Please enter again: ".format(selection))
                        valid_choice = False
                        break
                    else:
                        break
            except:
                selections = input("ERROR: selection {} not a valid choice. Please enter again: ".format(selection))
                valid_choice = False
    if multi:
        output = [choice_dict[int(selection.strip(' '))] for selection in selections.split(',')]
    else:
        output = choice_dict[int(selections.strip(' '))]

    return output

def query_yes_no(prompt, default='yes'):
    """
    Function for prompting user to answer yes or no to a given prompt.

    Usage:
        >>> query_yes_no("Accept match?")

        prints:
            Accept match? (yes or no):

        If user enters "y", "ye", or "yes", the function will return "yes".
        If user enters "n" or "no", the function will return "no".
        If user enters nothing, the default value is returned.
    """
    prompt = prompt + " (yes or no): "
    valid_choices = {
        "yes": "yes",
        "ye": "yes",
        "y": "yes",
        "no": "no",
        "n": "no"
        }
    response = input(prompt)

    while True:
        if response == '':
            output = default
            break
        elif response in valid_choices:
            output = valid_choices[response]
            break
        print("Invalid response '{}'. Please enter y or n.".format(response))
        response = input(prompt)

    return output

def determine_plural(item_to_check):
    if type(item_to_check) is int:
        num = item_to_check
    elif type(item_to_check) is list:
        num = len(item_to_check)
    else:
        raise Exception("Unsupported input type '{}'.".format(type(item_to_check)))
    if num == 1:
            plural = ''
    else:
        plural = 's'
    return plural

def print_verbose(text, verbose):
    """Wrapper for print method that only prints if verbose is True"""
    if verbose:
        print(text)