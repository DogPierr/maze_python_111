import os.path
import constants


def save(map, passes, name=constants.SAVE_NAME):
    add_number = 0
    while os.path.isfile(constants.SAVE_DIR + '/' + name):
        if not add_number:
            add_number += 1
            name += str(add_number)
        else:
            add_number += 1
            name = name[0:len(name) - len(str(add_number))] + str(add_number)
    with open(constants.SAVE_DIR + "/" + name, "w") as file:
        file.write(str(map) + "\n\n" + str(passes))
