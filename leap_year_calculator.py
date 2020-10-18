#DEFINE LEAP YEAR // A year is a leap year if it has an additional day that makes the number of days 366. This additional day is added in February (29)

# A leap year occurs once every for years

#HOW TO DETERMINE IF A YEAR IS A LEAP YEAR OR NOT,
#if a year is divisible by 4 without any remainder
#if a year is divisible by 4, but not by 100
#if a year is divisible by 100, but not by 400


year = int(input('Enter birth year :'))

is_a_leap_year = (year % 4) == 0

year_is_a_leap_year = (year % 100) == 0

also_a_leap_year = (year % 400) == 0

was_born_in_a_leap_year = is_a_leap_year and year_is_a_leap_year and also_a_leap_year

was_not_born_in_a_leap_year = not bool(was_born_in_a_leap_year) 

print('You were born in a leap year :', was_born_in_a_leap_year)
print('You were not born in a leap year :', was_not_born_in_a_leap_year)