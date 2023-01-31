
def get_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)
def first_last(first_name, last_name):
    return f"{first_name},{last_name}"
def last_first(first_name, last_name):
    return f'{last_name} {last_name}'

full_name = get_name('john', 'Doe',first_last)
print( full_name)
full_name = get_name('johb', 'doe', last_first)
print(full_name)