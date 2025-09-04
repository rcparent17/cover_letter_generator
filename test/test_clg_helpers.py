import sys, os
sys.path.append(os.path.join(os.getcwd(), "src"))
from clg_helpers import to_snake_case, collect_args, read_companies, is_valid_companies_yaml
import pytest
import yaml

from clg_test_fixtures import *

def test_read_companies(companies_yaml):
    companies = read_companies(companies_yaml)
    assert len(companies) == 2
    assert companies[0]["name"] == "comp1" and companies[1]["name"] == "comp2"
    assert companies[0]["requirements"][2] == "die"
    clean_tmpdir()

# these two below tests also cover invalid input testing for is_valid_companies_yaml()

def test_invalid_companies_yaml(invalid_yaml):
    with pytest.raises(yaml.error.YAMLError, match="Invalid input YAML"):
        read_companies(invalid_yaml)
    clean_tmpdir()

def test_missing_companies_yaml(missing_yaml):
    with pytest.raises(yaml.error.YAMLError, match="Invalid company entry in YAML file"):
        read_companies(missing_yaml)
    clean_tmpdir()

def test_is_valid_companies_yaml(companies_yaml):
    assert is_valid_companies_yaml(companies_yaml)
    clean_tmpdir()

def test_to_snake_case():
    assert to_snake_case("One") == "one"
    assert to_snake_case("Reilly Parent") == "reilly_parent"
    assert to_snake_case("Senior DevOps Engineer") == "senior_devops_engineer"

@pytest.mark.parametrize("args", [
    ["-r", "deps/reilly_parent_devops_resume.pdf", "-c", "deps/companies.yaml", "-t", "deps/template.html", "-o", "out"],
    ["--resume-file", "deps/reilly_parent_devops_resume.pdf", "--companies-file", "deps/companies.yaml", "--template-file", "deps/template.html", "--output-dir", "out"]
])
def test_collect_args(args):
    parsed_args = collect_args(args)
    collected = [parsed_args.template_file, parsed_args.resume_file, parsed_args.companies_file, parsed_args.output_dir]
    assert not None in collected
