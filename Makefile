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
TGTS = graphql jsonschema docs shex owl csv graphql python jsonld-context

#GEN_OPTS = --no-mergeimports
GEN_OPTS = 

all: gen stage
gen: $(patsubst %,gen-%,$(TGTS))
clean:
	rm -rf target/
	rm -rf docs/

t:
	echo $(SCHEMA_NAMES)

echo:
	echo $(patsubst %,gen-%,$(TGTS))

test: all pytest

pytest:
	pytest

install:
	. environment.sh
	pip install -r requirements.txt

tdir-%:
	mkdir -p target/$*
docs:
	mkdir $@

stage: $(patsubst %,stage-%,$(TGTS))
stage-%: gen-%
	cp -pr target/$* .

src-modified: $(SOURCE_FILES)
.PHONY: src-modified

###  -- MARKDOWN DOCS --
# Generate documentation ready for mkdocs
# TODO: modularize imports
# TODO: ensure triggered
gen-docs: target/docs/index.md copy-src-docs
.PHONY: gen-docs
copy-src-docs:
	cp $(SRC_DIR)/docs/*md target/docs/
target/docs/%.md: $(SCHEMA_SRC) tdir-docs
	gen-markdown $(GEN_OPTS) --dir target/docs $<
stage-docs: gen-docs
	cp -pr target/docs .

###  -- MARKDOWN DOCS --
# TODO: modularize imports
gen-python: $(patsubst %, target/python/%.py, $(SCHEMA_NAMES))
	cp python/*py ontology_association/datamodel/
.PHONY: gen-python
target/python/%.py: $(SCHEMA_DIR)/%.yaml  tdir-python
	gen-py-classes --no-mergeimports $(GEN_OPTS) $< > $@

###  -- MARKDOWN DOCS --
# TODO: modularize imports. For now imports are merged.
gen-graphql:target/graphql/$(SCHEMA_NAME).graphql 
target/graphql/%.graphql: $(SCHEMA_DIR)/%.yaml tdir-graphql
	gen-graphql $(GEN_OPTS) $< > $@

###  -- JSON schema --
# TODO: modularize imports. For now imports are merged.
gen-jsonschema: target/jsonschema/$(SCHEMA_NAME).schema.json
target/jsonschema/%.schema.json: $(SCHEMA_DIR)/%.yaml tdir-jsonschema
	gen-json-schema $(GEN_OPTS) -t transaction $< > $@

###  -- JSON-LD-CONTEXT --
# TODO: modularize imports. For now imports are merged.
gen-jsonld-context: target/jsonld-context/$(SCHEMA_NAME).context.json
target/jsonld-context/%.context.json: $(SCHEMA_DIR)/%.yaml tdir-jsonld-context
	gen-jsonld-context $(GEN_OPTS)  $< > $@

###  -- Shex --
# one file per module
gen-shex: $(patsubst %, target/shex/%.shex, $(SCHEMA_NAMES))
target/shex/%.shex: $(SCHEMA_DIR)/%.yaml tdir-shex
	gen-shex --no-mergeimports $(GEN_OPTS) $< > $@

###  -- Golr --
# one file per module
gen-golr: $(patsubst %, target/golr/%.golr.yaml, $(SCHEMA_NAME))
target/golr/%.golr.yaml: $(SCHEMA_DIR)/%.yaml tdir-golr
	gen-golr-views --no-mergeimports -d target/golr $(GEN_OPTS) $<

###  -- CSV --
# one file per module
gen-csv: $(patsubst %, target/csv/%.csv, $(SCHEMA_NAMES))
target/csv/%.csv: $(SCHEMA_DIR)/%.yaml tdir-csv
	gen-csv $(GEN_OPTS) $< > $@

###  -- OWL --
# TODO: modularize imports. For now imports are merged.
gen-owl: target/owl/$(SCHEMA_NAME).owl.ttl
.PHONY: gen-owl
target/owl/%.owl.ttl: $(SCHEMA_DIR)/%.yaml tdir-owl
	gen-owl $(GEN_OPTS) $< > $@

###  -- RDF (direct mapping) --
# TODO: modularize imports. For now imports are merged.
gen-rdf: target/rdf/$(SCHEMA_NAME).ttl
target/rdf/%.ttl: $(SCHEMA_DIR)/%.yaml tdir-rdf
	gen-rdf $(GEN_OPTS) $< > $@

###  -- LinkML --
# linkml (copy)
# one file per module
gen-linkml: target/linkml/$(SCHEMA_NAME).yaml
target/linkml/%.yaml: $(SCHEMA_DIR)/%.yaml tdir-limkml
	cp $< > $@

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

# ddl
sql/gaf.ddl.sql: src/schema/gaf.yaml
	./util/gen-sqlddl.py -c 'gaf association' $< > $@

sql/gpad.ddl.sql: src/schema/gpad.yaml
	./util/gen-sqlddl.py -c 'gpad association' $< > $@

sql/gpi.ddl.sql: src/schema/gpi.yaml
	./util/gen-sqlddl.py -c 'gpi entity' $< > $@

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
