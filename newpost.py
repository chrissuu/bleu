from datetime import date as d
def betw(x, a, b)->bool:
    '''Returns True if a <= x <= b'''

    return a <= x <= b

def is_valid_date_format(date)->bool:
    '''Returns True if the date format is valid'''
    date_split = date.split('-')
    if len(date_split)!=3:
        return False
    
    return betw(date_split[0], 1000, 9999) and \
           betw(date_split[1], 1, 12) and \
           betw(date_split[2], 1, 31)

def parse_input(input):
    return True if input == 'y' else False

print('Creating a new post template interactively...')
file_path = ""
i_date = input('Use today\'s date? [y/n]\n')
b_date = parse_input(i_date)
date = ''

if b_date:
    date = d.today()
else:
    custom_date = input('Enter date to use in format: yyyy-mm-dd\n')
    while not is_valid_date_format(custom_date):
        custom_date = input('Date was not in the correct format or not valid. Please re-enter in format: yyyy-mm-dd\n')

    else:

        date=custom_date
        print(f"Using custom date: {custom_date}")


        





