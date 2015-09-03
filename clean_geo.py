### Compare the country names in the gdp data and the geo json, then manually correct the geo json
import json

### Reshape PISA data
data = {}
cnt = []
gdp = ["Albania", "Argentina", "Australia", "Austria", "Belgium", "Brazil", "Bulgaria", "Canada", "Chile", "China-Shanghai", "Chinese Taipei", "Colombia", "Costa Rica", "Croatia", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hong Kong-China", "Hungary", "Iceland", "Indonesia", "Ireland", "Israel", "Italy", "Japan", "Jordan", "Kazakhstan", "Korea", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Macao-China", "Malaysia", "Mexico", "Montenegro", "Netherlands", "New Zealand", "Norway", "Peru", "Poland", "Portugal", "Qatar", "Romania", "Russian Federation", "Serbia", "Singapore", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Thailand", "Tunisia", "Turkey", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Vietnam"]

with open('../world_map.json','r') as f:
    data = json.loads(f.read())
for c in data["features"]:
    cnt.append(c['properties']['name'])

# print cnt
for i in gdp:
    if i not in cnt:
        print i

