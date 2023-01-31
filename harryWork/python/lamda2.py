def get_full_name(first, last, formatter):
    return formatter(first, last)
full_name = get_full_name(
    'john',
    'Doe',
    lambda first, last: f"{first} {last}"
)
print(full_name)