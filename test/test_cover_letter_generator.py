import sys, os
sys.path.append(os.path.join(os.getcwd(), "src"))
from cover_letter_generator import CoverLetterGenerator
from clg_test_fixtures import *
import pytest

def test_generate_letter_filename(company):
    pass

def test_generate_resume_filename(company):
    pass

def test_populate_template(template, company):
    pass

def test_clg_constructor(template_file, resume_file, companies_file, output_dir):
    pass

def test_generate_letter(generator):
    pass

def test_output_merged_pdf(generator):
    pass