import json

f = open("../../trello-board-extract.json")

data = json.load(f)
f.close()
#print(data)
def debug_helper(key_name, data):
    print(f"Found {len(data[key_name])} {key_name} which is {type(data[key_name])}")

def get_items_from(key_name, data):
    if key_name in data and isinstance(data[key_name], list):
        print(f"Found {len(data[key_name])} {key_name} which are of type: {type(data[key_name])}")
        print(f"Names of the {key_name} are: ")
        for item in data[key_name]:
            if "idList" in item:
                print(f"{item['name']} which is related to {compare_value_to_key(item['idList'], get_list_names_and_ids())}")
                # compare item['idList'] with the keys in list returned from get_list_names_and_ids
                # if match then item['idList'] should be replaced with value

                # write a Python function called "compare_value_to_key" that takes in two arguments
                # the first argument is a number the second is a dict
                # match that number to the key of the dict taken as the second argument 
                # when theres a match return the value of that key
                # else return a string saying "no match found"
            else: 
                print(f"{item['name']}")
            if key_name in data and isinstance(data[key_name], dict):
                print(f"{key_name} is a dict")
                for key, value in data[key_name].items():
                    print(f'{key}: {value}')

def get_list_names_and_ids():
    get_items_from("lists", data)
    try:
        for item in data["lists"]:
            list_names_and_ids = {item["id"]: item["name"] for item in data["lists"]}
            return list_names_and_ids
    except:
        return "can't extract list ids and names"

def compare_value_to_key(number, dictionary):
    if number in dictionary:
        return dictionary[number]
    else:
        return "no match found"

debug_helper("lists", data)
get_items_from("lists", data)
print(get_list_names_and_ids())
list_names_and_ids = get_list_names_and_ids()
get_items_from("cards", data)
#get_all_items_from("cards", data) 

#for key in data:
#    try:
#        for card in data["actions"]:
#            if "data" in card and "text" in card["data"]:
#                print("card text: ", card["data"]["text"])
#            else:
#                print("no text element attached")
#            if "data" in card and "list" in card["data"]:
#                #print("This is attached to the list ", card["data"]["list"])
#                #print("The type of the list is: ", type(card["data"]["list"]))
#                if "data" in card and isinstance(card["data"]["list"], dict):
#                    print("this is a dict")
#                    for key, value in card["data"]["list"].items():
#                        print(f'{key}: {value}')
#            else:
#                print("cant find list attribute")
#            if "data" in card and "card" in card["data"]:
##                print("This is attached to the list ", card["data"]["card"]["name"])
#                print(type(card["data"]["card"]["name"]))
#            #print('This is the action data: ', card["data"])
#            #print(card["name"], " has ", card["attachments"])
#    except:
#            print("Key not found")

