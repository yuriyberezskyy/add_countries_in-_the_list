travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, visited, cities):
  new_country = {}
  new_country = {
          "country": country,
          "visits": visited,
          "cities": cities
        }
  travel_log.append(new_country)

#🚨 Do not change the code below
add_new_country("Ukraine", 2, ["Kiyv", "Lviv"])
print(travel_log)



