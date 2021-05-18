import json

with open('config.json') as json_data:
    data = json.load(json_data)

database = data.get('database')
tables = list(data.get('tables').keys())

for table in tables:
    print('**********************')
    print("Table Name", table)
    all = data['tables'][table]['all']
    query = data['tables'][table]['query']
    clause = data['tables'][table]['clause']

    if all and not(clause):
        sql_query = "SELECT * FROM " + table
        print(sql_query)
        print()

    if query and clause:
        sql_query = "SELECT " + ','.join(query) + " FROM " + table + " WHERE " + list(clause.keys())[0] + " = " + str(list(clause.values())[0])
        print(sql_query)
        print()
