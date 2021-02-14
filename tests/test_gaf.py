from ontology_association.datamodel.gaf import GafAssociation

def test_gaf():
    assoc = GafAssociation(
        db='UniProtKB',
        local_id='P1234'
    )
    
