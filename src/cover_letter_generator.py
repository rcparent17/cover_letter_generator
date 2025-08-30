import sys, os

import pdfkit, pypdf

import clg_helpers

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
            self.template = "".join([x.strip() for x in template.readlines()])

def main():
    args = clg_helpers.collect_args()
    generator = CoverLetterGenerator(args.template_file, args.resume_file, args.companies_file, args.output_dir)

if __name__ == "__main__":
    main()