from ontology_association.datamodel.gpi import GpiEntity

def test_gpi():
    e = GpiEntity(
        db_object_ref='UniProtKB:P1234',
        db_object_symbol='abc',
        db_object_taxon='NCBITaxon:9606'
    )
    
