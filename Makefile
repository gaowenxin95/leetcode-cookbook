jupyter:

	jupyter nbconvert --to markdown --output-dir . --NbConvertApp.output_files_dir=libs \
		analysis/numpy_irr.ipynb

	jupyter nbconvert --to markdown --output-dir . --NbConvertApp.output_files_dir=libs \
	project/which_debts_are_worth_the_bank_s_effort/notebook.ipynb

	Rscript code/build-jupyter-notebook.R

cookbook:

	Rscript code/build.R

model:

	Rscript code/build-model-notes.R

readme:

	Rscript code/build-readme.R

push:

	Rscript code/push.R

copy:

	Rscript code/copy-md.R

clean:

	Rscript code/clean.R

all: jupyter cookbook clean push
