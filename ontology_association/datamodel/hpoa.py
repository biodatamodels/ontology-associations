# Auto generated from hpoa.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-05-27 10:07
# Schema: hpoa
#
# id: https://w3id.org/ontology_association/hpoa
# description: Various association data models
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml.utils.slot import Slot
from linkml.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml.utils.formatutils import camelcase, underscore, sfx
from linkml.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml.utils.curienamespace import CurieNamespace
from . association import AbstractThingId, Association, AssociationDocument, Gp2termRelationEnum, NameType, OntologyClassId, ProviderId, PublicationId, SymbolType
from linkml.utils.metamodelcore import XSDDateTime
from linkml_model.types import Datetime, String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
ONTOLOGY_ASSOCIATION = CurieNamespace('ontology_association', 'https://w3id.org/ontology_association/')
DEFAULT_ = ONTOLOGY_ASSOCIATION


# Types

# Class references



@dataclass
class HumanPhenotypeOntologyAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.HumanPhenotypeOntologyAssociation
    class_class_curie: ClassVar[str] = "ontology_association:HumanPhenotypeOntologyAssociation"
    class_name: ClassVar[str] = "human phenotype ontology association"
    class_model_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.HumanPhenotypeOntologyAssociation

    db: str = None
    local_id: str = None
    db_object_symbol: Union[str, SymbolType] = None
    relation: Union[str, "Gp2termRelationEnum"] = None
    ontology_class_ref: Union[str, AbstractThingId] = None
    supporting_references: Union[Union[str, PublicationId], List[Union[str, PublicationId]]] = None
    evidence_type: Union[str, OntologyClassId] = None
    aspect: str = None
    assigned_by: Union[str, ProviderId] = None
    onset: Optional[str] = None
    frequency: Optional[str] = None
    with_or_from: Optional[Union[Union[str, AbstractThingId], List[Union[str, AbstractThingId]]]] = empty_list()
    db_object_synonyms: Optional[Union[Union[str, NameType], List[Union[str, NameType]]]] = empty_list()
    annotation_date: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.db is None:
            raise ValueError("db must be supplied")
        if not isinstance(self.db, str):
            self.db = str(self.db)

        if self.local_id is None:
            raise ValueError("local_id must be supplied")
        if not isinstance(self.local_id, str):
            self.local_id = str(self.local_id)

        if self.db_object_symbol is None:
            raise ValueError("db_object_symbol must be supplied")
        if not isinstance(self.db_object_symbol, SymbolType):
            self.db_object_symbol = SymbolType(self.db_object_symbol)

        if self.relation is None:
            raise ValueError("relation must be supplied")
        if not isinstance(self.relation, Gp2termRelationEnum):
            self.relation = Gp2termRelationEnum(self.relation)

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

        if self.aspect is None:
            raise ValueError("aspect must be supplied")
        if not isinstance(self.aspect, str):
            self.aspect = str(self.aspect)

        if self.assigned_by is None:
            raise ValueError("assigned_by must be supplied")
        if not isinstance(self.assigned_by, ProviderId):
            self.assigned_by = ProviderId(self.assigned_by)

        if self.onset is not None and not isinstance(self.onset, str):
            self.onset = str(self.onset)

        if self.frequency is not None and not isinstance(self.frequency, str):
            self.frequency = str(self.frequency)

        if self.with_or_from is None:
            self.with_or_from = []
        if not isinstance(self.with_or_from, list):
            self.with_or_from = [self.with_or_from]
        self.with_or_from = [v if isinstance(v, AbstractThingId) else AbstractThingId(v) for v in self.with_or_from]

        if self.db_object_synonyms is None:
            self.db_object_synonyms = []
        if not isinstance(self.db_object_synonyms, list):
            self.db_object_synonyms = [self.db_object_synonyms]
        self.db_object_synonyms = [v if isinstance(v, NameType) else NameType(v) for v in self.db_object_synonyms]

        if self.annotation_date is not None and not isinstance(self.annotation_date, XSDDateTime):
            self.annotation_date = XSDDateTime(self.annotation_date)

        super().__post_init__(**kwargs)


@dataclass
class HumanPhenotypeOntologyAssociationDocument(AssociationDocument):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.HumanPhenotypeOntologyAssociationDocument
    class_class_curie: ClassVar[str] = "ontology_association:HumanPhenotypeOntologyAssociationDocument"
    class_name: ClassVar[str] = "human phenotype ontology association document"
    class_model_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.HumanPhenotypeOntologyAssociationDocument

    associations: Optional[Union[Union[dict, HumanPhenotypeOntologyAssociation], List[Union[dict, HumanPhenotypeOntologyAssociation]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.associations is None:
            self.associations = []
        if not isinstance(self.associations, list):
            self.associations = [self.associations]
        self._normalize_inlined_slot(slot_name="associations", slot_type=HumanPhenotypeOntologyAssociation, key_name="db", inlined_as_list=True, keyed=False)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.onset = Slot(uri=ONTOLOGY_ASSOCIATION.onset, name="onset", curie=ONTOLOGY_ASSOCIATION.curie('onset'),
                   model_uri=ONTOLOGY_ASSOCIATION.onset, domain=None, range=Optional[str])

slots.frequency = Slot(uri=ONTOLOGY_ASSOCIATION.frequency, name="frequency", curie=ONTOLOGY_ASSOCIATION.curie('frequency'),
                   model_uri=ONTOLOGY_ASSOCIATION.frequency, domain=None, range=Optional[str])

slots.human_phenotype_ontology_association_document_associations = Slot(uri=ONTOLOGY_ASSOCIATION.associations, name="human phenotype ontology association document_associations", curie=ONTOLOGY_ASSOCIATION.curie('associations'),
                   model_uri=ONTOLOGY_ASSOCIATION.human_phenotype_ontology_association_document_associations, domain=HumanPhenotypeOntologyAssociationDocument, range=Optional[Union[Union[dict, HumanPhenotypeOntologyAssociation], List[Union[dict, HumanPhenotypeOntologyAssociation]]]])
