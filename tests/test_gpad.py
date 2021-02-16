from ontology_association.datamodel.gpad import GpadAssociation

def test_gpad():
    assoc = GpadAssociation(
        db_object_ref='UniProtKB:P1234',
        ontology_class_ref='GO:0001234',
        evidence_type='IEA',
        supporting_references=['PMID:123456'],
        assigned_by='MGI',
        annotation_date='1999-01-01'
    )
    
