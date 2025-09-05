import sys, os

import pypdf

from weasyprint import HTML

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
    def __init__(self, template_file, resume_file, companies_file, output_dir, applicant_name):
        if not (os.path.exists(template_file) or os.path.exists(resume_file) or os.path.exists(companies_file)):
            raise FileExistsError("One or more provided files does not exist.")
        
        # read template
        self.template = ""
        with open(template_file, "r") as template:
            self.template = "".join([x.strip() for x in template.readlines()])

        self.companies = clg_helpers.read_companies(companies_file)
        self.resume_file = resume_file
        self.output_dir = output_dir
        self.applicant_name = applicant_name

    def generate_letter(self, company):
        letter_dir = f"{self.output_dir}/cover_letters"
        # create dir if it doesn't exist
        os.makedirs(letter_dir, exist_ok = True)
        letter_filepath = f"{letter_dir}/{self._generate_letter_filename(company)}"
        populated_template = self._populate_template(company)
        # generate file
        # pdfkit_options = {
        #     "page-size": "Letter",
        #     "enable-local-file-access": None
        # }
        # pdfkit.from_string(populated_template, letter_filepath, options=pdfkit_options)
        HTML(string=populated_template).write_pdf(letter_filepath, full_fonts=True)

    def _generate_letter_filename(self, company):
        snake_applicant_name = clg_helpers.to_snake_case(self.applicant_name)
        snake_company_name = clg_helpers.to_snake_case(company["name"])
        snake_job_title = clg_helpers.to_snake_case(company["job_title"])
        filename = f"{snake_applicant_name}_{snake_company_name}_{snake_job_title}_cover_letter.pdf"
        return filename

    def _generate_resume_filename(self, company):
        snake_applicant_name = clg_helpers.to_snake_case(self.applicant_name)
        snake_company_name = clg_helpers.to_snake_case(company["name"])
        snake_job_title = clg_helpers.to_snake_case(company["job_title"])
        filename = f"{snake_applicant_name}_{snake_company_name}_{snake_job_title}_resume.pdf"
        return filename

    def output_merged_pdf(self, company, cover_letter_file):
        # merger = pytest.PdfWriter()
        # files = [self.resume_file, cover_letter_file]

        # for file in files:
        #     merger.append(file)
        # generate filename
        # merger.write(output_filename)
        pass

    def _populate_template(self, company):
        populated_template = self.template
        requirements = ""
        for requirement in company["requirements"]:
            requirements += f"<li>{requirement}</li>"
        qualifications = ""
        for qualification in company["qualifications"]:
            qualifications += f"<li>{qualification}</li>"
        replacement_macros = {
            "{APPLICANT_NAME}": self.applicant_name,
            "{COMPANY_NAME}": company["name"],
            "{COMPANY_LOCATION}": company["location"],
            "{JOB_TITLE}": company["job_title"],
            "{REQUIREMENTS}": requirements,
            "{QUALIFICATIONS}": qualifications
        }
        for macro, value in replacement_macros.items():
            populated_template = populated_template.replace(macro, value)
        return populated_template

def main():
    args = clg_helpers.collect_args(sys.argv[1::])
    generator = CoverLetterGenerator(args.template_file, args.resume_file, args.companies_file, args.output_dir, args.applicant_name)

if __name__ == "__main__":
    main()