# how to open a json file and how to read
# data got from: https://gist.github.com/saniyusuf/406b843afdfb9c6a86e25753fe2761f4
# reference: https://www.geeksforgeeks.org/read-json-file-using-python/

# python library
import json

# open json file 1
file_json_1 = open('movie_1.json')
json_1 = json.load(file_json_1)
print('======== print json_1 ========')
print(json_1)
print('======== type of json_1 ========')
print(type(json_1))
print('======== keys of json_1 ========')
print(json_1.keys())
print('======== whats the Title of json_1? ========')
print(json_1['Title'])
print('======== whats the Genre of json_1? ========')
print(json_1['Genre'])

# open json file 2
file_json_2 = open('movie_2.json')
json_2 = json.load(file_json_2)
print('======== print json_2 ========')
print(json_2)
print('======== type of json_2 ========')
print(type(json_2))
print('======== access the first element of list json_2 ========')
print(json_2[0])
print('======== access the last element of list json_2 ========')
print(json_2[-1])

# how many movies do we have on json file 2?
print('======== how many movies do we have on json file 2? ========')
print(len(json_2))

# how many movies do we have on json file 2 that start with the letter T?
print('======== how many movies do we have on json file 2 that start with the letter T? ========')
count_with_first_letter_T = 0
for movie in json_2:
    if movie['Title'][0] == 'T':
        count_with_first_letter_T += 1
print(count_with_first_letter_T)

# how to create a json file
# reference: https://www.kite.com/python/answers/how-to-create-a-json-object-in-python
print('======== how to create a json file ========')
my_json_person = {"name":"Pedro", "CPF":"999999999"}
print(my_json_person)
print(type(my_json_person))
my_json_person_dump = json.dumps(my_json_person)
print(my_json_person_dump)
print(type(my_json_person_dump))

# how to save a json file
# reference: https://stackabuse.com/saving-text-json-and-csv-to-a-file-in-python/
file_json_my_json_person = open('my_json_person.json', 'w')
file_json_my_json_person.write(my_json_person_dump)
file_json_my_json_person.close()
