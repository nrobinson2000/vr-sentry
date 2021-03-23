files := $(addprefix out/, $(addsuffix .pdf, $(basename $(wildcard *.Rmd) )))

all: $(files)

out/%.pdf: %.Rmd
	@Rscript -e "rmarkdown::render('$(addsuffix .Rmd, $(basename $(notdir $@)))', output_file='$@')"

clean:
	rm out/*.pdf
