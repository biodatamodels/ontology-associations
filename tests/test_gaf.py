from ontology_association.datamodel.gaf import GafAssociation, GafAssociationDocument

DATE='1999-01-01'
def test_gaf():
    gafdoc = GafAssociationDocument(
        date_generated=DATE,
        url='http://example.org'
    )
    assoc = GafAssociation(
        db='UniProtKB',
        local_id='P1234',
        db_object_symbol='abc',
        ontology_class_ref='GO:0001234',
        aspect='F',
        db_object_taxon='NCBITaxon:9606',
        evidence_type='IEA',
        references=['PMID:123456'],
        assigned_by='MGI',
        annotation_date=DATE
    )
    gafdoc.associations=[assoc]
    print(f'Assoc: {gafdoc}')

    
    
