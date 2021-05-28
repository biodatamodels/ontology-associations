# Auto generated from gaf.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-05-27 19:28
# Schema: gaf
#
# id: https://w3id.org/ontology_association/gaf
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
from . association import AbstractThingId, Association, AssociationDocument, BiologicalEntity, ConjunctionExtensionExpression, NameType, OntologyClassId, PropertyValuePair, ProviderId, PublicationId, SymbolType, TaxonId, XafAssociation
from linkml.utils.metamodelcore import Bool, XSDDateTime
from linkml_model.types import Boolean, Datetime, String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
GO = CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_')
PR = CurieNamespace('PR', 'http://purl.obolibrary.org/obo/PR_')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
SO = CurieNamespace('SO', 'http://purl.obolibrary.org/obo/SO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
ONTOLOGY_ASSOCIATION = CurieNamespace('ontology_association', 'https://w3id.org/ontology_association/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
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
    relation: Union[str, "Gp2termRelationEnum"] = None
    ontology_class_ref: Union[str, AbstractThingId] = None
    supporting_references: Union[Union[str, PublicationId], List[Union[str, PublicationId]]] = None
    evidence_type: Union[str, OntologyClassId] = None
    assigned_by: Union[str, ProviderId] = None
    negation: Optional[Union[bool, Bool]] = None
    with_or_from: Optional[Union[Union[str, AbstractThingId], List[Union[str, AbstractThingId]]]] = empty_list()
    interacting_taxon_ref: Optional[Union[Union[str, TaxonId], List[Union[str, TaxonId]]]] = empty_list()
    annotation_date: Optional[Union[str, XSDDateTime]] = None
    annotation_extensions: Optional[Union[Union[dict, ConjunctionExtensionExpression], List[Union[dict, ConjunctionExtensionExpression]]]] = empty_list()
    annotation_properties: Optional[Union[Union[dict, PropertyValuePair], List[Union[dict, PropertyValuePair]]]] = empty_list()
    db_object_type: Optional[Union[str, "GpEntityTypeEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.db_object_ref is None:
            raise ValueError("db_object_ref must be supplied")
        if not isinstance(self.db_object_ref, AbstractThingId):
            self.db_object_ref = AbstractThingId(self.db_object_ref)

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

        if self.assigned_by is None:
            raise ValueError("assigned_by must be supplied")
        if not isinstance(self.assigned_by, ProviderId):
            self.assigned_by = ProviderId(self.assigned_by)

        if self.negation is not None and not isinstance(self.negation, Bool):
            self.negation = Bool(self.negation)

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

        if self.db_object_type is not None and not isinstance(self.db_object_type, GpEntityTypeEnum):
            self.db_object_type = GpEntityTypeEnum(self.db_object_type)

        super().__post_init__(**kwargs)


@dataclass
class GafAssociation(XafAssociation):
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
    ontology_class_ref: Union[str, AbstractThingId] = None
    supporting_references: Union[Union[str, PublicationId], List[Union[str, PublicationId]]] = None
    evidence_type: Union[str, OntologyClassId] = None
    aspect: Union[str, "GeneOntologyAspectEnum"] = None
    db_object_taxon: Union[str, TaxonId] = None
    assigned_by: Union[str, ProviderId] = None
    qualifiers: Optional[Union[Union[str, "Gp2termRelationEnum"], List[Union[str, "Gp2termRelationEnum"]]]] = empty_list()
    with_or_from: Optional[Union[Union[str, AbstractThingId], List[Union[str, AbstractThingId]]]] = empty_list()
    db_object_name: Optional[Union[str, NameType]] = None
    db_object_synonyms: Optional[Union[Union[str, NameType], List[Union[str, NameType]]]] = empty_list()
    db_object_type: Optional[Union[str, "GpEntityTypeEnum"]] = None
    annotation_date: Optional[Union[str, XSDDateTime]] = None
    annotation_extensions: Optional[Union[Union[dict, ConjunctionExtensionExpression], List[Union[dict, ConjunctionExtensionExpression]]]] = empty_list()
    gene_product_form: Optional[Union[dict, BiologicalEntity]] = None

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
        if not isinstance(self.aspect, GeneOntologyAspectEnum):
            self.aspect = GeneOntologyAspectEnum(self.aspect)

        if self.db_object_taxon is None:
            raise ValueError("db_object_taxon must be supplied")
        if not isinstance(self.db_object_taxon, TaxonId):
            self.db_object_taxon = TaxonId(self.db_object_taxon)

        if self.assigned_by is None:
            raise ValueError("assigned_by must be supplied")
        if not isinstance(self.assigned_by, ProviderId):
            self.assigned_by = ProviderId(self.assigned_by)

        if self.qualifiers is None:
            self.qualifiers = []
        if not isinstance(self.qualifiers, list):
            self.qualifiers = [self.qualifiers]
        self.qualifiers = [v if isinstance(v, Gp2termRelationEnum) else Gp2termRelationEnum(v) for v in self.qualifiers]

        if self.with_or_from is None:
            self.with_or_from = []
        if not isinstance(self.with_or_from, list):
            self.with_or_from = [self.with_or_from]
        self.with_or_from = [v if isinstance(v, AbstractThingId) else AbstractThingId(v) for v in self.with_or_from]

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

        if self.gene_product_form is not None and not isinstance(self.gene_product_form, BiologicalEntity):
            self.gene_product_form = BiologicalEntity()

        super().__post_init__(**kwargs)


@dataclass
class SimpleGafAssociation(GafAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.SimpleGafAssociation
    class_class_curie: ClassVar[str] = "ontology_association:SimpleGafAssociation"
    class_name: ClassVar[str] = "simple gaf association"
    class_model_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.SimpleGafAssociation

    db: str = None
    local_id: str = None
    db_object_symbol: Union[str, SymbolType] = None
    ontology_class_ref: Union[str, AbstractThingId] = None
    supporting_references: Union[Union[str, PublicationId], List[Union[str, PublicationId]]] = None
    evidence_type: Union[str, OntologyClassId] = None
    aspect: Union[str, "GeneOntologyAspectEnum"] = None
    db_object_taxon: Union[str, TaxonId] = None
    assigned_by: Union[str, ProviderId] = None
    qualifiers: Optional[Union[Union[str, "SimpleQualifierEnum"], List[Union[str, "SimpleQualifierEnum"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.qualifiers is None:
            self.qualifiers = []
        if not isinstance(self.qualifiers, list):
            self.qualifiers = [self.qualifiers]
        self.qualifiers = [v if isinstance(v, SimpleQualifierEnum) else SimpleQualifierEnum(v) for v in self.qualifiers]

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


@dataclass
class GafAssociationDocument(AssociationDocument):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.GafAssociationDocument
    class_class_curie: ClassVar[str] = "ontology_association:GafAssociationDocument"
    class_name: ClassVar[str] = "gaf association document"
    class_model_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.GafAssociationDocument

    associations: Optional[Union[Union[dict, GafAssociation], List[Union[dict, GafAssociation]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.associations is None:
            self.associations = []
        if not isinstance(self.associations, list):
            self.associations = [self.associations]
        self._normalize_inlined_slot(slot_name="associations", slot_type=GafAssociation, key_name="db", inlined_as_list=True, keyed=False)

        super().__post_init__(**kwargs)


# Enumerations
class GeneOntologyAspectEnum(EnumDefinitionImpl):

    F = PermissibleValue(text="F",
                         description="molecular_function",
                         meaning=GO["0003674"])
    P = PermissibleValue(text="P",
                         description="biological_process",
                         meaning=GO["0008150"])
    C = PermissibleValue(text="C",
                         description="cellular_component",
                         meaning=GO["0005575"])

    _defn = EnumDefinition(
        name="GeneOntologyAspectEnum",
    )

class GpEntityTypeEnum(EnumDefinitionImpl):

    protein_coding_gene = PermissibleValue(text="protein_coding_gene",
                                                             meaning=SO["0001217"])
    ncRNA_gene = PermissibleValue(text="ncRNA_gene",
                                           meaning=SO["0001263"])
    mRNA = PermissibleValue(text="mRNA",
                               meaning=SO["0000234"])
    ncRNA = PermissibleValue(text="ncRNA",
                                 meaning=SO["0000655"])
    protein = PermissibleValue(text="protein",
                                     meaning=PR["000000001"])
    genetic_marker = PermissibleValue(text="genetic_marker",
                                                   meaning=SO["0001645"])

    _defn = EnumDefinition(
        name="GpEntityTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "protein-containing complex",
                PermissibleValue(text="protein-containing complex",
                                 meaning=GO["0032991"]) )

class Gp2termRelationEnum(EnumDefinitionImpl):

    NOT = PermissibleValue(text="NOT",
                             meaning=OWL.complementOf)
    enables = PermissibleValue(text="enables",
                                     meaning=RO["0002327"])
    involved_in = PermissibleValue(text="involved_in",
                                             meaning=RO["0002331"])
    located_in = PermissibleValue(text="located_in",
                                           meaning=RO["0001025"])
    contributes_to = PermissibleValue(text="contributes_to",
                                                   meaning=RO["0002326"])
    acts_upstream_of = PermissibleValue(text="acts_upstream_of",
                                                       meaning=RO["0002263"])
    part_of = PermissibleValue(text="part_of",
                                     meaning=BFO["0000050"])
    acts_upstream_of_positive_effect = PermissibleValue(text="acts_upstream_of_positive_effect",
                                                                                       meaning=RO["0004034"])
    is_active_in = PermissibleValue(text="is_active_in",
                                               meaning=RO["0002432"])
    acts_upstream_of_negative_effect = PermissibleValue(text="acts_upstream_of_negative_effect",
                                                                                       meaning=RO["0004035"])
    colocalizes_with = PermissibleValue(text="colocalizes_with",
                                                       meaning=RO["0002325"])
    acts_upstream_of_or_within = PermissibleValue(text="acts_upstream_of_or_within",
                                                                           meaning=RO["0002264"])
    acts_upstream_of_or_within_positive_effect = PermissibleValue(text="acts_upstream_of_or_within_positive_effect",
                                                                                                           meaning=RO["0004032"])
    acts_upstream_of_or_within_negative_effect = PermissibleValue(text="acts_upstream_of_or_within_negative_effect",
                                                                                                           meaning=RO["0004033"])

    _defn = EnumDefinition(
        name="Gp2termRelationEnum",
    )

class SimpleQualifierEnum(EnumDefinitionImpl):

    NOT = PermissibleValue(text="NOT",
                             meaning=OWL.complementOf)
    contributes_to = PermissibleValue(text="contributes_to",
                                                   meaning=RO["0002326"])

    _defn = EnumDefinition(
        name="SimpleQualifierEnum",
    )

# Slots
class slots:
    pass

slots.gpad_association_db_object_type = Slot(uri=ONTOLOGY_ASSOCIATION.db_object_type, name="gpad association_db object type", curie=ONTOLOGY_ASSOCIATION.curie('db_object_type'),
                   model_uri=ONTOLOGY_ASSOCIATION.gpad_association_db_object_type, domain=GpadAssociation, range=Optional[Union[str, "GpEntityTypeEnum"]])

slots.gpad_association_relation = Slot(uri=ONTOLOGY_ASSOCIATION.relation, name="gpad association_relation", curie=ONTOLOGY_ASSOCIATION.curie('relation'),
                   model_uri=ONTOLOGY_ASSOCIATION.gpad_association_relation, domain=GpadAssociation, range=Union[str, "Gp2termRelationEnum"])

slots.gpad_association_document_associations = Slot(uri=ONTOLOGY_ASSOCIATION.associations, name="gpad association document_associations", curie=ONTOLOGY_ASSOCIATION.curie('associations'),
                   model_uri=ONTOLOGY_ASSOCIATION.gpad_association_document_associations, domain=GpadAssociationDocument, range=Optional[Union[Union[dict, GpadAssociation], List[Union[dict, GpadAssociation]]]])

slots.gaf_association_ontology_class_ref = Slot(uri=ONTOLOGY_ASSOCIATION.ontology_class_ref, name="gaf association_ontology class ref", curie=ONTOLOGY_ASSOCIATION.curie('ontology_class_ref'),
                   model_uri=ONTOLOGY_ASSOCIATION.gaf_association_ontology_class_ref, domain=GafAssociation, range=Union[str, AbstractThingId],
                   pattern=re.compile(r'^GO:\d+'))

slots.gaf_association_db_object_type = Slot(uri=ONTOLOGY_ASSOCIATION.db_object_type, name="gaf association_db object type", curie=ONTOLOGY_ASSOCIATION.curie('db_object_type'),
                   model_uri=ONTOLOGY_ASSOCIATION.gaf_association_db_object_type, domain=GafAssociation, range=Optional[Union[str, "GpEntityTypeEnum"]])

slots.gaf_association_aspect = Slot(uri=ONTOLOGY_ASSOCIATION.aspect, name="gaf association_aspect", curie=ONTOLOGY_ASSOCIATION.curie('aspect'),
                   model_uri=ONTOLOGY_ASSOCIATION.gaf_association_aspect, domain=GafAssociation, range=Union[str, "GeneOntologyAspectEnum"])

slots.gaf_association_qualifiers = Slot(uri=ONTOLOGY_ASSOCIATION.qualifiers, name="gaf association_qualifiers", curie=ONTOLOGY_ASSOCIATION.curie('qualifiers'),
                   model_uri=ONTOLOGY_ASSOCIATION.gaf_association_qualifiers, domain=GafAssociation, range=Optional[Union[Union[str, "Gp2termRelationEnum"], List[Union[str, "Gp2termRelationEnum"]]]])

slots.simple_gaf_association_qualifiers = Slot(uri=ONTOLOGY_ASSOCIATION.qualifiers, name="simple gaf association_qualifiers", curie=ONTOLOGY_ASSOCIATION.curie('qualifiers'),
                   model_uri=ONTOLOGY_ASSOCIATION.simple_gaf_association_qualifiers, domain=SimpleGafAssociation, range=Optional[Union[Union[str, "SimpleQualifierEnum"], List[Union[str, "SimpleQualifierEnum"]]]])

slots.gaf_association_document_associations = Slot(uri=ONTOLOGY_ASSOCIATION.associations, name="gaf association document_associations", curie=ONTOLOGY_ASSOCIATION.curie('associations'),
                   model_uri=ONTOLOGY_ASSOCIATION.gaf_association_document_associations, domain=GafAssociationDocument, range=Optional[Union[Union[dict, GafAssociation], List[Union[dict, GafAssociation]]]])
