

def parse(str):
    str = str.strip()
    if str[0] == "-":
        return ("a", "b")

    return {
        "map": {
            "field1": "value1",
            "field2": "value2"
        }
    }


def parse_file(filename):
    pass


def parse_files(filenames):
    pass


def parse_dir(dirname):
    pass