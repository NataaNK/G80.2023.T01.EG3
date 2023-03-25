import json
import os
from pathlib import Path

# NO RUNEAR ESTE TEST PORQUE SE RESETEARÁN TODOS LOS .JSON DENTRO DE LA CARPETA JSON_TEST
# SI ESTÁ SEGURO DE QUE QUIERE EJECUTARLO, CAMBIE LA VARIABLE SECURITY A FALSE

SECURITY = True
NUM_TEST = 66
if not SECURITY:
    for i in range(NUM_TEST):
        file = str(Path.home()) + "/PycharmProjects/G80.2023.T01.EG3/src/json_files/json_tests/mytest"+str(i+1)+".json"

        if os.path.isfile(file):
                os.remove(file)
        data = []
        new_dict = {"OrderID": "03de4c31222c38cbce5957655a0b5f28",
                "ContactEmail": "emaildeprueba@gmail.com"}

        data.append(new_dict)

        with open(file, "w", encoding= "utf8") as file1:
                json.dump(new_dict, file1, indent=2)