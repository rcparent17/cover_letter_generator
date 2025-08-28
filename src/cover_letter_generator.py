import sys, os

import yaml
import pdfkit, pypdf
import argparse

'''
COMPANY YAML ENTRY TEMPLATE:

- name: ""
  location: ""
  job_title: ""
  requirements:
    - ""
    - ""
    - ""
    - ""
  qualifications:
    - ""
    - ""
    - ""
    - ""

'''

# TODO
class CoverLetterGenerator:
    def __init__(self, template_file="deps/template.txt", resume_file="deps/reilly_parent_devops_resume.pdf", companies_file="deps/companies.yaml"):
        if not (os.path.exists(template_file) or os.path.exists(resume_file) or os.path.exists(companies_file)):
            raise FileExistsError("One or more provided files does not exist.")
        
        # read template
        self.template = ""
        with open(template_file, "r") as template:
            self.template = "".join(template.readlines())
        
def main():
    generator = CoverLetterGenerator()

if __name__ == "__main__":
    main()