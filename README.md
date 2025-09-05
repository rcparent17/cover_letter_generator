# COVER LETTER GENERATOR
###### DEVELOPED BY REILLY PARENT
I am currently in the job search. The most time consuming part is manually filling out cover letters for every application, appending them to my resume, and exporting a PDF for each application. So I decided, being that I brand myself as a DevOps Engineer specializing in automation, I would automate this process as much as possible. Below is how v1.0.0 of this project works.
## Dependencies
This project is being developed on Ubuntu. So this section will only cover initial set up for Ubuntu. This project uses GNU make for running the script and [Poetry](https://python-poetry.org/) for dependency management and virtual environment management. You can install these on Ubuntu with this command:
```bash
sudo apt install python3-poetry make
```
A Makefile is provided as a wrapper for this tool. Simply running `make` will install all of the poetry dependencies and run the script. That file is where you define the input files described in the "Inputs" section. Below is the list of dependencies currently in the Poetry environment:
* `weasyprint` - for exporting HTML data as a pdf file
* `pypdf` - for combining the generated cover letter and the base resume file and exporting a new PDF
* `pytest` - for unit testing
* `pyyaml` - for reading and processing yaml files
* `black` - for automatic Python code formatting
## Project Structure
The project is currently structured as follows:
* Base repo directory - where poetry config, the README, the Makefile, and git related files live
* `src` - where all the source code files live
* `deps` - where all of the dependency input files for the script live
* `docs` - where my development documentation (not much) lives. This will probably be deleted in a future patch.
* `test` - where all of the pytest unit test files live
* `out` - where all of the generated resume (`out/resumes/`) + cover letter (`out/cover_letters/`) PDF files live
## Inputs
All of the inputs are defined in the Makefile and can be modified there.
1. Companies YAML file - A YAML file containing the applicant's name (currently only used for output file naming, YOUR NAME should just be in the template file as normal text) and entries for each company that you want to generate a resume/cover letter for. The structure must be as follows and none of the fields can be empty strings or undefined:
```yaml
applicant_name: ""
companies:
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
  - name: ... # entry 2 and so on, each company entry starting with a `-` and with the EXACT STRUCTURE of this example entry above
```
2. Template HTML file - An HTML template version of the cover letter to be generated (can download Google doc as HTML directly). The script replaces macros with data for each company entry in the companies YAML file. The current supported macros are:
    1. `{COMPANY_NAME}` - The name of the company
    2. `{COMPANY_LOCATION}` - The location of the company's headquarters
    3. `{JOB_TITLE}` - The title on the job posting, written in a human readable way (with any dashes removed and words rearranged if needed)
    4. `{REQUIREMENTS}` and `{QUALIFICATIONS}` - These macros get replaced by the script with an ordered list of the requirements and corresponding qualifications provided in the companies YAML file
3. Base resume PDF - Your resume without a cover letter included, to have the cover letter appended to.
4. Output directory - The desired output directory for the generated PDF files (default `out`). Resumes will be placed in the `resumes` subdirectory, and cover letters will be placed in the `cover_letters` subdirectory.
## Process Flow
Below is a pseudocode representation of the process flow of the script (mostly for myself, but someone may be intrigued):
```
1. Read template file into string
2. Read companies YAML file (pyyaml)
3. For each company:
	a. Read template HTML file (has CSS included)
	b. Replace template macros to generate cover letter text
	d. Convert HTML to cover letter PDF in out/cover_letters directory (weasyprint)
	e. Combine base resume PDF and cover letter PDF into final output PDF in out/resumes directory (pypdf)
```
