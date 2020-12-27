import pymongo


class CreateCollections:
    # Database connection
    myclients = pymongo.MongoClient("mongodb+srv://mahmut:123@cluster0.3ycuu.mongodb.net/PorteDB?retryWrites=true&w=majority")
    mydb = myclients["PorteDB"]

    # Collections
    companies_collection = mydb["Companies"]
    countries_collection = mydb["Countries"]
    currency_collection = mydb["CurrencyTypes"]
    cost_collection = mydb["ShipmentCost"]

    # my_collection = [companies_collection, countries_collection, currency_collection, cost_collection]

    companies_list = [
        {"id": "1", "shipment_name": "X"},
        {"id": "2", "shipment_name": "Y"},
        {"id": "3", "shipment_name": "Z"}
    ]

    country_list = [
        {"id": "1", "country_name": "A"},
        {"id": "2", "country_name": "B"},
        {"id": "3", "country_name": "C"},
        {"id": "4", "country_name": "D"},
        {"id": "5", "country_name": "E"},
        {"id": "6", "country_name": "F"}
    ]

    currency_list = [
        {"id": "1", "currency_type": "USD", "currency_symbol": "$"},
        {"id": "2", "currency_type": "EUR", "currency_symbol": "€"},
        {"id": "3", "currency_type": "TRY", "currency_symbol": "₺"}
    ]

    shipment_cost_list = [
        {"id": "1", "country_id": "1", "cost": [
            {"company_id": "1", "currency_id": "1", "amount": 10},
            {"company_id": "2", "currency_id": "1", "amount": 20},
            {"company_id": "3", "currency_id": "1", "amount": 15}
        ], "cheapest_way": "X"},

        {"id": "2", "country_id": "2", "cost": [
            {"company_id": "1", "currency_id": "1", "amount": 8},
            {"company_id": "2", "currency_id": "1", "amount": 14},
            {"company_id": "3", "currency_id": "1", "amount": 22}
        ], "cheapest_way": "X"},

        {"id": "3", "country_id": "3", "cost": [
            {"company_id": "1", "currency_id": "1", "amount": 30},
            {"company_id": "2", "currency_id": "1", "amount": 25},
            {"company_id": "3", "currency_id": "1", "amount": 20}
        ], "cheapest_way": "Z"},

        {"id": "4", "country_id": "4", "cost": [
            {"company_id": "1", "currency_id": "1", "amount": 44},
            {"company_id": "2", "currency_id": "1", "amount": 16},
            {"company_id": "3", "currency_id": "1", "amount": 28}
        ], "cheapest_way": "Y"},

        {"id": "5", "country_id": "5", "cost": [
            {"company_id": "1", "currency_id": "1", "amount": 15},
            {"company_id": "2", "currency_id": "1", "amount": 25},
            {"company_id": "3", "currency_id": "1", "amount": 35}
        ], "cheapest_way": "X"},

        {"id": "6", "country_id": "6", "cost": [
            {"company_id": "1", "currency_id": "1", "amount": 9},
            {"company_id": "2", "currency_id": "1", "amount": 29},
            {"company_id": "3", "currency_id": "1", "amount": 19}
        ], "cheapest_way": "X"}
    ]

    companies_collection.insert_many(companies_list)
    countries_collection.insert_many(country_list)
    cost_collection.insert_many(shipment_cost_list)
    currency_collection.insert_many(currency_list)
