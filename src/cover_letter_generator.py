import sys, os

import pypdf

from weasyprint import HTML

import clg_helpers


# Class that encapsulates all functionality for generating cover letters and combined resumes, based on YAML input
class CoverLetterGenerator:
    def __init__(
        self, template_file, resume_file, companies_file, output_dir
    ):
        if not (
            os.path.exists(template_file)
            or os.path.exists(resume_file)
            or os.path.exists(companies_file)
        ):
            raise FileExistsError("One or more provided files does not exist.")

        # read template as oneline HTML string
        self.template = ""
        with open(template_file, "r") as template:
            self.template = "".join([x.strip() for x in template.readlines()])

        self.companies = clg_helpers.read_companies(companies_file)
        self.resume_file = resume_file
        self.output_dir = output_dir
        self.applicant_name = clg_helpers.get_applicant_name(companies_file)

    # Generates a cover letter PDF file for a company entry and the generator's populated template
    def generate_letter(self, company):
        letter_dir = f"{self.output_dir}/cover_letters"
        # create dir if it doesn't exist
        os.makedirs(letter_dir, exist_ok=True)
        letter_filepath = f"{letter_dir}/{self._generate_letter_filename(company)}"
        populated_template = self._populate_template(company)
        HTML(string=populated_template).write_pdf(letter_filepath, full_fonts=True)
        print(f"Cover letter generated: {letter_filepath}")

    # Generates the desired cover letter file name (all in snake case) for a company entry
    def _generate_letter_filename(self, company):
        snake_applicant_name = clg_helpers.to_snake_case(self.applicant_name)
        snake_company_name = clg_helpers.to_snake_case(company["name"])
        snake_job_title = clg_helpers.to_snake_case(company["job_title"])
        filename = f"{snake_applicant_name}_{snake_company_name}_{snake_job_title}_cover_letter.pdf"
        return filename

    # Generates the desired resume file name (all in snake case) for a company entry
    def _generate_resume_filename(self, company):
        snake_applicant_name = clg_helpers.to_snake_case(self.applicant_name)
        snake_company_name = clg_helpers.to_snake_case(company["name"])
        snake_job_title = clg_helpers.to_snake_case(company["job_title"])
        filename = f"{snake_applicant_name}_{snake_company_name}_{snake_job_title}_resume.pdf"
        return filename

    # Combines the base resume PDF file and the already generated cover letter PDF file into a new output PDF file
    def output_merged_pdf(self, company):
        resume_filename = self._generate_resume_filename(company)
        letter_filename = self._generate_letter_filename(company)
        letter_dir = f"{self.output_dir}/cover_letters"
        resume_dir = f"{self.output_dir}/resumes"
        # create dir if it doesn't exist
        os.makedirs(resume_dir, exist_ok=True)
        letter_filepath = f"{letter_dir}/{letter_filename}"
        resume_filepath = f"{resume_dir}/{resume_filename}"

        writer = pypdf.PdfWriter()
        # add base resume and generated cover letter to writer
        writer.append(self.resume_file)
        writer.append(letter_filepath)

        writer.write(resume_filepath)
        print(f"Combined resume generated: {resume_filepath}")

    # Replaces all macros in the generator's template with their values from the company entry. Returns new string
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
            "{QUALIFICATIONS}": qualifications,
        }
        for macro, value in replacement_macros.items():
            populated_template = populated_template.replace(macro, value)
        return populated_template


# Main function. Invoked by make
def main():
    args = clg_helpers.collect_args(sys.argv[1::])
    generator = CoverLetterGenerator(
        args.template_file,
        args.resume_file,
        args.companies_file,
        args.output_dir,
    )
    for company in generator.companies:
        generator.generate_letter(company)
        generator.output_merged_pdf(company)


if __name__ == "__main__":
    main()
