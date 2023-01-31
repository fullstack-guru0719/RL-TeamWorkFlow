companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]

companies.sort(key=lambda company: company[2])

print(companies)