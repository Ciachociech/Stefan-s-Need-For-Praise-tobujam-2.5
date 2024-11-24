import json
import time


def save_statistics_to_json(statistics, name="stefan", extension=".dat"):
    statistics.timestamp = time.time()
    file = open(name + extension, "w")
    file.write(json.dumps(statistics.__dict__))
    file.close()