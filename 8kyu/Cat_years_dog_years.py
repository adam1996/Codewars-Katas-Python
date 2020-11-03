'''
Cat years, Dog years (8kyu)
https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b

I have a cat and a dog.

I got them at the same time as kitten/puppy. That was humanYears years ago.

Return their respective ages now as [humanYears,catYears,dogYears]

NOTES:

humanYears >= 1
humanYears are whole numbers only
Cat Years
15 cat years for first year
+9 cat years for second year
+4 cat years for each year after that
Dog Years
15 dog years for first year
+9 dog years for second year
+5 dog years for each year after that

'''
def human_years_cat_years_dog_years(human_years):
    if human_years == 1: cat_years = 15
    elif human_years == 2: cat_years = 24
    else: cat_years = 24 + (4 * (human_years - 2))

    if human_years == 1: dog_years = 15
    elif human_years == 2: dog_years = 24
    else: dog_years = 24 + (5 * (human_years - 2))

    return [human_years,cat_years,dog_years]


print(human_years_cat_years_dog_years(10))
