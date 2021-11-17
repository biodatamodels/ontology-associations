

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

CREATE TABLE gpi_document (
	entities TEXT, 
	PRIMARY KEY (entities)
);

CREATE TABLE gpi_entity (
	db_object_ref TEXT NOT NULL, 
	db_object_symbol TEXT NOT NULL, 
	db_object_name TEXT, 
	db_object_type TEXT, 
	db_object_taxon TEXT NOT NULL, 
	PRIMARY KEY (db_object_ref)
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
	annotation_date TEXT, 
	assigned_by TEXT NOT NULL, 
	annotation_extensions TEXT, 
	gene_product_form TEXT, 
	PRIMARY KEY (db, local_id, db_object_symbol, qualifiers, ontology_class_ref, supporting_references, evidence_type, with_or_from, aspect, db_object_name, db_object_synonyms, db_object_type, db_object_taxon, annotation_date, assigned_by, annotation_extensions, gene_product_form)
);

CREATE TABLE property_value_pair (
	property TEXT, 
	value TEXT, 
	gpi_entity_db_object_ref TEXT, 
	PRIMARY KEY (property, value, gpi_entity_db_object_ref), 
	FOREIGN KEY(gpi_entity_db_object_ref) REFERENCES gpi_entity (db_object_ref)
);

CREATE TABLE gpi_entity_db_object_synonyms (
	backref_id TEXT, 
	db_object_synonyms TEXT, 
	PRIMARY KEY (backref_id, db_object_synonyms), 
	FOREIGN KEY(backref_id) REFERENCES gpi_entity (db_object_ref)
);

CREATE TABLE gpi_entity_encoded_by (
	backref_id TEXT, 
	encoded_by TEXT, 
	PRIMARY KEY (backref_id, encoded_by), 
	FOREIGN KEY(backref_id) REFERENCES gpi_entity (db_object_ref)
);

CREATE TABLE gpi_entity_parent_protein (
	backref_id TEXT, 
	parent_protein TEXT, 
	PRIMARY KEY (backref_id, parent_protein), 
	FOREIGN KEY(backref_id) REFERENCES gpi_entity (db_object_ref)
);

CREATE TABLE gpi_entity_protein_containing_complex_members (
	backref_id TEXT, 
	protein_containing_complex_members TEXT, 
	PRIMARY KEY (backref_id, protein_containing_complex_members), 
	FOREIGN KEY(backref_id) REFERENCES gpi_entity (db_object_ref)
);

CREATE TABLE gpi_entity_db_xrefs (
	backref_id TEXT, 
	db_xrefs TEXT, 
	PRIMARY KEY (backref_id, db_xrefs), 
	FOREIGN KEY(backref_id) REFERENCES gpi_entity (db_object_ref)
);
