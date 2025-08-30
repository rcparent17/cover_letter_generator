import sys, os
sys.path.append(os.path.join(os.getcwd(), "src"))
from clg_helpers import to_snake_case, collect_args, read_companies
import pytest
import shutil
import yaml

@pytest.fixture
def companies_yaml(tmpdir):
    companies_yaml = '''companies:
  - name: "comp1"
    location: "nowhere"
    job_title: "freeloader"
    requirements:
      - "eat food"
      - "sleep"
      - "die"
      - "ascend"
    qualifications:
      - "i eat"
      - "i sleep"
      - "i will die"
      - "i will ascend"
  - name: "comp2"
    location: "anywhere"
    job_title: "anything"
    requirements:
      - "wake up"
      - "eat"
      - "eat again"
      - "sleep"
    qualifications:
      - "i wake up"
      - "i eat"
      - "i still eat"
      - "i sleep"
    '''.strip()
    tmp_file_path = tmpdir.join("tmp_companies.yaml")
    with open(tmp_file_path, "w") as tmp_yaml_file:
        tmp_yaml_file.write(companies_yaml)
    yield tmp_file_path

def test_read_companies(companies_yaml):
    companies = read_companies(companies_yaml)
    assert len(companies) == 2
    assert companies[0]["name"] == "comp1" and companies[1]["name"] == "comp2"
    assert companies[0]["requirements"][2] == "die"

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