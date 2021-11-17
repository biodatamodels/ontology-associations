

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
	"Creation_date" TEXT, 
	"Update_date" TEXT, 
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
	"Creation_date" TEXT, 
	"Update_date" TEXT, 
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
	annotation_date TEXT, 
	assigned_by TEXT NOT NULL, 
	annotation_extensions TEXT, 
	gene_product_form TEXT, 
	PRIMARY KEY (db, local_id, db_object_symbol, qualifiers, ontology_class_ref, supporting_references, evidence_type, with_or_from, aspect, db_object_name, db_object_synonyms, db_object_type, db_object_taxon, annotation_date, assigned_by, annotation_extensions, gene_product_form)
);