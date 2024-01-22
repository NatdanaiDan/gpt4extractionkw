import g4f
from utl import MessageStorage, textsort
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import random

print("Start")
client = MongoClient(
    "mongodb+srv://64015037:2YqYA4kjsTImOMmY@keytoad.nslb9f9.mongodb.net/?retryWrites=true&w=majority",
    server_api=ServerApi("1"),
)
db = client["keytoad"]
collection = db["funirture_kw"]
collection_default = db["funirture"]
providers = [
    g4f.Provider.GeekGpt,
    g4f.Provider.FreeGpt,
    g4f.Provider.FakeGpt,
    g4f.Provider.You,
]
iteration_counter = 0
index_provider = 0
list_tosort = textsort.split("|")


def getdata():
    while True:
        data = list(collection_default.aggregate([{"$sample": {"size": 1}}]))
        # check "output" is already in collection or not
        if not collection.find_one({"input": data[0]["output"]}):
            return data
        else:
            # delete duplicate
            collection_default.delete_one({"output": data[0]["output"]})
            print("Delete duplicate")


while True:
    # count collection_default if empty then break
    if collection_default.count_documents({}) == 0:
        break
    data = getdata()
    item = data[0]["output"]
    dict_input = {"role": "user"}
    dict_input["content"] = "input : " + item
    MessageStorage.append(dict_input)
    while True:
        try:
            provider = providers[index_provider]
            response = g4f.ChatCompletion.create(
                model=g4f.models.gpt_35_long,
                messages=MessageStorage,
                provider=provider,
            )
            for text in textsort.split("|"):
                if text in response:
                    response = response.replace(text, "")

            if (
                "<s>" in response
                and "</s>" in response
                and list_tosort[0] not in response
                and list_tosort[1] not in response
                and list_tosort[2] not in response
                and list_tosort[3] not in response
                and list_tosort[4] not in response
                and list_tosort[5] not in response
                and list_tosort[6] not in response
                and list_tosort[7] not in response
                and list_tosort[8] not in response
                and "<s></s>" not in response
            ):
                break

        except Exception as e:
            print(provider)
            print(e)
            print("Skip this")

        provider = providers[index_provider]
        index_provider += 1
        if index_provider == 4:
            index_provider = 0
    MessageStorage.pop()
    print("--------------------------------------------------")
    print(item)
    print(response)
    print("--------------------------------------------------")
    # print(MessageStorage)
    try:
        related = (
            data[0]["related"]
            .replace("[", "")
            .replace("]", "")
            .replace("'", "")
            .replace(" ", "")
        )
    except:
        related = ""

    collection.insert_one({"input": item, "output": response, "related": related})

    # Increment the counter
    iteration_counter += 1

    # Check if the counter is a multiple of 100
    if iteration_counter % 50 == 0:
        print(f"Iteration {iteration_counter} completed.")
