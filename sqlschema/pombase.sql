

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
