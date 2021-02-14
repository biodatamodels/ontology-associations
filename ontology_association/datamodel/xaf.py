# Auto generated from xaf.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-02-13 18:36
# Schema: xaf
#
# id: https://w3id.org/ontology_association/xaf
# description: Generalization/weakening of GAF
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
from . association import ConjunctionExtensionExpression, NameType, NamedThingId, OntologyClassId, ProviderId, RelationTermId, SymbolType, TaxonId
from biolinkml.utils.metamodelcore import XSDDateTime
from includes.types import Datetime, String

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
class GafAssociation(YAMLRoot):
    """
    line of GAF
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.GafAssociation
    class_class_curie: ClassVar[str] = "ontology_association:GafAssociation"
    class_name: ClassVar[str] = "gaf association"
    class_model_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.GafAssociation

    db: str = None
    local_id: str = None
    db_object_symbol: Union[str, SymbolType] = None
    ontology_class_ref: Union[str, NamedThingId] = None
    references: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    evidence_type: Union[str, OntologyClassId] = None
    aspect: str = None
    db_object_taxon: Union[str, TaxonId] = None
    assigned_by: Union[str, ProviderId] = None
    relation: Optional[Union[str, RelationTermId]] = None
    with_or_from: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()
    db_object_name: Optional[Union[str, NameType]] = None
    db_object_synonyms: Optional[Union[Union[str, NameType], List[Union[str, NameType]]]] = empty_list()
    db_object_type: Optional[Union[str, "GpEntityTypeEnum"]] = None
    annotation_date: Optional[Union[str, XSDDateTime]] = None
    annotation_extensions: Optional[Union[Union[dict, ConjunctionExtensionExpression], List[Union[dict, ConjunctionExtensionExpression]]]] = empty_list()

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

        if self.ontology_class_ref is None:
            raise ValueError("ontology_class_ref must be supplied")
        if not isinstance(self.ontology_class_ref, NamedThingId):
            self.ontology_class_ref = NamedThingId(self.ontology_class_ref)

        if self.references is None:
            raise ValueError("references must be supplied")
        elif not isinstance(self.references, list):
            self.references = [self.references]
        elif len(self.references) == 0:
            raise ValueError(f"references must be a non-empty list")
        self.references = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.references]

        if self.evidence_type is None:
            raise ValueError("evidence_type must be supplied")
        if not isinstance(self.evidence_type, OntologyClassId):
            self.evidence_type = OntologyClassId(self.evidence_type)

        if self.aspect is None:
            raise ValueError("aspect must be supplied")
        if not isinstance(self.aspect, str):
            self.aspect = str(self.aspect)

        if self.db_object_taxon is None:
            raise ValueError("db_object_taxon must be supplied")
        if not isinstance(self.db_object_taxon, TaxonId):
            self.db_object_taxon = TaxonId(self.db_object_taxon)

        if self.assigned_by is None:
            raise ValueError("assigned_by must be supplied")
        if not isinstance(self.assigned_by, ProviderId):
            self.assigned_by = ProviderId(self.assigned_by)

        if self.relation is not None and not isinstance(self.relation, RelationTermId):
            self.relation = RelationTermId(self.relation)

        if self.with_or_from is None:
            self.with_or_from = []
        if not isinstance(self.with_or_from, list):
            self.with_or_from = [self.with_or_from]
        self.with_or_from = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.with_or_from]

        if self.db_object_name is not None and not isinstance(self.db_object_name, NameType):
            self.db_object_name = NameType(self.db_object_name)

        if self.db_object_synonyms is None:
            self.db_object_synonyms = []
        if not isinstance(self.db_object_synonyms, list):
            self.db_object_synonyms = [self.db_object_synonyms]
        self.db_object_synonyms = [v if isinstance(v, NameType) else NameType(v) for v in self.db_object_synonyms]

        if self.db_object_type is not None and not isinstance(self.db_object_type, GpEntityTypeEnum):
            self.db_object_type = GpEntityTypeEnum(self.db_object_type)

        if self.annotation_date is not None and not isinstance(self.annotation_date, XSDDateTime):
            self.annotation_date = XSDDateTime(self.annotation_date)

        if self.annotation_extensions is None:
            self.annotation_extensions = []
        if not isinstance(self.annotation_extensions, list):
            self.annotation_extensions = [self.annotation_extensions]
        self.annotation_extensions = [v if isinstance(v, ConjunctionExtensionExpression) else ConjunctionExtensionExpression(**v) for v in self.annotation_extensions]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.gaf_association_aspect = Slot(uri=ONTOLOGY_ASSOCIATION.aspect, name="gaf association_aspect", curie=ONTOLOGY_ASSOCIATION.curie('aspect'),
                   model_uri=ONTOLOGY_ASSOCIATION.gaf_association_aspect, domain=GafAssociation, range=str)
