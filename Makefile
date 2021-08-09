OUT_DIR=out
RESUME_DIR=resume
WEBSITE_DIR=website
PYTHON=python3

.PHONY: all clean

all: $(OUT_DIR)/index.html $(OUT_DIR)/resume.pdf

$(OUT_DIR)/index.html: main.py config.yml $(WEBSITE_DIR)/index.jinja2 $(WEBSITE_DIR)/style.css
	$(PYTHON) $< --output-dir "$(OUT_DIR)"

$(OUT_DIR)/resume.pdf: $(OUT_DIR)/index.html $(RESUME_DIR)/resume.jinja2 $(RESUME_DIR)/style.css
	pandoc --self-contained --css "$(RESUME_DIR)"/style.css --output "$(OUT_DIR)"/resume.html "$(OUT_DIR)"/resume.md
	wkhtmltopdf --page-size letter "$(OUT_DIR)"/resume.html "$(OUT_DIR)"/resume.pdf

clean:
	rm -f $(OUT_DIR)/*