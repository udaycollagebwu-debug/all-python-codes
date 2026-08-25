collage ={
   "student":{
        'name':'uday sankar singha',
        "cours":'python for machin learning',
        'roll':418,
        'age':19
    },
   "teacher":{
       'name':'Sabyasachi Chandra',
       'age':35,
       'id':1205
   },
   'cours_details':{
       'cours name':'python for machin learning',
       'cours code':130019
   }
}

print(collage)
# pop operaction on the dictionare
collage.pop('cours_details')

print("another")
print(collage)
# popitem operaction on the dictionare
print("another")
print("This is the pop element :",collage.popitem())
print(collage)
print("another")
#clear operation in dic
print("another")
collage.clear()
print("The clear dic is :",collage)