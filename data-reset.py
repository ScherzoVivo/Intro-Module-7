import pickle

fhandle = open("address.dat", "wb")

data = [
    {
    "id" : 1,
    "name" : "Dave Phillips",
    "street" : "1234 Main Street",
    "city" : "St. Louis",
    "state" : "MO",
    "zip-code" : "65465",
    "country" : "USA",
    "phone" : "928.707.7070"
    },
    {
    "id" : 2,
    "name" : "Bob Giggleton",
    "street" : "5534 Bojangles Drive",
    "city" : "Chattanooga",
    "state" : "NY",
    "zip-code" : "84325",
    "country" : "USA",
    "phone" : "526.489.5526"
    },
    {
    "id" : 3,
    "name" : "Tiffany Dinglehopper",
    "street" : "1 Airview Boulevard",
    "city" : "Branson",
    "state" : "MO",
    "zip-code" : "62514",
    "country" : "USA",
    "phone" : "856.229.4476"
    }
]

pickle.dump(data, fhandle)
fhandle.close()

#pickle.dump(data, open("save.p", "wb"))

print("Success!")
