

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

CREATE TABLE causaltab_interaction (
	"ID(s)_interactor_A" TEXT, 
	"ID(s)_interactor_B" TEXT, 
	"Alt._ID(s)_interactor_A" TEXT, 
	"Alt._ID(s)_interactor_B" TEXT, 
	"Alias(es)_interactor_A" TEXT, 
	"Alias(es)_interactor_B" TEXT, 
	"Interaction_detection_method(s)" VARCHAR(49), 
	"Publication_1st_author(s)" TEXT, 
	"Publication_Identifier(s)" TEXT, 
	"Taxid_interactor_A" TEXT, 
	"Taxid_interactor_B" TEXT, 
	"Interaction_type(s)" VARCHAR(42), 
	"Source_database(s)" TEXT, 
	"Interaction_identifier(s)" TEXT, 
	"Confidence_value(s)" TEXT, 
	"Expansion_method(s)" VARCHAR(33), 
	"Biological_role(s)_interactor_A" VARCHAR(34), 
	"Biological_role(s)_interactor_B" VARCHAR(34), 
	"Experimental_role(s)_interactor_A" VARCHAR(35), 
	"Experimental_role(s)_interactor_B" VARCHAR(35), 
	"Type(s)_interactor_A" TEXT, 
	"Type(s)_interactor_B" TEXT, 
	"Xref(s)_interactor_A" TEXT, 
	"Xref(s)_interactor_B" TEXT, 
	"Interaction_Xref(s)" VARCHAR(40), 
	"Annotation(s)_interactor_A" TEXT, 
	"Annotation(s)_interactor_B" TEXT, 
	"Interaction_annotation(s)" TEXT, 
	"Host_organism(s)" TEXT, 
	"Interaction_parameter(s)" TEXT, 
	"Creation_date" DATETIME, 
	"Update_date" DATETIME, 
	"Checksum(s)_interactor_A" TEXT, 
	"Checksum(s)_interactor_B" TEXT, 
	"Interaction_Checksum(s)" TEXT, 
	"Negative" VARCHAR(5), 
	"Feature(s)_interactor_A" TEXT, 
	"Feature(s)_interactor_B" TEXT, 
	"Stoichiometry(s)_interactor_A" VARCHAR(1), 
	"Stoichiometry(s)_interactor_B" VARCHAR(1), 
	"Identification_method_participant_A" TEXT, 
	"Identification_method_participant_B" TEXT, 
	"Biological_Effect_interactor_A" VARCHAR(1), 
	"Biological_Effect_interactor_B" VARCHAR(1), 
	"Causal_Regulatory_Mechanism" VARCHAR(49), 
	"Causal_statement" TEXT, 
	PRIMARY KEY ("ID(s)_interactor_A", "ID(s)_interactor_B", "Alt._ID(s)_interactor_A", "Alt._ID(s)_interactor_B", "Alias(es)_interactor_A", "Alias(es)_interactor_B", "Interaction_detection_method(s)", "Publication_1st_author(s)", "Publication_Identifier(s)", "Taxid_interactor_A", "Taxid_interactor_B", "Interaction_type(s)", "Source_database(s)", "Interaction_identifier(s)", "Confidence_value(s)", "Expansion_method(s)", "Biological_role(s)_interactor_A", "Biological_role(s)_interactor_B", "Experimental_role(s)_interactor_A", "Experimental_role(s)_interactor_B", "Type(s)_interactor_A", "Type(s)_interactor_B", "Xref(s)_interactor_A", "Xref(s)_interactor_B", "Interaction_Xref(s)", "Annotation(s)_interactor_A", "Annotation(s)_interactor_B", "Interaction_annotation(s)", "Host_organism(s)", "Interaction_parameter(s)", "Creation_date", "Update_date", "Checksum(s)_interactor_A", "Checksum(s)_interactor_B", "Interaction_Checksum(s)", "Negative", "Feature(s)_interactor_A", "Feature(s)_interactor_B", "Stoichiometry(s)_interactor_A", "Stoichiometry(s)_interactor_B", "Identification_method_participant_A", "Identification_method_participant_B", "Biological_Effect_interactor_A", "Biological_Effect_interactor_B", "Causal_Regulatory_Mechanism", "Causal_statement")
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
	gene_product_properties TEXT, 
	PRIMARY KEY (db_object_ref)
);

CREATE TABLE human_phenotype_ontology_association (
	db TEXT NOT NULL, 
	local_id TEXT NOT NULL, 
	db_object_symbol TEXT NOT NULL, 
	relation TEXT NOT NULL, 
	ontology_class_ref TEXT NOT NULL, 
	supporting_references TEXT NOT NULL, 
	evidence_type TEXT NOT NULL, 
	onset TEXT, 
	frequency TEXT, 
	with_or_from TEXT, 
	aspect TEXT NOT NULL, 
	db_object_synonyms TEXT, 
	annotation_date DATETIME, 
	assigned_by TEXT NOT NULL, 
	PRIMARY KEY (db, local_id, db_object_symbol, relation, ontology_class_ref, supporting_references, evidence_type, onset, frequency, with_or_from, aspect, db_object_synonyms, annotation_date, assigned_by)
);

CREATE TABLE human_phenotype_ontology_association_document (
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

CREATE TABLE mitab_interaction (
	"ID(s)_interactor_A" TEXT, 
	"ID(s)_interactor_B" TEXT, 
	"Alt._ID(s)_interactor_A" TEXT, 
	"Alt._ID(s)_interactor_B" TEXT, 
	"Alias(es)_interactor_A" TEXT, 
	"Alias(es)_interactor_B" TEXT, 
	"Interaction_detection_method(s)" VARCHAR(49), 
	"Publication_1st_author(s)" TEXT, 
	"Publication_Identifier(s)" TEXT, 
	"Taxid_interactor_A" TEXT, 
	"Taxid_interactor_B" TEXT, 
	"Interaction_type(s)" VARCHAR(42), 
	"Source_database(s)" TEXT, 
	"Interaction_identifier(s)" TEXT, 
	"Confidence_value(s)" TEXT, 
	"Expansion_method(s)" VARCHAR(33), 
	"Biological_role(s)_interactor_A" VARCHAR(34), 
	"Biological_role(s)_interactor_B" VARCHAR(34), 
	"Experimental_role(s)_interactor_A" VARCHAR(35), 
	"Experimental_role(s)_interactor_B" VARCHAR(35), 
	"Type(s)_interactor_A" TEXT, 
	"Type(s)_interactor_B" TEXT, 
	"Xref(s)_interactor_A" TEXT, 
	"Xref(s)_interactor_B" TEXT, 
	"Interaction_Xref(s)" VARCHAR(40), 
	"Annotation(s)_interactor_A" TEXT, 
	"Annotation(s)_interactor_B" TEXT, 
	"Interaction_annotation(s)" TEXT, 
	"Host_organism(s)" TEXT, 
	"Interaction_parameter(s)" TEXT, 
	"Creation_date" DATETIME, 
	"Update_date" DATETIME, 
	"Checksum(s)_interactor_A" TEXT, 
	"Checksum(s)_interactor_B" TEXT, 
	"Interaction_Checksum(s)" TEXT, 
	"Negative" VARCHAR(5), 
	"Feature(s)_interactor_A" TEXT, 
	"Feature(s)_interactor_B" TEXT, 
	"Stoichiometry(s)_interactor_A" VARCHAR(1), 
	"Stoichiometry(s)_interactor_B" VARCHAR(1), 
	"Identification_method_participant_A" TEXT, 
	"Identification_method_participant_B" TEXT, 
	PRIMARY KEY ("ID(s)_interactor_A", "ID(s)_interactor_B", "Alt._ID(s)_interactor_A", "Alt._ID(s)_interactor_B", "Alias(es)_interactor_A", "Alias(es)_interactor_B", "Interaction_detection_method(s)", "Publication_1st_author(s)", "Publication_Identifier(s)", "Taxid_interactor_A", "Taxid_interactor_B", "Interaction_type(s)", "Source_database(s)", "Interaction_identifier(s)", "Confidence_value(s)", "Expansion_method(s)", "Biological_role(s)_interactor_A", "Biological_role(s)_interactor_B", "Experimental_role(s)_interactor_A", "Experimental_role(s)_interactor_B", "Type(s)_interactor_A", "Type(s)_interactor_B", "Xref(s)_interactor_A", "Xref(s)_interactor_B", "Interaction_Xref(s)", "Annotation(s)_interactor_A", "Annotation(s)_interactor_B", "Interaction_annotation(s)", "Host_organism(s)", "Interaction_parameter(s)", "Creation_date", "Update_date", "Checksum(s)_interactor_A", "Checksum(s)_interactor_B", "Interaction_Checksum(s)", "Negative", "Feature(s)_interactor_A", "Feature(s)_interactor_B", "Stoichiometry(s)_interactor_A", "Stoichiometry(s)_interactor_B", "Identification_method_participant_A", "Identification_method_participant_B")
);

CREATE TABLE pombase_phaf_association (
	"Database_name" VARCHAR(7) NOT NULL, 
	"Gene_systematic_ID" TEXT NOT NULL, 
	"FYPO_ID" TEXT NOT NULL, 
	"Allele_description" TEXT, 
	"Expression" VARCHAR(23), 
	"Parental_strain" TEXT, 
	"Strain_name_(background)" TEXT, 
	"Genotype_description" TEXT, 
	"Gene_name" TEXT, 
	"Allele_name" TEXT, 
	"Allele_synonym" TEXT, 
	"Allele_type" VARCHAR(33), 
	"Evidence" VARCHAR(73) NOT NULL, 
	"Condition" TEXT, 
	"Penetrance" TEXT, 
	"Severity" TEXT, 
	"Extension" TEXT, 
	"Reference" TEXT NOT NULL, 
	"Taxon" INTEGER NOT NULL, 
	"Date" TEXT, 
	PRIMARY KEY ("Database_name", "Gene_systematic_ID", "FYPO_ID", "Allele_description", "Expression", "Parental_strain", "Strain_name_(background)", "Genotype_description", "Gene_name", "Allele_name", "Allele_synonym", "Allele_type", "Evidence", "Condition", "Penetrance", "Severity", "Extension", "Reference", "Taxon", "Date")
);

CREATE TABLE pombase_phaf_association_document (
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
