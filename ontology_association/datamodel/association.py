# Auto generated from association.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-02-13 18:45
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
from biolinkml.utils.metamodelcore import Bool, XSDDateTime
from includes.types import Boolean, Datetime, String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
GO = CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_')
PR = CurieNamespace('PR', 'http://purl.obolibrary.org/obo/PR_')
SO = CurieNamespace('SO', 'http://purl.obolibrary.org/obo/SO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
ONTOLOGY_ASSOCIATION = CurieNamespace('ontology_association', 'https://w3id.org/ontology_association/')
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
class NamedThingId(Curie):
    pass


class ProviderId(NamedThingId):
    pass


class ControlledTermId(NamedThingId):
    pass


class OntologyClassId(ControlledTermId):
    pass


class TaxonId(OntologyClassId):
    pass


class RelationTermId(ControlledTermId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.NamedThing
    class_class_curie: ClassVar[str] = "ontology_association:NamedThing"
    class_name: ClassVar[str] = "named thing"
    class_model_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.NamedThing

    id: Union[str, NamedThingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Provider(NamedThing):
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
class ControlledTerm(NamedThing):
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

    associations: Optional[Union[Union[dict, Association], List[Union[dict, Association]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.associations is None:
            self.associations = []
        if not isinstance(self.associations, list):
            self.associations = [self.associations]
        self.associations = [v if isinstance(v, Association) else Association(**v) for v in self.associations]

        super().__post_init__(**kwargs)


# Enumerations
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
                   model_uri=ONTOLOGY_ASSOCIATION.db_object_ref, domain=None, range=Union[str, NamedThingId])

slots.aspect = Slot(uri=ONTOLOGY_ASSOCIATION.aspect, name="aspect", curie=ONTOLOGY_ASSOCIATION.curie('aspect'),
                   model_uri=ONTOLOGY_ASSOCIATION.aspect, domain=None, range=str)

slots.db_object_symbol = Slot(uri=ONTOLOGY_ASSOCIATION.db_object_symbol, name="db object symbol", curie=ONTOLOGY_ASSOCIATION.curie('db_object_symbol'),
                   model_uri=ONTOLOGY_ASSOCIATION.db_object_symbol, domain=None, range=Union[str, SymbolType])

slots.db_object_name = Slot(uri=ONTOLOGY_ASSOCIATION.db_object_name, name="db object name", curie=ONTOLOGY_ASSOCIATION.curie('db_object_name'),
                   model_uri=ONTOLOGY_ASSOCIATION.db_object_name, domain=None, range=Optional[Union[str, NameType]])

slots.db_object_synonyms = Slot(uri=ONTOLOGY_ASSOCIATION.db_object_synonyms, name="db object synonyms", curie=ONTOLOGY_ASSOCIATION.curie('db_object_synonyms'),
                   model_uri=ONTOLOGY_ASSOCIATION.db_object_synonyms, domain=None, range=Optional[Union[Union[str, NameType], List[Union[str, NameType]]]])

slots.db_object_type = Slot(uri=ONTOLOGY_ASSOCIATION.db_object_type, name="db object type", curie=ONTOLOGY_ASSOCIATION.curie('db_object_type'),
                   model_uri=ONTOLOGY_ASSOCIATION.db_object_type, domain=None, range=Optional[Union[str, "GpEntityTypeEnum"]])

slots.db_object_taxon = Slot(uri=ONTOLOGY_ASSOCIATION.db_object_taxon, name="db object taxon", curie=ONTOLOGY_ASSOCIATION.curie('db_object_taxon'),
                   model_uri=ONTOLOGY_ASSOCIATION.db_object_taxon, domain=None, range=Union[str, TaxonId])

slots.encoded_by = Slot(uri=ONTOLOGY_ASSOCIATION.encoded_by, name="encoded by", curie=ONTOLOGY_ASSOCIATION.curie('encoded_by'),
                   model_uri=ONTOLOGY_ASSOCIATION.encoded_by, domain=None, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.parent_protein = Slot(uri=ONTOLOGY_ASSOCIATION.parent_protein, name="parent protein", curie=ONTOLOGY_ASSOCIATION.curie('parent_protein'),
                   model_uri=ONTOLOGY_ASSOCIATION.parent_protein, domain=None, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.protein_containing_complex_members = Slot(uri=ONTOLOGY_ASSOCIATION.protein_containing_complex_members, name="protein containing complex members", curie=ONTOLOGY_ASSOCIATION.curie('protein_containing_complex_members'),
                   model_uri=ONTOLOGY_ASSOCIATION.protein_containing_complex_members, domain=None, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.db_xrefs = Slot(uri=ONTOLOGY_ASSOCIATION.db_xrefs, name="db xrefs", curie=ONTOLOGY_ASSOCIATION.curie('db_xrefs'),
                   model_uri=ONTOLOGY_ASSOCIATION.db_xrefs, domain=None, range=Optional[Union[Union[str, Curie], List[Union[str, Curie]]]])

slots.negation = Slot(uri=ONTOLOGY_ASSOCIATION.negation, name="negation", curie=ONTOLOGY_ASSOCIATION.curie('negation'),
                   model_uri=ONTOLOGY_ASSOCIATION.negation, domain=None, range=Optional[Union[bool, Bool]])

slots.ontology_class_ref = Slot(uri=ONTOLOGY_ASSOCIATION.ontology_class_ref, name="ontology class ref", curie=ONTOLOGY_ASSOCIATION.curie('ontology_class_ref'),
                   model_uri=ONTOLOGY_ASSOCIATION.ontology_class_ref, domain=None, range=Union[str, NamedThingId])

slots.relation = Slot(uri=ONTOLOGY_ASSOCIATION.relation, name="relation", curie=ONTOLOGY_ASSOCIATION.curie('relation'),
                   model_uri=ONTOLOGY_ASSOCIATION.relation, domain=None, range=Optional[Union[str, RelationTermId]])

slots.references = Slot(uri=ONTOLOGY_ASSOCIATION.references, name="references", curie=ONTOLOGY_ASSOCIATION.curie('references'),
                   model_uri=ONTOLOGY_ASSOCIATION.references, domain=None, range=Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]])

slots.with_or_from = Slot(uri=ONTOLOGY_ASSOCIATION.with_or_from, name="with or from", curie=ONTOLOGY_ASSOCIATION.curie('with_or_from'),
                   model_uri=ONTOLOGY_ASSOCIATION.with_or_from, domain=None, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

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

slots.annotation_extensions = Slot(uri=ONTOLOGY_ASSOCIATION.annotation_extensions, name="annotation extensions", curie=ONTOLOGY_ASSOCIATION.curie('annotation_extensions'),
                   model_uri=ONTOLOGY_ASSOCIATION.annotation_extensions, domain=None, range=Optional[Union[Union[dict, ConjunctionExtensionExpression], List[Union[dict, ConjunctionExtensionExpression]]]])

slots.annotation_properties = Slot(uri=ONTOLOGY_ASSOCIATION.annotation_properties, name="annotation properties", curie=ONTOLOGY_ASSOCIATION.curie('annotation_properties'),
                   model_uri=ONTOLOGY_ASSOCIATION.annotation_properties, domain=None, range=Optional[Union[Union[dict, PropertyValuePair], List[Union[dict, PropertyValuePair]]]])

slots.gene_product_properties = Slot(uri=ONTOLOGY_ASSOCIATION.gene_product_properties, name="gene product properties", curie=ONTOLOGY_ASSOCIATION.curie('gene_product_properties'),
                   model_uri=ONTOLOGY_ASSOCIATION.gene_product_properties, domain=None, range=Optional[Union[Union[dict, PropertyValuePair], List[Union[dict, PropertyValuePair]]]])

slots.propertyValuePair__property = Slot(uri=ONTOLOGY_ASSOCIATION.property, name="propertyValuePair__property", curie=ONTOLOGY_ASSOCIATION.curie('property'),
                   model_uri=ONTOLOGY_ASSOCIATION.propertyValuePair__property, domain=None, range=Optional[Union[str, ControlledTermId]])

slots.propertyValuePair__value = Slot(uri=ONTOLOGY_ASSOCIATION.value, name="propertyValuePair__value", curie=ONTOLOGY_ASSOCIATION.curie('value'),
                   model_uri=ONTOLOGY_ASSOCIATION.propertyValuePair__value, domain=None, range=Optional[str])

slots.associationDocument__associations = Slot(uri=ONTOLOGY_ASSOCIATION.associations, name="associationDocument__associations", curie=ONTOLOGY_ASSOCIATION.curie('associations'),
                   model_uri=ONTOLOGY_ASSOCIATION.associationDocument__associations, domain=None, range=Optional[Union[Union[dict, Association], List[Union[dict, Association]]]])
