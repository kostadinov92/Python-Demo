temperatures = {
    'София': -14,
    'Новосибирск': -31,
    'Таити': 30,
    'Таити1': [30, 2],
    'Варна': {22, 3},
    'Русе': {
        "temperature": -23,
        "humidity": 90,
    },
    'ловдив': None,
    'Пазарджик': None
}

print("-" * 20)
print(temperatures)
print(temperatures['София'])
print(temperatures.get('Бургас'))
print(temperatures.get('Бургас', 'No data'))
print(temperatures.get('София', 'No data'))

# temp_burgas = temperatures.setdefault('Бургас', -2)

print("-" * 20)

key = 'Бургас'
if key in temperatures:
    print(temperatures[key])
else:
    print("No data for {}".format(key))

temperatures['Пловдив'] = 31
print(temperatures)

print("-" * 20)

for city_name in temperatures:
    temperature_data = temperatures[city_name]
    print(city_name, ' -> ', temperature_data)

for neshto in temperatures.items():
    key, value = neshto
    print(neshto)
    print(key)
    print(value)

for city_name, temperature_data in temperatures.items():
    print(city_name, ' -> ', temperature_data)

for temperature_data in temperatures.values():
    print(temperature_data)
