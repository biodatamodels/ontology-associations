

CREATE TABLE association_document (
	date_generated TEXT, 
	generated_by TEXT, 
	url TEXT, 
	project_release TEXT, 
	funding TEXT, 
	go_version TEXT, 
	ro_version TEXT, 
	gorel_version TEXT, 
	associations TEXT, 
	PRIMARY KEY (date_generated, generated_by, url, project_release, funding, go_version, ro_version, gorel_version, associations)
);

CREATE TABLE gaf_association (
	db TEXT NOT NULL, 
	local_id TEXT NOT NULL, 
	db_object_symbol TEXT NOT NULL, 
	qualifiers VARCHAR(42), 
	ontology_class_ref TEXT NOT NULL, 
	supporting_references TEXT NOT NULL, 
	evidence_type TEXT NOT NULL, 
	with_or_from TEXT, 
	aspect VARCHAR(1) NOT NULL, 
	db_object_name TEXT, 
	db_object_synonyms TEXT, 
	db_object_type VARCHAR(26), 
	db_object_taxon TEXT NOT NULL, 
	annotation_date DATETIME, 
	assigned_by TEXT NOT NULL, 
	annotation_extensions TEXT, 
	gene_product_form TEXT, 
	PRIMARY KEY (db, local_id, db_object_symbol, qualifiers, ontology_class_ref, supporting_references, evidence_type, with_or_from, aspect, db_object_name, db_object_synonyms, db_object_type, db_object_taxon, annotation_date, assigned_by, annotation_extensions, gene_product_form)
);

CREATE TABLE gaf_association_document (
	date_generated TEXT, 
	generated_by TEXT, 
	url TEXT, 
	project_release TEXT, 
	funding TEXT, 
	go_version TEXT, 
	ro_version TEXT, 
	gorel_version TEXT, 
	associations TEXT, 
	PRIMARY KEY (date_generated, generated_by, url, project_release, funding, go_version, ro_version, gorel_version, associations)
);

CREATE TABLE gpad_association (
	db_object_ref TEXT NOT NULL, 
	negation BOOLEAN, 
	relation VARCHAR(42) NOT NULL, 
	ontology_class_ref TEXT NOT NULL, 
	supporting_references TEXT NOT NULL, 
	evidence_type TEXT NOT NULL, 
	with_or_from TEXT, 
	interacting_taxon_ref TEXT, 
	annotation_date DATETIME, 
	assigned_by TEXT NOT NULL, 
	annotation_extensions TEXT, 
	annotation_properties TEXT, 
	db_object_type VARCHAR(26), 
	PRIMARY KEY (db_object_ref, negation, relation, ontology_class_ref, supporting_references, evidence_type, with_or_from, interacting_taxon_ref, annotation_date, assigned_by, annotation_extensions, annotation_properties, db_object_type)
);

CREATE TABLE gpad_association_document (
	date_generated TEXT, 
	generated_by TEXT, 
	url TEXT, 
	project_release TEXT, 
	funding TEXT, 
	go_version TEXT, 
	ro_version TEXT, 
	gorel_version TEXT, 
	associations TEXT, 
	PRIMARY KEY (date_generated, generated_by, url, project_release, funding, go_version, ro_version, gorel_version, associations)
);

CREATE TABLE property_value_pair (
	property TEXT, 
	value TEXT, 
	PRIMARY KEY (property, value)
);

CREATE TABLE simple_gaf_association (
	db TEXT NOT NULL, 
	local_id TEXT NOT NULL, 
	db_object_symbol TEXT NOT NULL, 
	ontology_class_ref TEXT NOT NULL, 
	supporting_references TEXT NOT NULL, 
	evidence_type TEXT NOT NULL, 
	with_or_from TEXT, 
	aspect VARCHAR(1) NOT NULL, 
	db_object_name TEXT, 
	db_object_synonyms TEXT, 
	db_object_type VARCHAR(26), 
	db_object_taxon TEXT NOT NULL, 
	annotation_date DATETIME, 
	assigned_by TEXT NOT NULL, 
	annotation_extensions TEXT, 
	gene_product_form TEXT, 
	qualifiers VARCHAR(14), 
	PRIMARY KEY (db, local_id, db_object_symbol, ontology_class_ref, supporting_references, evidence_type, with_or_from, aspect, db_object_name, db_object_synonyms, db_object_type, db_object_taxon, annotation_date, assigned_by, annotation_extensions, gene_product_form, qualifiers)
);

CREATE TABLE xaf_association (
	db TEXT NOT NULL, 
	local_id TEXT NOT NULL, 
	db_object_symbol TEXT NOT NULL, 
	qualifiers TEXT, 
	ontology_class_ref TEXT NOT NULL, 
	supporting_references TEXT NOT NULL, 
	evidence_type TEXT NOT NULL, 
	with_or_from TEXT, 
	aspect TEXT NOT NULL, 
	db_object_name TEXT, 
	db_object_synonyms TEXT, 
	db_object_type TEXT, 
	db_object_taxon TEXT NOT NULL, 
	annotation_date DATETIME, 
	assigned_by TEXT NOT NULL, 
	annotation_extensions TEXT, 
	gene_product_form TEXT, 
	PRIMARY KEY (db, local_id, db_object_symbol, qualifiers, ontology_class_ref, supporting_references, evidence_type, with_or_from, aspect, db_object_name, db_object_synonyms, db_object_type, db_object_taxon, annotation_date, assigned_by, annotation_extensions, gene_product_form)
);
