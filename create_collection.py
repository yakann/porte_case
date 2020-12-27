import pymongo


class CreateCollections:
    # Database connection
    def __init__(self):

        self.myclients = pymongo.MongoClient("mongodb+srv://mahmut:123@cluster0.3ycuu.mongodb.net/PorteDB?retryWrites=true&w=majority")
        self.mydb = self.myclients["PorteDB"]

        self.return_count()

        self.deger = self.mydb.Companies.count_documents({})

    def return_count(self):
        country_list = [
            {"id": "1", "country_name": "A", "X": 10, "Y": 20, "Z": 15},
            {"id": "2", "country_name": "B", "X": 8, "Y": 14, "Z": 22},
            {"id": "3", "country_name": "C", "X": 30, "Y": 25, "Z": 20},
            {"id": "4", "country_name": "D", "X": 44, "Y": 16, "Z": 28},
            {"id": "5", "country_name": "E", "X": 15, "Y": 25, "Z": 35},
            {"id": "6", "country_name": "F", "X": 38, "Y": 29, "Z": 19},
            {"id": "7", "country_name": "G", "X": 43, "Y": 29, "Z": 19},
            {"id": "8", "country_name": "H", "X": 9, "Y": 29, "Z": 19}
        ]

        companies_collection = self.mydb["Companies"]
        result = companies_collection.insert_many(country_list)
        result.inserted_ids

    @property
    def get_deger(self):
        return self.deger