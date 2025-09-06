DEPENDENCIES_PATH = deps
OUT_PATH = out

RESUME_FILE = ${DEPENDENCIES_PATH}/reilly_parent_devops_resume.pdf
COMPANIES_FILE = ${DEPENDENCIES_PATH}/companies.yaml
TEMPLATE_FILE = ${DEPENDENCIES_PATH}/template.html

run: install
	poetry run python src/cover_letter_generator.py \
		--resume-file "${RESUME_FILE}" \
		--companies-file "${COMPANIES_FILE}" \
		--template-file "${TEMPLATE_FILE}" \
		--output-dir "${OUT_PATH}" 

install:
	poetry install

clean:
	rm -rf "${OUT_PATH}"

clean_run: clean run

test: install
	poetry run pytest -l -v test/*