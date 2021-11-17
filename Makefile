###Configuration
#
# These are standard options to make Make sane:
# <http://clarkgrubb.com/makefile-style-guide#toc2>

MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := all
.DELETE_ON_ERROR:
.SUFFIXES:
.SECONDARY:

SRC_DIR = src
SCHEMA_DIR = $(SRC_DIR)/schema
SCHEMAS = all complexpheno signor pombase hpoa gpad gaf gpi

all: all-schemas all-docs markdown

all-schemas: $(patsubst %, gen-%, $(SCHEMAS))
all-docs: $(patsubst %, md-%, $(SCHEMAS)) markdown

gen-%: $(SCHEMA_DIR)/%.yaml
	gen-project $< -d .
md-%: $(SCHEMA_DIR)/%.yaml
	gen-markdown -d docs  $< && mv docs/index.md  docs/$*.md

markdown:
	cp src/docs/*md docs/
	cp docs/all.md docs/index.md

copy-python:
	cp python/*py ontology_association/datamodel/

deploy-docs:
	wc docs/index.md && mkdocs gh-deploy

test.db:
	cat sql/gaf.ddl.sql | sqlite3 test.db

tests/data/%.gaf.pandas.tsv: tests/data/%.gaf.tsv
	./util/gaf2pandas $< > $@

tests/data/%.gaf.jsonld: tests/data/%.gaf.pandas.tsv
	./util/tsv2jsonld.py -C jsonld-context/all.context.json $< > $@

tests/data/%.ttl: tests/data/%.jsonld
	riot $< > $@

TESTGAF=tests/data/example_mgi.gaf.pandas.tsv
load-test:
	(echo ".mode tab"; echo ".import $(TESTGAF) gafassociation") | sqlite3 test.db

load-%: tests/data/%.gaf.pandas.tsv
	(echo ".mode tab"; echo ".import $< gafassociation") | sqlite3 test.db

rules/%.report.txt: rules/%.sql
	cat $< | sqlite3 test.db > $@
