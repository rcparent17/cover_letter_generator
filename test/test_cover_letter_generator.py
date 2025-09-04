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

def test_generate_letter_filename(company):
    assert CoverLetterGenerator._generate_letter_filename(company) == "reilly_parent_comp1_freeloader_cover_letter.pdf"

def test_generate_resume_filename(company):
    assert CoverLetterGenerator._generate_resume_filename(company) == "reilly_parent_comp1_freeloader_resume.pdf"

def test_populate_template(template, company):
    pass

def test_clg_constructor(template_file, resume_file, companies_file, output_dir):
    pass

def test_generate_letter(generator):
    pass

def test_output_merged_pdf(generator):
    pass