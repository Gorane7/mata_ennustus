from gorgame import game

#GLOBALS
years = 5
square_size = 30
display_in_order = False

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

def get_topics(meanings):
    topics = {}
    for i, meaning in enumerate(meanings):
        if meaning["type"] in topics.keys():
            if meaning["tag"] == "easy":
                topics[meaning["type"]]["easy"] = i
            else:
                topics[meaning["type"]]["hard"] = i
        else:
            if meaning["tag"] == "easy":
                topics[meaning["type"]] = {"easy": i, "hard": None}
            else:
                topics[meaning["type"]] = {"easy": None, "hard": i}
    return topics

meanings = get_meanings()
data = get_data(meanings)
print(meanings)
print(data)



if display_in_order:
    y_size = square_size*(years + 1)
    size = (1000, y_size)
    game = game.Game(size)

    game.screen.window.add_component([0, 0], [200, y_size], "black", 1, "data", window = True)
    game.screen.window.add_component([200, 0], [800, y_size], "white", 1, "display", window = True)

    game.screen.window.get("data").add_component([0, 0], [200, 30], "black", 1, "current", textbox = True)

    for i in range(years):
        game.screen.window.get("display").add_component([0, i*square_size], [800, square_size], "black", 1, "year: " + str(i + 2014), window = True)
        for j, topic in enumerate(data[i]):
            if meanings[topic]["tag"] == "easy":
                this_colour = "green"
            else:
                this_colour = "red"
            game.screen.window.get("display").get("year: " + str(i + 2014)).add_component([j*square_size, 0], [square_size, square_size], this_colour, 1, meanings[topic]["type"])
        while True:
            game.loop()
            game.screen.window.get("data").get("current").add_text(str(game.screen.current_entity), "green")
else:
    x_display = square_size*(years + 1)
    size = (400 + x_display, 700)
    game = game.Game(size)

    game.screen.window.add_component([0, 0], [400 + years*square_size, 700], "black", 1, "data", window = True)
    game.screen.window.add_component([400 + years*square_size, 0], [square_size, 700], "white", 1, "display", window = True)

    topics = get_topics(meanings)

    for i, (topic, values) in enumerate(topics.items()):
        game.screen.window.get("data").add_component([0, i*square_size], [400 + years*square_size, square_size], "grey", 1, topic, window = True)
        game.screen.window.get("data").get(topic).add_component([0, 0], [400, square_size], "black", 1, topic + "text", textbox = True)
        game.screen.window.get("data").get(topic).get(topic + "text").add_text(topic, "green")

    for i, year in enumerate(data):
        for topic in year:
            if meanings[topic]["tag"] == "easy":
                colour = "green"
            else:
                colour = "red"
            game.screen.window.get("data").get(meanings[topic]["type"]).add_component([400 + i*square_size, 0], [square_size, square_size], colour, 1, "box")

    while True:
        game.loop()
