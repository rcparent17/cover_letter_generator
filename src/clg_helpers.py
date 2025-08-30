import argparse
import yaml

def collect_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--resume-file", required=True)
    parser.add_argument("-c", "--companies-file", required=True)
    parser.add_argument("-t", "--template-file", required=True)
    parser.add_argument("-o", "--output-dir", required=True)
    return parser.parse_args(args=args)

def read_companies(yaml_file):
    companies = []
    with open(yaml_file, "r") as companies_file:
        companies_yaml = yaml.safe_load(companies_file)
    for company in companies_yaml["companies"]:
        companies.append(company)
    return companies

def to_snake_case(text):
    return text.lower().replace(" ", "_")