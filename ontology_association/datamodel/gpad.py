# Auto generated from gpad.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-02-14 15:29
# Schema: gpad
#
# id: https://w3id.org/ontology_association/gpad
# description: GPAD datamodel https://github.com/geneontology/go-annotation/blob/master/specs/gpad-gpi-2-0.md
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from biolinkml.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from biolinkml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from biolinkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from biolinkml.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from . association import AbstractThingId, Association, AssociationDocument, ConjunctionExtensionExpression, OntologyClassId, PropertyValuePair, ProviderId, PublicationId, RelationTermId, TaxonId
from biolinkml.utils.metamodelcore import Bool, XSDDateTime
from includes.types import Boolean, Datetime, String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
GO = CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
ONTOLOGY_ASSOCIATION = CurieNamespace('ontology_association', 'https://w3id.org/ontology_association/')
DEFAULT_ = ONTOLOGY_ASSOCIATION


# Types

# Class references



@dataclass
class GpadAssociation(Association):
    """
    line of GPAD
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.GpadAssociation
    class_class_curie: ClassVar[str] = "ontology_association:GpadAssociation"
    class_name: ClassVar[str] = "gpad association"
    class_model_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.GpadAssociation

    db_object_ref: Union[str, AbstractThingId] = None
    ontology_class_ref: Union[str, AbstractThingId] = None
    supporting_references: Union[Union[str, PublicationId], List[Union[str, PublicationId]]] = None
    evidence_type: Union[str, OntologyClassId] = None
    assigned_by: Union[str, ProviderId] = None
    negation: Optional[Union[bool, Bool]] = None
    relation: Optional[Union[str, RelationTermId]] = None
    with_or_from: Optional[Union[Union[str, AbstractThingId], List[Union[str, AbstractThingId]]]] = empty_list()
    interacting_taxon_ref: Optional[Union[Union[str, TaxonId], List[Union[str, TaxonId]]]] = empty_list()
    annotation_date: Optional[Union[str, XSDDateTime]] = None
    annotation_extensions: Optional[Union[Union[dict, ConjunctionExtensionExpression], List[Union[dict, ConjunctionExtensionExpression]]]] = empty_list()
    annotation_properties: Optional[Union[Union[dict, PropertyValuePair], List[Union[dict, PropertyValuePair]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.db_object_ref is None:
            raise ValueError("db_object_ref must be supplied")
        if not isinstance(self.db_object_ref, AbstractThingId):
            self.db_object_ref = AbstractThingId(self.db_object_ref)

        if self.ontology_class_ref is None:
            raise ValueError("ontology_class_ref must be supplied")
        if not isinstance(self.ontology_class_ref, AbstractThingId):
            self.ontology_class_ref = AbstractThingId(self.ontology_class_ref)

        if self.supporting_references is None:
            raise ValueError("supporting_references must be supplied")
        elif not isinstance(self.supporting_references, list):
            self.supporting_references = [self.supporting_references]
        elif len(self.supporting_references) == 0:
            raise ValueError(f"supporting_references must be a non-empty list")
        self.supporting_references = [v if isinstance(v, PublicationId) else PublicationId(v) for v in self.supporting_references]

        if self.evidence_type is None:
            raise ValueError("evidence_type must be supplied")
        if not isinstance(self.evidence_type, OntologyClassId):
            self.evidence_type = OntologyClassId(self.evidence_type)

        if self.assigned_by is None:
            raise ValueError("assigned_by must be supplied")
        if not isinstance(self.assigned_by, ProviderId):
            self.assigned_by = ProviderId(self.assigned_by)

        if self.negation is not None and not isinstance(self.negation, Bool):
            self.negation = Bool(self.negation)

        if self.relation is not None and not isinstance(self.relation, RelationTermId):
            self.relation = RelationTermId(self.relation)

        if self.with_or_from is None:
            self.with_or_from = []
        if not isinstance(self.with_or_from, list):
            self.with_or_from = [self.with_or_from]
        self.with_or_from = [v if isinstance(v, AbstractThingId) else AbstractThingId(v) for v in self.with_or_from]

        if self.interacting_taxon_ref is None:
            self.interacting_taxon_ref = []
        if not isinstance(self.interacting_taxon_ref, list):
            self.interacting_taxon_ref = [self.interacting_taxon_ref]
        self.interacting_taxon_ref = [v if isinstance(v, TaxonId) else TaxonId(v) for v in self.interacting_taxon_ref]

        if self.annotation_date is not None and not isinstance(self.annotation_date, XSDDateTime):
            self.annotation_date = XSDDateTime(self.annotation_date)

        if self.annotation_extensions is None:
            self.annotation_extensions = []
        if not isinstance(self.annotation_extensions, list):
            self.annotation_extensions = [self.annotation_extensions]
        self.annotation_extensions = [v if isinstance(v, ConjunctionExtensionExpression) else ConjunctionExtensionExpression(**v) for v in self.annotation_extensions]

        if self.annotation_properties is None:
            self.annotation_properties = []
        if not isinstance(self.annotation_properties, list):
            self.annotation_properties = [self.annotation_properties]
        self.annotation_properties = [v if isinstance(v, PropertyValuePair) else PropertyValuePair(**v) for v in self.annotation_properties]

        super().__post_init__(**kwargs)


@dataclass
class GpadAssociationDocument(AssociationDocument):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.GpadAssociationDocument
    class_class_curie: ClassVar[str] = "ontology_association:GpadAssociationDocument"
    class_name: ClassVar[str] = "gpad association document"
    class_model_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.GpadAssociationDocument

    associations: Optional[Union[Union[dict, GpadAssociation], List[Union[dict, GpadAssociation]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.associations is None:
            self.associations = []
        if not isinstance(self.associations, list):
            self.associations = [self.associations]
        self._normalize_inlined_slot(slot_name="associations", slot_type=GpadAssociation, key_name="db object ref", inlined_as_list=True, keyed=False)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.gpad_association_document_associations = Slot(uri=ONTOLOGY_ASSOCIATION.associations, name="gpad association document_associations", curie=ONTOLOGY_ASSOCIATION.curie('associations'),
                   model_uri=ONTOLOGY_ASSOCIATION.gpad_association_document_associations, domain=GpadAssociationDocument, range=Optional[Union[Union[dict, GpadAssociation], List[Union[dict, GpadAssociation]]]])
