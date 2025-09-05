# COVER LETTER GENERATOR
###### DEVELOPED BY REILLY PARENT
I am currently in the job search. The most time consuming part is manually filling out cover letters for every application, appending them to my resume, and exporting a PDF for each application. So I decided, being that I brand myself as a DevOps Engineer specializing in automation, I would automate this process as much as possible. Below is how I would like this project to end up working.
## Dependencies
This project is being developed on Ubuntu. So this section will only cover initial set up for Ubuntu. This project uses GNU make for running the script and [Poetry](https://python-poetry.org/) for dependency management and virtual environment management. You can install these on Ubuntu with this command:
```bash
sudo apt install python3-poetry make
```
And to use the Makefile, simply run the command:
```bash
make
```
Once poetry is installed, you can install all of the project dependencies with the command `poetry install` in the base directory of this repo. A Makefile is provided as a wrapper for the poetry command to run the script. That file is where you would define the input files described in the "Input Files" section. Below is the list of dependencies currently in the Poetry environment:
* `pdfkit` - for exporting HTML data as a pdf file
* `pypdf` - for appending the generated cover letter to the provided resume file (for an ATS word count boost)
* `pytest` - for unit testing
* `pyyaml` - for reading and processing yaml files
## Project Structure
The project is currently structured as follows:
* Base repo directory - where poetry config, the README, the Makefile, and git related files live
* `src` - where all the source code files live
* `deps` - where all of the dependency input files for the script live
* `test` - where all of the pytest unit test files live
* `out` - where all of the generated resume (`out/resumes/`) + cover letter (`out/cover_letters/`) PDF files live
## Input Files
The paths to all of the input files are defined in the Makefile and can be modified there.
1. Companies YAML file - A YAML file containing entries for each company that you want to generate a resume/cover letter for. The structure must be as follows:
```yaml
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
2. Template HTML file - An HTML template version of the cover letter to be generated (can download Google doc as HTML directly). The script replaces macros with data for each company entry in the companies YAML file. The current planned macros are:
    1. `{COMPANY_NAME}` - The name of the company
    2. `{COMPANY_LOCATION}` - The location of the company's headquarters
    3. `{JOB_TITLE}` - The title on the job posting, written in a human readable way (with any dashes removed and words rearranged if needed)
    4. `{REQUIREMENTS}` and `{QUALIFICATIONS}` - These macros get replaced by the script with an ordered list of the requirements and corresponding qualifications provided in the companies YAML file
3. Base resume PDF - Your resume without a cover letter included, to have the cover letter appended to. You can modify the CSS being passed to `pdfkit` to change the font and layout. The default CSS will match my resume.
## Process Flow
Below is a pseudocode representation of the process flow of the script (mostly for myself, but someone may be intrigued):
```
1. Read template file into string
2. Read companies YAML file (`pyyaml`)
3. For each company:
	a. Read template HTML file (has CSS included)
	b. Replace template macros to generate cover letter text
	c. Convert plaintext cover letter contents to equivalent HTML elements and append it to temp HTML file
	d. Convert HTML to cover letter PDF in `out/cover_letters` directory (`pdfkit`)
	e. Combine base resume PDF and cover letter PDF into final output PDF in `out/resumes` directory (`pypdf`)
```
