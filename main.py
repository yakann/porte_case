# This is a sample Python script.
import pymongo
import create_collection
import operator


class Sinif():

    def __init__(self):
        # Database connection
        self.myclients = pymongo.MongoClient(
            "mongodb+srv://mahmut:123@cluster0.3ycuu.mongodb.net/PorteDB?retryWrites=true&w=majority" )
        self.mydb = self.myclients["PorteDB"]
        self.control_dict = {"X": 0, "Y": 0, "Z": 0}
        self.output_collection = self.mydb["Output"]

    def bul(self, item, args):

        args.remove(item)
        for j in args:
            query = self.mydb.Companies.find({"country_name": item}, {"X": 1, "Y": 1, "Z": 1, "_id": 0})[0]

            val1, _ = self.get_min_value(self.control_dict)

            val = self.control_dict[val1]

            for key, value in {k: v for k, v in sorted(query.items(), key=lambda item: item[1])}.items():
                if val == self.control_dict[key]:
                    self.output_collection.insert_one({"FROM_COUNTRY": item, "TO_COUNTRY": j, "SHIPMENT_COMPANY": key, "CARGO_AMONT": value})
                    self.control_dict[key] = self.control_dict[key] + 1
                    break

        args.append(item)

    @staticmethod
    def get_min_value(query):
        min_value = min(query.items(), key=operator.itemgetter(1))[0]
        return min_value, query[min_value]

    def country_function(self):
        country_list = []
        for i in self.mydb.Companies.find({}, {"country_name": 1, "_id": 0}):
            country_list.append(i["country_name"])
        return country_list

    def inc_processing_function(self, count):
        sum_process = count * (count - 1)

        return sum_process % 3

    @property
    def print_output(self):
        for i in self.mydb.Output.find({}, {"_id": 0} ).sort([("FROM_COUNTRY", 1), ("TO_COUNTRY", 1)]):
            print(i)

    @property
    def print_dict(self):
        return self.control_dict


if __name__ == '__main__':

    instance = create_collection.CreateCollections()

    sinif = Sinif()
    country_list = sinif.country_function()
    inc_processing = sinif.inc_processing_function(instance.get_deger)

    for i in sinif.mydb.Companies.find({}, {"country_name": 1, "_id": 0}):

        sinif.bul(i["country_name"], country_list)

    sinif.print_output
    print(sinif.print_dict)

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
