

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

CREATE TABLE complex_disease_association (
	disease_id TEXT, 
	disease_name TEXT, 
	relation VARCHAR(27) NOT NULL, 
	term_id TEXT, 
	term_label TEXT, 
	qualifier TEXT, 
	frequency TEXT, 
	sex TEXT, 
	time_course TEXT, 
	modifier TEXT, 
	evidence TEXT, 
	citation TEXT, 
	biocuration TEXT, 
	PRIMARY KEY (disease_id, disease_name, relation, term_id, term_label, qualifier, frequency, sex, time_course, modifier, evidence, citation, biocuration)
);

CREATE TABLE complex_disease_association_document (
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

CREATE TABLE complex_disease_disease_risk_association (
	disease_id TEXT, 
	disease_name TEXT, 
	term_id TEXT, 
	term_label TEXT, 
	qualifier TEXT, 
	frequency TEXT, 
	sex TEXT, 
	time_course TEXT, 
	modifier TEXT, 
	evidence TEXT, 
	citation TEXT, 
	biocuration TEXT, 
	relation VARCHAR(27) NOT NULL, 
	PRIMARY KEY (disease_id, disease_name, term_id, term_label, qualifier, frequency, sex, time_course, modifier, evidence, citation, biocuration, relation)
);

CREATE TABLE complex_disease_exposure_risk_association (
	disease_id TEXT, 
	disease_name TEXT, 
	term_id TEXT, 
	term_label TEXT, 
	qualifier TEXT, 
	frequency TEXT, 
	sex TEXT, 
	time_course TEXT, 
	modifier TEXT, 
	evidence TEXT, 
	citation TEXT, 
	biocuration TEXT, 
	relation VARCHAR(27) NOT NULL, 
	PRIMARY KEY (disease_id, disease_name, term_id, term_label, qualifier, frequency, sex, time_course, modifier, evidence, citation, biocuration, relation)
);

CREATE TABLE complex_disease_phenotype_association (
	disease_id TEXT, 
	disease_name TEXT, 
	term_id TEXT, 
	term_label TEXT, 
	qualifier TEXT, 
	frequency TEXT, 
	sex TEXT, 
	time_course TEXT, 
	modifier TEXT, 
	evidence TEXT, 
	citation TEXT, 
	biocuration TEXT, 
	relation VARCHAR(27) NOT NULL, 
	PRIMARY KEY (disease_id, disease_name, term_id, term_label, qualifier, frequency, sex, time_course, modifier, evidence, citation, biocuration, relation)
);

CREATE TABLE complex_disease_phenotype_risk_association (
	disease_id TEXT, 
	disease_name TEXT, 
	term_id TEXT, 
	term_label TEXT, 
	qualifier TEXT, 
	frequency TEXT, 
	sex TEXT, 
	time_course TEXT, 
	modifier TEXT, 
	evidence TEXT, 
	citation TEXT, 
	biocuration TEXT, 
	relation VARCHAR(27) NOT NULL, 
	PRIMARY KEY (disease_id, disease_name, term_id, term_label, qualifier, frequency, sex, time_course, modifier, evidence, citation, biocuration, relation)
);

CREATE TABLE property_value_pair (
	property TEXT, 
	value TEXT, 
	PRIMARY KEY (property, value)
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
