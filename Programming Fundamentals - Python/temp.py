countries_list = input().split(', ')
capitals_list = input().split(', ')
result_dictionary = {countries_list[index]: capitals_list[index] for index in range(len(countries_list))}
for country, capital in result_dictionary.items():
    print(f'{country} -> {capital}')
