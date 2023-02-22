import json
import pickle
import _json

pupils = {'1a': 'Ivanov', '1b': 'Petrov'}



with open('pupils.pickle','wb') as pupils_file:
   pupils_dump = pickle.load(pupils_file)

print('Done writing dump!')


with open('pupils.pickle', 'rb') as pupils_file:
   pupils_dump = pickle.load(pupils_life)

print(pupils_dump)



print('*'*50)


with open ('pupils.json', 'w') as pupil file:
   json.dump(pupils, pupils_file)

print('Done writing json!')

with open ('pupils.json', 'r') as pupils_ file:
   pupils_json = json.load(pupils_file)

   print (pupils_json)
















