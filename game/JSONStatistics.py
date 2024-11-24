import json
import time

import game


def save_statistics_to_json(statistics, name="stefan", extension=".dat"):
    statistics.timestamp = time.time()
    file = open(name + extension, "w")
    file.write(json.dumps(statistics.__dict__))
    file.close()

def load_statistics_from_json(name="stefan", extension=".dat"):
    file = None
    try:
        file = open(name + extension, "r")
    except ValueError:
        return None
    json_content = ""
    for line in file.readlines():
        json_content += line
    print(json_content)
    json_dict = json.loads(json_content)

    statistics = game.GameStatistics()
    statistics.frames = json_dict["frames"]
    statistics.attention = json_dict["attention"]
    statistics.power = json_dict["power"]
    statistics.destruction = json_dict["destruction"]
    statistics.satisfaction = json_dict["satisfaction"]
    statistics.currency = json_dict["currency"]
    statistics.needs_upgrade = json_dict["needs_upgrade"]
    statistics.feeding_upgrade = json_dict["feeding_upgrade"]
    statistics.petting_upgrade = json_dict["petting_upgrade"]
    statistics.cleaning_upgrade = json_dict["cleaning_upgrade"]
    statistics.poops = 0

    # simulate time when game is not running
    time_diff = time.time() - json_dict["timestamp"]
    statistics.update(int(60 * time_diff))
    statistics.timestamp = time.time()

    # ensure backup save is made and delete current save file data
    save_statistics_to_json(statistics, extension=".dat.bkp")
    open(name + ".dat", "w")
    return statistics