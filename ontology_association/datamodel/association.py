# Auto generated from association.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-05-27 10:58
# Schema: ontology_association
#
# id: https://w3id.org/ontology_association
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
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = ONTOLOGY_ASSOCIATION


# Types
class Curie(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "curie"
    type_model_uri = ONTOLOGY_ASSOCIATION.Curie


class SymbolType(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "symbol type"
    type_model_uri = ONTOLOGY_ASSOCIATION.SymbolType


class NameType(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "name type"
    type_model_uri = ONTOLOGY_ASSOCIATION.NameType


# Class references
class AbstractThingId(Curie):
    pass


class ProviderId(AbstractThingId):
    pass


class PublicationId(AbstractThingId):
    pass


class ControlledTermId(AbstractThingId):
    pass


class OntologyClassId(ControlledTermId):
    pass


class TaxonId(OntologyClassId):
    pass


class RelationTermId(ControlledTermId):
    pass


class Entity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.Entity
    class_class_curie: ClassVar[str] = "ontology_association:Entity"
    class_name: ClassVar[str] = "entity"
    class_model_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.Entity


class BiologicalEntity(Entity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.BiologicalEntity
    class_class_curie: ClassVar[str] = "ontology_association:BiologicalEntity"
    class_name: ClassVar[str] = "biological entity"
    class_model_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.BiologicalEntity


@dataclass
class AbstractThing(Entity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.AbstractThing
    class_class_curie: ClassVar[str] = "ontology_association:AbstractThing"
    class_name: ClassVar[str] = "abstract thing"
    class_model_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.AbstractThing

    id: Union[str, AbstractThingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, AbstractThingId):
            self.id = AbstractThingId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Provider(AbstractThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.Provider
    class_class_curie: ClassVar[str] = "ontology_association:Provider"
    class_name: ClassVar[str] = "provider"
    class_model_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.Provider

    id: Union[str, ProviderId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ProviderId):
            self.id = ProviderId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Publication(AbstractThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.Publication
    class_class_curie: ClassVar[str] = "ontology_association:Publication"
    class_name: ClassVar[str] = "publication"
    class_model_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.Publication

    id: Union[str, PublicationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PublicationId):
            self.id = PublicationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ControlledTerm(AbstractThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.ControlledTerm
    class_class_curie: ClassVar[str] = "ontology_association:ControlledTerm"
    class_name: ClassVar[str] = "controlled term"
    class_model_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.ControlledTerm

    id: Union[str, ControlledTermId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ControlledTermId):
            self.id = ControlledTermId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class OntologyClass(ControlledTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.OntologyClass
    class_class_curie: ClassVar[str] = "ontology_association:OntologyClass"
    class_name: ClassVar[str] = "ontology class"
    class_model_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.OntologyClass

    id: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Taxon(OntologyClass):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.Taxon
    class_class_curie: ClassVar[str] = "ontology_association:Taxon"
    class_name: ClassVar[str] = "taxon"
    class_model_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.Taxon

    id: Union[str, TaxonId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, TaxonId):
            self.id = TaxonId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class RelationTerm(ControlledTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.RelationTerm
    class_class_curie: ClassVar[str] = "ontology_association:RelationTerm"
    class_name: ClassVar[str] = "relation term"
    class_model_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.RelationTerm

    id: Union[str, RelationTermId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, RelationTermId):
            self.id = RelationTermId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class PropertyValuePair(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.PropertyValuePair
    class_class_curie: ClassVar[str] = "ontology_association:PropertyValuePair"
    class_name: ClassVar[str] = "property value pair"
    class_model_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.PropertyValuePair

    property: Optional[Union[str, ControlledTermId]] = None
    value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.property is not None and not isinstance(self.property, ControlledTermId):
            self.property = ControlledTermId(self.property)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


class ConjunctionExtensionExpression(YAMLRoot):
    """
    set of expressions all true
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.ConjunctionExtensionExpression
    class_class_curie: ClassVar[str] = "ontology_association:ConjunctionExtensionExpression"
    class_name: ClassVar[str] = "conjunction extension expression"
    class_model_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.ConjunctionExtensionExpression


class Association(YAMLRoot):
    """
    generic association
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.Association
    class_class_curie: ClassVar[str] = "ontology_association:Association"
    class_name: ClassVar[str] = "association"
    class_model_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.Association


@dataclass
class XafAssociation(Association):
    """
    line of xAF. xAF is a generalization of GAF designed to work for other ontologies than GO, and for other entities
    beyond genes and proteins. xAF has the same column headers to GAF, but has fewer restrictions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.XafAssociation
    class_class_curie: ClassVar[str] = "ontology_association:XafAssociation"
    class_name: ClassVar[str] = "xaf association"
    class_model_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.XafAssociation

    db: str = None
    local_id: str = None
    db_object_symbol: Union[str, SymbolType] = None
    ontology_class_ref: Union[str, AbstractThingId] = None
    supporting_references: Union[Union[str, PublicationId], List[Union[str, PublicationId]]] = None
    evidence_type: Union[str, OntologyClassId] = None
    aspect: str = None
    db_object_taxon: Union[str, TaxonId] = None
    assigned_by: Union[str, ProviderId] = None
    qualifiers: Optional[Union[str, List[str]]] = empty_list()
    with_or_from: Optional[Union[Union[str, AbstractThingId], List[Union[str, AbstractThingId]]]] = empty_list()
    db_object_name: Optional[Union[str, NameType]] = None
    db_object_synonyms: Optional[Union[Union[str, NameType], List[Union[str, NameType]]]] = empty_list()
    db_object_type: Optional[str] = None
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

        if self.qualifiers is None:
            self.qualifiers = []
        if not isinstance(self.qualifiers, list):
            self.qualifiers = [self.qualifiers]
        self.qualifiers = [v if isinstance(v, str) else str(v) for v in self.qualifiers]

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

        if self.db_object_type is not None and not isinstance(self.db_object_type, str):
            self.db_object_type = str(self.db_object_type)

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


class Document(YAMLRoot):
    """
    root class for association or entity documents
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.Document
    class_class_curie: ClassVar[str] = "ontology_association:Document"
    class_name: ClassVar[str] = "document"
    class_model_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.Document


@dataclass
class AssociationDocument(Document):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.AssociationDocument
    class_class_curie: ClassVar[str] = "ontology_association:AssociationDocument"
    class_name: ClassVar[str] = "association document"
    class_model_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.AssociationDocument

    date_generated: Optional[str] = None
    generated_by: Optional[Union[str, ProviderId]] = None
    url: Optional[str] = None
    project_release: Optional[str] = None
    funding: Optional[str] = None
    go_version: Optional[str] = None
    ro_version: Optional[str] = None
    gorel_version: Optional[str] = None
    associations: Optional[Union[Union[dict, Association], List[Union[dict, Association]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.date_generated is not None and not isinstance(self.date_generated, str):
            self.date_generated = str(self.date_generated)

        if self.generated_by is not None and not isinstance(self.generated_by, ProviderId):
            self.generated_by = ProviderId(self.generated_by)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        if self.project_release is not None and not isinstance(self.project_release, str):
            self.project_release = str(self.project_release)

        if self.funding is not None and not isinstance(self.funding, str):
            self.funding = str(self.funding)

        if self.go_version is not None and not isinstance(self.go_version, str):
            self.go_version = str(self.go_version)

        if self.ro_version is not None and not isinstance(self.ro_version, str):
            self.ro_version = str(self.ro_version)

        if self.gorel_version is not None and not isinstance(self.gorel_version, str):
            self.gorel_version = str(self.gorel_version)

        if self.associations is None:
            self.associations = []
        if not isinstance(self.associations, list):
            self.associations = [self.associations]
        self.associations = [v if isinstance(v, Association) else Association(**v) for v in self.associations]

        super().__post_init__(**kwargs)


class Denormalized(YAMLRoot):
    """
    mixin for a denormalized class. A denormalized class is formed from a join of two or more other classes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.Denormalized
    class_class_curie: ClassVar[str] = "ontology_association:Denormalized"
    class_name: ClassVar[str] = "denormalized"
    class_model_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.Denormalized


class Normalized(YAMLRoot):
    """
    mixin for a normalized class, in the sense of database normal forms
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.Normalized
    class_class_curie: ClassVar[str] = "ontology_association:Normalized"
    class_name: ClassVar[str] = "normalized"
    class_model_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.Normalized


class GoRelated(YAMLRoot):
    """
    mixin for any association that is GO related
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.GoRelated
    class_class_curie: ClassVar[str] = "ontology_association:GoRelated"
    class_name: ClassVar[str] = "go related"
    class_model_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.GoRelated


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=ONTOLOGY_ASSOCIATION.id, name="id", curie=ONTOLOGY_ASSOCIATION.curie('id'),
                   model_uri=ONTOLOGY_ASSOCIATION.id, domain=None, range=URIRef)

slots.local_id = Slot(uri=ONTOLOGY_ASSOCIATION.local_id, name="local id", curie=ONTOLOGY_ASSOCIATION.curie('local_id'),
                   model_uri=ONTOLOGY_ASSOCIATION.local_id, domain=None, range=str,
                   pattern=re.compile(r'\S+'))

slots.db = Slot(uri=ONTOLOGY_ASSOCIATION.db, name="db", curie=ONTOLOGY_ASSOCIATION.curie('db'),
                   model_uri=ONTOLOGY_ASSOCIATION.db, domain=None, range=str,
                   pattern=re.compile(r'[a-zA-Z0-9\.\-\_]+'))

slots.db_object_ref = Slot(uri=ONTOLOGY_ASSOCIATION.db_object_ref, name="db object ref", curie=ONTOLOGY_ASSOCIATION.curie('db_object_ref'),
                   model_uri=ONTOLOGY_ASSOCIATION.db_object_ref, domain=None, range=Union[str, AbstractThingId])

slots.aspect = Slot(uri=ONTOLOGY_ASSOCIATION.aspect, name="aspect", curie=ONTOLOGY_ASSOCIATION.curie('aspect'),
                   model_uri=ONTOLOGY_ASSOCIATION.aspect, domain=None, range=str)

slots.db_object_symbol = Slot(uri=ONTOLOGY_ASSOCIATION.db_object_symbol, name="db object symbol", curie=ONTOLOGY_ASSOCIATION.curie('db_object_symbol'),
                   model_uri=ONTOLOGY_ASSOCIATION.db_object_symbol, domain=None, range=Union[str, SymbolType])

slots.db_object_name = Slot(uri=ONTOLOGY_ASSOCIATION.db_object_name, name="db object name", curie=ONTOLOGY_ASSOCIATION.curie('db_object_name'),
                   model_uri=ONTOLOGY_ASSOCIATION.db_object_name, domain=None, range=Optional[Union[str, NameType]])

slots.db_object_synonyms = Slot(uri=ONTOLOGY_ASSOCIATION.db_object_synonyms, name="db object synonyms", curie=ONTOLOGY_ASSOCIATION.curie('db_object_synonyms'),
                   model_uri=ONTOLOGY_ASSOCIATION.db_object_synonyms, domain=None, range=Optional[Union[Union[str, NameType], List[Union[str, NameType]]]])

slots.db_object_type = Slot(uri=ONTOLOGY_ASSOCIATION.db_object_type, name="db object type", curie=ONTOLOGY_ASSOCIATION.curie('db_object_type'),
                   model_uri=ONTOLOGY_ASSOCIATION.db_object_type, domain=None, range=Optional[str])

slots.db_object_taxon = Slot(uri=ONTOLOGY_ASSOCIATION.db_object_taxon, name="db object taxon", curie=ONTOLOGY_ASSOCIATION.curie('db_object_taxon'),
                   model_uri=ONTOLOGY_ASSOCIATION.db_object_taxon, domain=None, range=Union[str, TaxonId])

slots.encoded_by = Slot(uri=ONTOLOGY_ASSOCIATION.encoded_by, name="encoded by", curie=ONTOLOGY_ASSOCIATION.curie('encoded_by'),
                   model_uri=ONTOLOGY_ASSOCIATION.encoded_by, domain=None, range=Optional[Union[Union[str, AbstractThingId], List[Union[str, AbstractThingId]]]])

slots.parent_protein = Slot(uri=ONTOLOGY_ASSOCIATION.parent_protein, name="parent protein", curie=ONTOLOGY_ASSOCIATION.curie('parent_protein'),
                   model_uri=ONTOLOGY_ASSOCIATION.parent_protein, domain=None, range=Optional[Union[Union[str, AbstractThingId], List[Union[str, AbstractThingId]]]])

slots.protein_containing_complex_members = Slot(uri=ONTOLOGY_ASSOCIATION.protein_containing_complex_members, name="protein containing complex members", curie=ONTOLOGY_ASSOCIATION.curie('protein_containing_complex_members'),
                   model_uri=ONTOLOGY_ASSOCIATION.protein_containing_complex_members, domain=None, range=Optional[Union[Union[str, AbstractThingId], List[Union[str, AbstractThingId]]]])

slots.db_xrefs = Slot(uri=ONTOLOGY_ASSOCIATION.db_xrefs, name="db xrefs", curie=ONTOLOGY_ASSOCIATION.curie('db_xrefs'),
                   model_uri=ONTOLOGY_ASSOCIATION.db_xrefs, domain=None, range=Optional[Union[Union[str, Curie], List[Union[str, Curie]]]])

slots.negation = Slot(uri=ONTOLOGY_ASSOCIATION.negation, name="negation", curie=ONTOLOGY_ASSOCIATION.curie('negation'),
                   model_uri=ONTOLOGY_ASSOCIATION.negation, domain=None, range=Optional[Union[bool, Bool]])

slots.ontology_class_ref = Slot(uri=ONTOLOGY_ASSOCIATION.ontology_class_ref, name="ontology class ref", curie=ONTOLOGY_ASSOCIATION.curie('ontology_class_ref'),
                   model_uri=ONTOLOGY_ASSOCIATION.ontology_class_ref, domain=None, range=Union[str, AbstractThingId])

slots.qualifiers = Slot(uri=ONTOLOGY_ASSOCIATION.qualifiers, name="qualifiers", curie=ONTOLOGY_ASSOCIATION.curie('qualifiers'),
                   model_uri=ONTOLOGY_ASSOCIATION.qualifiers, domain=None, range=Optional[Union[str, List[str]]])

slots.relation = Slot(uri=ONTOLOGY_ASSOCIATION.relation, name="relation", curie=ONTOLOGY_ASSOCIATION.curie('relation'),
                   model_uri=ONTOLOGY_ASSOCIATION.relation, domain=None, range=str)

slots.supporting_references = Slot(uri=ONTOLOGY_ASSOCIATION.supporting_references, name="supporting references", curie=ONTOLOGY_ASSOCIATION.curie('supporting_references'),
                   model_uri=ONTOLOGY_ASSOCIATION.supporting_references, domain=None, range=Union[Union[str, PublicationId], List[Union[str, PublicationId]]])

slots.with_or_from = Slot(uri=ONTOLOGY_ASSOCIATION.with_or_from, name="with or from", curie=ONTOLOGY_ASSOCIATION.curie('with_or_from'),
                   model_uri=ONTOLOGY_ASSOCIATION.with_or_from, domain=None, range=Optional[Union[Union[str, AbstractThingId], List[Union[str, AbstractThingId]]]])

slots.interacting_taxon_ref = Slot(uri=ONTOLOGY_ASSOCIATION.interacting_taxon_ref, name="interacting taxon ref", curie=ONTOLOGY_ASSOCIATION.curie('interacting_taxon_ref'),
                   model_uri=ONTOLOGY_ASSOCIATION.interacting_taxon_ref, domain=None, range=Optional[Union[Union[str, TaxonId], List[Union[str, TaxonId]]]])

slots.evidence_type = Slot(uri=ONTOLOGY_ASSOCIATION.evidence_type, name="evidence type", curie=ONTOLOGY_ASSOCIATION.curie('evidence_type'),
                   model_uri=ONTOLOGY_ASSOCIATION.evidence_type, domain=None, range=Union[str, OntologyClassId])

slots.bioentity_type = Slot(uri=ONTOLOGY_ASSOCIATION.bioentity_type, name="bioentity type", curie=ONTOLOGY_ASSOCIATION.curie('bioentity_type'),
                   model_uri=ONTOLOGY_ASSOCIATION.bioentity_type, domain=None, range=Optional[str])

slots.annotation_date = Slot(uri=ONTOLOGY_ASSOCIATION.annotation_date, name="annotation date", curie=ONTOLOGY_ASSOCIATION.curie('annotation_date'),
                   model_uri=ONTOLOGY_ASSOCIATION.annotation_date, domain=None, range=Optional[Union[str, XSDDateTime]],
                   pattern=re.compile(r'^\d{6}'))

slots.assigned_by = Slot(uri=ONTOLOGY_ASSOCIATION.assigned_by, name="assigned by", curie=ONTOLOGY_ASSOCIATION.curie('assigned_by'),
                   model_uri=ONTOLOGY_ASSOCIATION.assigned_by, domain=None, range=Union[str, ProviderId])

slots.gene_product_form = Slot(uri=ONTOLOGY_ASSOCIATION.gene_product_form, name="gene product form", curie=ONTOLOGY_ASSOCIATION.curie('gene_product_form'),
                   model_uri=ONTOLOGY_ASSOCIATION.gene_product_form, domain=None, range=Optional[Union[dict, BiologicalEntity]])

slots.annotation_extensions = Slot(uri=ONTOLOGY_ASSOCIATION.annotation_extensions, name="annotation extensions", curie=ONTOLOGY_ASSOCIATION.curie('annotation_extensions'),
                   model_uri=ONTOLOGY_ASSOCIATION.annotation_extensions, domain=None, range=Optional[Union[Union[dict, ConjunctionExtensionExpression], List[Union[dict, ConjunctionExtensionExpression]]]])

slots.annotation_properties = Slot(uri=ONTOLOGY_ASSOCIATION.annotation_properties, name="annotation properties", curie=ONTOLOGY_ASSOCIATION.curie('annotation_properties'),
                   model_uri=ONTOLOGY_ASSOCIATION.annotation_properties, domain=None, range=Optional[Union[Union[dict, PropertyValuePair], List[Union[dict, PropertyValuePair]]]])

slots.gene_product_properties = Slot(uri=ONTOLOGY_ASSOCIATION.gene_product_properties, name="gene product properties", curie=ONTOLOGY_ASSOCIATION.curie('gene_product_properties'),
                   model_uri=ONTOLOGY_ASSOCIATION.gene_product_properties, domain=None, range=Optional[Union[Union[dict, PropertyValuePair], List[Union[dict, PropertyValuePair]]]])

slots.document_metadata_field = Slot(uri=ONTOLOGY_ASSOCIATION.document_metadata_field, name="document metadata field", curie=ONTOLOGY_ASSOCIATION.curie('document_metadata_field'),
                   model_uri=ONTOLOGY_ASSOCIATION.document_metadata_field, domain=None, range=Optional[str])

slots.date_generated = Slot(uri=ONTOLOGY_ASSOCIATION.date_generated, name="date generated", curie=ONTOLOGY_ASSOCIATION.curie('date_generated'),
                   model_uri=ONTOLOGY_ASSOCIATION.date_generated, domain=None, range=Optional[str])

slots.generated_by = Slot(uri=ONTOLOGY_ASSOCIATION.generated_by, name="generated by", curie=ONTOLOGY_ASSOCIATION.curie('generated_by'),
                   model_uri=ONTOLOGY_ASSOCIATION.generated_by, domain=None, range=Optional[Union[str, ProviderId]])

slots.url = Slot(uri=ONTOLOGY_ASSOCIATION.url, name="url", curie=ONTOLOGY_ASSOCIATION.curie('url'),
                   model_uri=ONTOLOGY_ASSOCIATION.url, domain=None, range=Optional[str])

slots.project_release = Slot(uri=ONTOLOGY_ASSOCIATION.project_release, name="project release", curie=ONTOLOGY_ASSOCIATION.curie('project_release'),
                   model_uri=ONTOLOGY_ASSOCIATION.project_release, domain=None, range=Optional[str])

slots.funding = Slot(uri=ONTOLOGY_ASSOCIATION.funding, name="funding", curie=ONTOLOGY_ASSOCIATION.curie('funding'),
                   model_uri=ONTOLOGY_ASSOCIATION.funding, domain=None, range=Optional[str])

slots.ontology_version = Slot(uri=ONTOLOGY_ASSOCIATION.ontology_version, name="ontology version", curie=ONTOLOGY_ASSOCIATION.curie('ontology_version'),
                   model_uri=ONTOLOGY_ASSOCIATION.ontology_version, domain=None, range=Optional[str])

slots.go_version = Slot(uri=ONTOLOGY_ASSOCIATION.go_version, name="go version", curie=ONTOLOGY_ASSOCIATION.curie('go_version'),
                   model_uri=ONTOLOGY_ASSOCIATION.go_version, domain=None, range=Optional[str])

slots.ro_version = Slot(uri=ONTOLOGY_ASSOCIATION.ro_version, name="ro version", curie=ONTOLOGY_ASSOCIATION.curie('ro_version'),
                   model_uri=ONTOLOGY_ASSOCIATION.ro_version, domain=None, range=Optional[str])

slots.gorel_version = Slot(uri=ONTOLOGY_ASSOCIATION.gorel_version, name="gorel version", curie=ONTOLOGY_ASSOCIATION.curie('gorel_version'),
                   model_uri=ONTOLOGY_ASSOCIATION.gorel_version, domain=None, range=Optional[str])

slots.eco_version = Slot(uri=ONTOLOGY_ASSOCIATION.eco_version, name="eco version", curie=ONTOLOGY_ASSOCIATION.curie('eco_version'),
                   model_uri=ONTOLOGY_ASSOCIATION.eco_version, domain=None, range=Optional[str])

slots.propertyValuePair__property = Slot(uri=ONTOLOGY_ASSOCIATION.property, name="propertyValuePair__property", curie=ONTOLOGY_ASSOCIATION.curie('property'),
                   model_uri=ONTOLOGY_ASSOCIATION.propertyValuePair__property, domain=None, range=Optional[Union[str, ControlledTermId]])

slots.propertyValuePair__value = Slot(uri=ONTOLOGY_ASSOCIATION.value, name="propertyValuePair__value", curie=ONTOLOGY_ASSOCIATION.curie('value'),
                   model_uri=ONTOLOGY_ASSOCIATION.propertyValuePair__value, domain=None, range=Optional[str])

slots.associationDocument__associations = Slot(uri=ONTOLOGY_ASSOCIATION.associations, name="associationDocument__associations", curie=ONTOLOGY_ASSOCIATION.curie('associations'),
                   model_uri=ONTOLOGY_ASSOCIATION.associationDocument__associations, domain=None, range=Optional[Union[Union[dict, Association], List[Union[dict, Association]]]])
