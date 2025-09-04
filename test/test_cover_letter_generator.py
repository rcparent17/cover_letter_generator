import sys, os
sys.path.append(os.path.join(os.getcwd(), "src"))
from cover_letter_generator import CoverLetterGenerator
import clg_helpers
from clg_test_fixtures import *
import pytest

@pytest.fixture
def company(companies_yaml):
    companies = clg_helpers.read_companies(companies_yaml)
    yield companies[0]

@pytest.fixture
def generator():
    yield CoverLetterGenerator("deps/template.html", "deps/reilly_parent_devops_resume.pdf", "deps/companies.yaml", "out")

def test_generate_letter_filename(generator, company):
    assert generator._generate_letter_filename(company) == "reilly_parent_comp1_freeloader_cover_letter.pdf"

def test_generate_resume_filename(generator, company):
    assert generator._generate_resume_filename(company) == "reilly_parent_comp1_freeloader_resume.pdf"

def test_populate_template(generator):
    template = "{APPLICANT_NAME}#{COMPANY_NAME}#{COMPANY_LOCATION}#{JOB_TITLE}\n{REQUIREMENTS}\n{QUALIFICATIONS}"
    expected_requirements = "<li>eat food</li>\n<li>sleep</li>\n<li>die</li>\n<li>ascend</li>"
    expected_qualifications = "<li>i eat</li>\n<li>i sleep</li>\n<li>i will die</li>\n<li>i will ascend</li>"
    expected_populated_template = "\n".join(["no one#comp1#nowhere#freeloader", expected_requirements, expected_qualifications])
    assert generator._populate_template(template) == expected_populated_template

def test_clg_constructor(generator):
    pass

def test_generate_letter(generator):
    pass

def test_output_merged_pdf(generator):
    pass