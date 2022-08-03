import json


def create_log_json(data):
    data = data.split(";", 1)
    data = [data[0], data[1]]
    # print(data)
    with open("data_file.json", "a") as outfile:
        outfile.write(json.dumps(data))
        outfile.write(",")
        outfile.close()
    return data


text = "00:38:16; Inputed rational formula; 6+5"

print(create_log_json(text))


def print_json():
    with open("data_file.json", "r") as read_file:
        data = json.load(read_file)
    return data


print(print_json())

# data = {"00:38:16": " Inputed rational formula; 6+5"}

# with open("data_file.json", "a") as outfile:
#     outfile.write(json.dumps(data))
#     outfile.write(",")
#     outfile.close()


# with open("data_file.json", mode="w", encoding="utf-8") as f:
#     json.dump([], f)

# with open("data_file.json", mode="w", encoding="utf-8") as feedsjson:
#     entry = {"name": args.name, "url": args.url}
#     feeds.append(entry)
#     json.dump(feeds, feedsjson)
