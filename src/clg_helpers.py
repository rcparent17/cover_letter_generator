import argparse
import yaml

def collect_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--resume-file", required=True)
    parser.add_argument("-c", "--companies-file", required=True)
    parser.add_argument("-t", "--template-file", required=True)
    parser.add_argument("-o", "--output-dir", required=True)
    return parser.parse_args()

def read_companies(yaml_file):
    pass

def to_snake_case(text):
    pass