import g4f
from utl import MessageStorage
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import random

print("Start")
client = MongoClient(
    "mongodb+srv://64015037:2YqYA4kjsTImOMmY@keytoad.nslb9f9.mongodb.net/?retryWrites=true&w=majority",
    server_api=ServerApi("1"),
)
db = client["keytoad"]
collection = db["test"]
collection_cosmetic = db["cosmetic"]
providers = [
    g4f.Provider.GeekGpt,
    g4f.Provider.FreeGpt,
    g4f.Provider.FakeGpt,
    g4f.Provider.You,
]
iteration_counter = 0


def getdata():
    while True:
        data = list(collection_cosmetic.aggregate([{"$sample": {"size": 1}}]))
        # check "output" is already in collection or not
        if not collection.find_one({"input": data[0]["output"]}):
            return data[0]["output"]
        else:
            # delete duplicate
            collection_cosmetic.delete_one({"output": data[0]["output"]})
            print("Delete duplicate")


for i in range(1, 1001):
    item = getdata()
    dict_input = {"role": "user"}
    dict_input["content"] = "input : " + item
    MessageStorage.append(dict_input)
    while True:
        try:
            provider_random = random.choice(providers)
            response = g4f.ChatCompletion.create(
                model=g4f.models.gpt_35_long,
                messages=MessageStorage,
                provider=provider_random,
            )
            if "<s>" in response and "</s>" in response:
                break
        except Exception as e:
            print(provider_random.__name__)
            print(e)
            print("Skip this")

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
