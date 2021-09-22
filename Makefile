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
SOURCE_FILES := $(shell find $(SCHEMA_DIR) -name '*.yaml')
SCHEMA_NAMES = $(patsubst $(SCHEMA_DIR)/%.yaml, %, $(SOURCE_FILES))

SCHEMA_NAME = all
SCHEMA_SRC = $(SCHEMA_DIR)/$(SCHEMA_NAME).yaml
TGTS = graphql jsonschema docs shex owl csv graphql python jsonld-context golr

#GEN_OPTS = --no-mergeimports
GEN_OPTS = 

all: gen stage

gen-project:
	gen-project -d ontology_associations $(SCHEMA_SRC)

# test docs locally.
docserve:
	mkdocs serve

gh-deploy:
	mkdocs gh-deploy

# headers
csv/gaf.header.tsv: src/schema/gaf.yaml
	./util/gen-header.py -c 'gaf association' $< > $@

csv/gpad.header.tsv: src/schema/gpad.yaml
	./util/gen-header.py -c 'gpad association' $< > $@

csv/gpi.header.tsv: src/schema/gpi.yaml
	./util/gen-header.py -c 'gpi entity' $< > $@


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
