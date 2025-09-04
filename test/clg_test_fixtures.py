import sys, os

sys.path.append(os.path.join(os.getcwd(), "src"))
from cover_letter_generator import CoverLetterGenerator
import clg_helpers

import pytest

TMP_FILES = []

@pytest.fixture
def companies_yaml(tmpdir):
    companies_yaml = '''applicant_name: "no one"
companies:
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
    TMP_FILES.append(tmp_file_path)
    with open(tmp_file_path, "w") as tmp_yaml_file:
        tmp_yaml_file.write(companies_yaml)
    yield tmp_file_path

@pytest.fixture
def invalid_yaml(tmpdir):
    companies_yaml = ''':
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
    tmp_file_path = tmpdir.join("invalid_companies.yaml")
    TMP_FILES.append(tmp_file_path)
    with open(tmp_file_path, "w") as tmp_yaml_file:
        tmp_yaml_file.write(companies_yaml)
    yield tmp_file_path

@pytest.fixture
def missing_yaml(tmpdir):
    companies_yaml = '''applicant_name: "no one"
companies:
  - name: "comp1"
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
    '''.strip()
    tmp_file_path = tmpdir.join("invalid_companies.yaml")
    TMP_FILES.append(tmp_file_path)
    with open(tmp_file_path, "w") as tmp_yaml_file:
        tmp_yaml_file.write(companies_yaml)
    yield tmp_file_path

@pytest.fixture
def company(companies_yaml):
    companies = clg_helpers.read_companies(companies_yaml)
    clean_tmpdir()
    yield companies[0]

@pytest.fixture
def generator():
    yield CoverLetterGenerator("deps/template.html", "deps/reilly_parent_devops_resume.pdf", "deps/companies.yaml", "out", "no one")

def clean_tmpdir():
    global TMP_FILES
    for file in TMP_FILES:
        os.remove(str(file))
    TMP_FILES = []