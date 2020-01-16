import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='The path to the export file')
    parser.add_argument('--format', default=json,choices=[json,csv], type=str.lower(), help='Choose which format should be the output in')
    return parser
