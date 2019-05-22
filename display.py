

#GLOBALS

def main():
    meanings = get_meanings()
    data = get_data(meanings)
    display(meanings, data)

def display(meaning, data):
    pass

def get_data(meanings):
    data = []
    file = open("data.txt", "r")
    for line in file.readlines():
        this_data = line.strip("\n").split(".")
        for i in range(len(this_data)):
            this_data[i] = int(this_data[i])
        data.append(this_data)
    return data

def get_meanings():
    meanings = []
    file = open("key.txt", "r")
    for line in file.readlines():
        data = line.strip("\n").split(":")[1].split(" ")
        this_dict = {}
        if data[0] == "lihtne":
            this_dict["tag"] = "easy"
            del data[0]
            this_dict["type"] = " ".join(data)
        else:
            this_dict["tag"] = "hard"
            this_dict["type"] = " ".join(data)
        meanings.append(this_dict)
    return meanings


main()
