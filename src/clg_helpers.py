import argparse
import yaml


def collect_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--resume-file", required=True)
    parser.add_argument("-c", "--companies-file", required=True)
    parser.add_argument("-t", "--template-file", required=True)
    parser.add_argument("-o", "--output-dir", required=True)
    parser.add_argument("-a", "--applicant-name", required=True)
    return parser.parse_args(args=args)


def read_companies(yaml_file):
    companies = []
    if is_valid_companies_yaml(yaml_file):
        with open(yaml_file, "r") as companies_file:
            companies_yaml = yaml.safe_load(companies_file)
        for company in companies_yaml["companies"]:
            companies.append(company)
    return companies


def get_applicant_name(yaml_file):
    name = ""
    if is_valid_companies_yaml(yaml_file):
        with open(yaml_file, "r") as companies_file:
            name = yaml.safe_load(companies_file)["applicant_name"]
    return name


def to_snake_case(text):
    return text.lower().replace(" ", "_")


def is_valid_companies_yaml(yaml_file):
    companies = []
    applicant_name = ""
    try:
        with open(yaml_file, "r") as companies_file:
            companies_yaml = yaml.safe_load(companies_file)
            # throw error if no applicant name found
            try:
                applicant_name = companies_yaml["applicant_name"]
            except KeyError:
                raise yaml.parser.ParserError()
        for company in companies_yaml["companies"]:
            companies.append(company)
    except yaml.parser.ParserError:
        raise yaml.error.YAMLError("Invalid input YAML")
    for company in companies:
        # conditions that would cause problems in the program
        try:
            if any(
                [
                    applicant_name == "" or applicant_name == None,
                    company["name"] == "" or company["name"] == None,
                    company["location"] == "" or company["location"] == None,
                    company["job_title"] == "" or company["job_title"] == None,
                    company["requirements"] == [] or company["requirements"] == None,
                    company["qualifications"] == []
                    or company["qualifications"] == None,
                    not len(company["requirements"]) == len(company["qualifications"]),
                    "" in company["requirements"] or "" in [company["qualifications"]],
                ]
            ):
                raise yaml.error.YAMLError("Invalid entry in YAML file")
        except KeyError:
            raise yaml.error.YAMLError("Invalid entry in YAML file")

    return True
