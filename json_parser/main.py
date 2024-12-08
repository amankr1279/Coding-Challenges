import argparse

def validity_check(json: str):
    pass

def read_contents(file_path : str):
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="JSON Parser",
        description="Python script to parse json files"
    )

    parser.add_argument("-f",
                        action="store_true",
                        required=False)

    parser.parse_args()
    contents = read_contents("hello")