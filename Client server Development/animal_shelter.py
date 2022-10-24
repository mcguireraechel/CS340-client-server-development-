# python lib code...

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,username,password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:46186/?authMechanism=DEFAULT&authSource=AAC' % (username, password))
       # self.client = MongoClient('mongodb:// localhost:46186')
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animaldb.insert(data)  # data should be dictionary 
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD

    def read_all(self, data):
        cursor = self.database.animaldb.find(data, {'_id' : False})
        return cursor
    
    def read(self, data):
        if data is not None:
            return self.database.animaldb.find_one(data)
        else:
            print("Nothingto read because data perameter is empty")
            return False 
    
    
# Create method to implement the U in CRUD
    def update_data(self, data,updatedData):
        print("HIT")
        if data is not None:
            self.database.animaldb.update_one({data}, {"$set":{updatedData}})
            #make it in JSON format
            obj = json.loads(cursor)
            json_formatted = json.dumps(obj, indent=4)
            return json_formatted
        else:
            raise Exception("Nothing to update")
        
#Create method to implement the D in CRUD 
    def delete(self, data):
        if data is not None:
            self.database.animaldb.delete_one(data)
            
            return True
        else:
            raise Exception("Nothing to delete")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        