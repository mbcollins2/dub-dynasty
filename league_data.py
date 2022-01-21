import pickle
from espn_api.basketball import League

league_id = 88932378
year = 2021
swid = '355F8053-8A6C-45DE-9F80-538A6CA5DE8C'
espn_s2 = 'AEBfB5kMxA%2Fe%2BoXPbA15UjYAgeb%2FNj4TjVnyDuvZmvG8nfiUQWkwnT4uy2hEFFA0owGdXprxcUotW4D6hucgXSlbMxHX%2B%2BUP6rQhL0auJI6l351sgglKKGzHKGpt0%2FRhXG190sPtf8IHvkXRo7dyq0IYJb1RPDAOqU0Vrm3WogtTvUeSWVkdZA7VUGEH3dmsYnh3D4mV21YMw1gE2pwQSpLFhuYVtBDtc%2FyTT6o%2FRO8wefkb0D1A4rjId%2FFyoK4BvLgxF5sB0%2FQLU7AJcmJgL4E15c38LQ2Prv3EFi1sFlLxAg%3D%3D'

league = League(league_id=88932378, year=2022, espn_s2=espn_s2, swid=swid)

with open('league.pkl', 'wb') as l:
    pickle.dump(league, l)