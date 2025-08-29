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
    def __init__(self, template_file, resume_file, companies_file, output_dir):
        if not (os.path.exists(template_file) or os.path.exists(resume_file) or os.path.exists(companies_file)):
            raise FileExistsError("One or more provided files does not exist.")
        
        # read template
        self.template = ""
        with open(template_file, "r") as template:
            self.template = "".join(template.readlines())

def collect_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--resume-file", required=True)
    parser.add_argument("-c", "--companies-file", required=True)
    parser.add_argument("-t", "--template-file", required=True)
    parser.add_argument("-o", "--output-dir", required=True)
    return parser.parse_args()

def main():
    args = collect_args()
    generator = CoverLetterGenerator(args.template_file, args.resume_file, args.companies_file, args.output_dir)

if __name__ == "__main__":
    main()