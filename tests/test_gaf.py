from ontology_association.datamodel.gaf import GafAssociation

def test_gaf():
    assoc = GafAssociation(
        db='UniProtKB',
        local_id='P1234',
        db_object_symbol='abc',
        ontology_class_ref='GO:0001234',
        db_object_taxon='NCBITaxon:9606',
        evidence_type='IEA',
        references=['PMID:123456'],
        assigned_by='MGI',
        annotation_date='1999-01-01'
    )
    
