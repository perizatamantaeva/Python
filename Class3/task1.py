def years_to_days(years):
    days = years * 365
    return days

def years_to_weeks(years):
    weeks = years * 52
    return weeks

def years_to_months(years):
    months = years * 12
    return months

def years_to_hours(years):
    hours = years * 365 * 24
    return hours


num_of_years = int(input("Enter the number of years: "))

num_of_days = years_to_days(num_of_years)
num_of_weeks = years_to_weeks(num_of_years)
num_of_months = years_to_months(num_of_years)
num_of_hours = years_to_hours(num_of_years)

print(f"{num_of_years} years is equal to: ")
print(f"{num_of_days} days.")
print(f"{num_of_weeks} weeks.")
print(f"{num_of_months} months.")
print(f"{num_of_hours} hours.")

