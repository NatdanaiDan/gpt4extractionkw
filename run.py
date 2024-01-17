import g4f
from utl import MessageStorage
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

print("Start")
client = MongoClient(
    "mongodb+srv://64015037:2YqYA4kjsTImOMmY@keytoad.nslb9f9.mongodb.net/?retryWrites=true&w=majority",
    server_api=ServerApi("1"),
)
db = client["keytoad"]
collection = db["test"]
collection_cosmetic = db["cosmetic"]
g4f.debug.logging = True  # Enable debug logging
g4f.debug.version_check = False  # Disable automatic version checking
print(g4f.Provider.Bing.params)  # Print supported args for Bing
iteration_counter = 0


def getdata():
    while True:
        data = list(collection_cosmetic.aggregate([{"$sample": {"size": 1}}]))
        # check "output" is already in collection or not
        if not collection.find_one({"input": data[0]["output"]}):
            return data[0]["output"]
        else:
            print("Duplicate")


for i in range(1, 1001):
    item = getdata()
    dict_input = {"role": "user"}
    dict_input["content"] = "input : " + item
    MessageStorage.append(dict_input)
    while True:
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_35_long,
            messages=MessageStorage,
        )
        if "<s>" in response and "</s>" in response:
            break
        else:
            print("Error")
            print(response)
    MessageStorage.pop()
    print("--------------------------------------------------")
    print(response)
    print("--------------------------------------------------")
    # print(MessageStorage)
    collection.insert_one({"input": item, "output": response})

    # Increment the counter
    iteration_counter += 1

    # Check if the counter is a multiple of 100
    if iteration_counter % 50 == 0:
        print(f"Iteration {iteration_counter} completed.")
