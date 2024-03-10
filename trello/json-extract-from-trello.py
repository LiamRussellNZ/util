import json

f = open("../trello/json-board-export.json")

data = json.load(f)
f.close()
print(data)
def get_all_items_from(key_name, data):
    for key_name in data:
        print(data[key_name])
        if key_name in data and isinstance(data[key_name], dict):
            print(f"{key_name} is a dict")
            for key, value in data[key_name].items():
                print(f'{key}: {value}')
                
def get_all_lists():
    get_all_items_from("lists", data)

    
get_all_lists()
#get_all_items_from("cards", data) 

#print(data)

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

