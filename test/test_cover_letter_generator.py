import sys, os
sys.path.append(os.path.join(os.getcwd(), "src"))

import clg_helpers
from clg_test_fixtures import *
import pytest

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

def test_clg_constructor(generator, companies_yaml):
    assert generator.output_dir == "out"
    assert generator.companies == clg_helpers.read_companies(companies_yaml)
    assert generator.resume_file == "deps/reilly_parent_devops_resume.pdf"
    clean_tmpdir()

def test_generate_letter(generator, company):
    template = "{APPLICANT_NAME}#{COMPANY_NAME}#{COMPANY_LOCATION}#{JOB_TITLE}\n{REQUIREMENTS}\n{QUALIFICATIONS}"
    expected_letter_path = "out/cover_letters/reilly_parent_comp1_freeloader_cover_letter.pdf"
    generator.generate_letter(template, company)
    assert os.path.exists(expected_letter_path)
    assert os.path.getsize(expected_letter_path) > 0
    os.remove(expected_letter_path)

@pytest.mark.parametrize("cover_letter_file", [
    "reilly_parent_comp1_freeloader_cover_letter.pdf"
])
def test_output_merged_pdf(generator, company, cover_letter_file):
    expected_resume_path = "out/cover_letters/reilly_parent_comp1_freeloader_cover_letter.pdf"
    generator.output_merged_pdf(company, cover_letter_file)
    assert os.path.exists(expected_resume_path)
    assert os.path.getsize(expected_resume_path) > 0
    os.remove(expected_resume_path)