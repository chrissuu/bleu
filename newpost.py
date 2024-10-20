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

def is_valid_tags_format(tags)->bool:
    '''Returns True if the tags format is valid'''
    
    if tags[0] != '[' or tags[1] != ']':
        return False

    return True 

def parse_input(input):
    '''Changes 'y' or 'n' to boolean values'''
    return True if input == 'y' else False

def parse_post_name(post_name):
    filtered = str(filter(lambda x : x != '-', post_name))

    split_post_name = filtered.split(' ')
    return '-'.join(split_post_name)
    

print('Creating a new post template interactively...')
file_path = ""

'''Setting Date For Post'''

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

'''Setting Post Name'''

i_post_name = input('Enter a file post name\n')
file_post_name = parse_post_name(i_post_name)

'''Setting File Path'''

file_path = str(date) + "-" + str(file_post_name)

'''Setting File Contents'''

f = open(f"_posts/{file_path}", 'w')
f.write('---\n')
f.write('layout: post\n')

# POST TITLE
i_post_title = input('Use file post name as post title? [y/n]\n')
b_post_title = parse_input(i_post_title)

if i_post_title:
    f.write(f"title: {i_post_name}\n")
else:
    post_title = input('Enter a post title:\n')
    f.write(f"title: {post_title}\n")

# POST SUBTITLE
i_subtitle = input('Enter a post subtitle:\n')

while i_subtitle != "":
    i_subtitle = input('An empty subtitle is not valid. Please re-enter:')

f.write(f"subtitle: {i_subtitle}\n")


# POST TAGS
i_tags = input('Enter tags in a pythonic list:\n')

while not is_valid_tags_format(i_tags):
    i_tags = input('Tags were not of the correct format. Please re-enter:')

f.write(f"tags: {i_tags}\n")


# POST TYPE
i_post_name = input('Rigorous post name?'
