import numpy as np
country_name = ['Iran', 'Ethiopia', 'Bangladesh', 'Sudan', 'Poland', 'Russia', 'Uganda', 'Pakistan', 'Germany', 'Turkey', 'India', 'United States', 'Brazil', 'China', 'Indonesia', 'Nigeria', 'Japan', 'Mexico', 'France', 'United Kingdom', 'Italy', 'South Africa', 'South Korea', 'Canada', 'Australia', 'Argentina', 'Spain', 'Ukraine', 'Colombia', 'Netherlands', 'Saudi Arabia', 'Egypt', 'Peru', 'Iraq', 'Philippines', 'Thailand', 'Sweden', 'Norway', 'Belgium', 'Switzerland', 'Austria', 'Denmark', 'Finland', 'Israel', 'Greece', 'Czech Republic', 'Portugal', 'Hungary', 'Ireland', 'Romania', 'New Zealand', 'Singapore', 'Malaysia', 'Venezuela', 'Chile', 'Kazakhstan', 'Morocco', 'Algeria', 'Vietnam', 'Tanzania', 'Kenya', 'Angola', 'Ghana', 'Zimbabwe', 'Tunisia', 'Jordan', 'Lebanon']

countries_sizes = {
    'Iran': {'size': 1745150},
    'Ethiopia': {'size': 1129300},
    'Bangladesh': {'size': 147630},
    'Sudan': {'size': 1886068},
    'Poland': {'size': 322575},
    'Russia': {'size': 17098242},
    'Uganda': {'size': 241038},
    'Pakistan': {'size': 796095},
    'Germany': {'size': 357588},
    'Turkey': {'size': 783562},
    'India': {'size': 3287263},
    'United States': {'size': 9831510},
    'Brazil': {'size': 8514215},
    'China': {'size': 9600013},
    'Indonesia': {'size': 1904569},
    'Nigeria': {'size': 923768},
    'Japan': {'size': 377973},
    'Mexico': {'size': 1964375},
    'France': {'size': 551695},
    'United Kingdom': {'size': 243610},
    'Italy': {'size': 302073},
    'South Africa': {'size': 1221037},
    'South Korea': {'size': 100210},
    'Canada': {'size': 9879750},
    'Australia': {'size': 7692024},
    'Argentina': {'size': 2780400},
    'Spain': {'size': 505990},
    'Ukraine': {'size': 603550},
    'Colombia': {'size': 1141749},
    'Netherlands': {'size': 41543},
    'Saudi Arabia': {'size': 2149690},
    'Egypt': {'size': 1001450},
    'Peru': {'size': 1285220},
    'Iraq': {'size': 438317},
    'Philippines': {'size': 300000},
    'Thailand': {'size': 510890},
    'Sweden': {'size': 447430},
    'Norway': {'size': 385203},
    'Belgium': {'size': 30528},
    'Switzerland': {'size': 41290},
    'Austria': {'size': 83879},
    'Denmark': {'size': 42920},
    'Finland': {'size': 338440},
    'Israel': {'size': 22145},
    'Greece': {'size': 131957},
    'Czech Republic': {'size': 78867},
    'Portugal': {'size': 92212},
    'Hungary': {'size': 93030},
    'Ireland': {'size': 84421},
    'Romania': {'size': 238397},
    'New Zealand': {'size': 267710},
    'Singapore': {'size': 719},
    'Malaysia': {'size': 330345},
    'Venezuela': {'size': 912050},
    'Chile': {'size': 756950},
    'Kazakhstan': {'size': 2725000},
    'Morocco': {'size': 446550},
    'Algeria': {'size': 2381740},
    'Vietnam': {'size': 331690},
    'Tanzania': {'size': 947300},
    'Kenya': {'size': 580370},
    'Angola': {'size': 1246700},
    'Ghana': {'size': 238540},
    'Zimbabwe': {'size': 390760},
    'Tunisia': {'size': 163610},
    'Jordan': {'size': 89342},
    'Lebanon': {'size': 10452},}

def sort_sizes(countries_sizes):
    total_sizes = {}
    for country, data in countries_sizes.items():
        total_sizes[country] = data['size']
    sorted_sizes = sorted(total_sizes.items(), key=lambda x: x[1], reverse=True)
    return sorted_sizes

sorted_sizes = sort_sizes(countries_sizes)
for country, total in sorted_sizes:
    print(country, ':', total)

countries_sizes_two = {}

for country_name in ['Canada','Australia','South Africa', 'Turkey', 'France', 'Spain', 'Sweden', 'Norway', 'Finland','Italy','New Zealand','United Kingdom','Hungary','Portugal','Ireland','Czech Republic','Denmark','Netherlands','Belgium']:
    countries_sizes_two[country_name] = {'size': countries_sizes[country_name]['size']}

total_size = sum(country_data['size'] for country_data in countries_sizes_two.values())

for country_name, country_data in countries_sizes_two.items():
    country_size = country_data['size']
    percentage = (country_size / total_size) * 100
    print(f"{country_name} is {percentage:.2f}% of the total size.")



total_size = sum(country_data['size'] for country_data in countries_sizes_two.values())

with open('/Users/rohitdraman/Downloads/new refugee numbers.csv', 'w') as f:
    for country_name, country_data in countries_sizes_two.items():
        country_size = country_data['size']
        percentage = (country_size / total_size)
        refugees = (percentage) * (10.61/2)
        print(f"{country_name}: {refugees:.2f}")
        f.write(f"{country_name}, {refugees:.2f}\n")
        print(country_name,refugees*2275)



#expected price
2275