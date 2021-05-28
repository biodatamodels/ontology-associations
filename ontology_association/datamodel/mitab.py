# Auto generated from mitab.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-05-27 10:07
# Schema: mitab
#
# id: https://w3id.org/mitab
# description: mitab
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
from linkml.utils.metamodelcore import XSDDateTime
from linkml_model.types import Datetime, String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
MI = CurieNamespace('MI', 'http://purl.obolibrary.org/obo/MI_')
MI2CAST = CurieNamespace('MI2CAST', 'https://github.com/MI2CAST/MI2CAST/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MITAB = CurieNamespace('mitab', 'https://w3id.org/mitab')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = MITAB


# Types
class Identifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "identifier"
    type_model_uri = MITAB.Identifier


class Psi-miIdentifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "psi-mi identifier"
    type_model_uri = MITAB["Psi-miIdentifier"]


class TaxidIdentifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "taxid identifier"
    type_model_uri = MITAB.TaxidIdentifier


class Intact-miscoreIdentifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "intact-miscore identifier"
    type_model_uri = MITAB["Intact-miscoreIdentifier"]


class RogidIdentifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "rogid identifier"
    type_model_uri = MITAB.RogidIdentifier


# Class references



class Interaction(YAMLRoot):
    """
    An interaction between two molecular entities
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MITAB.Interaction
    class_class_curie: ClassVar[str] = "mitab:Interaction"
    class_name: ClassVar[str] = "interaction"
    class_model_uri: ClassVar[URIRef] = MITAB.Interaction


@dataclass
class MitabInteraction(Interaction):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MITAB.MitabInteraction
    class_class_curie: ClassVar[str] = "mitab:MitabInteraction"
    class_name: ClassVar[str] = "mitab interaction"
    class_model_uri: ClassVar[URIRef] = MITAB.MitabInteraction

    ID(s)_interactor_A: Optional[Union[str, Identifier]] = None
    ID(s)_interactor_B: Optional[Union[str, Identifier]] = None
    Alt._ID(s)_interactor_A: Optional[Union[Union[str, Identifier], List[Union[str, Identifier]]]] = empty_list()
    Alt._ID(s)_interactor_B: Optional[Union[str, List[str]]] = empty_list()
    Alias(es)_interactor_A: Optional[Union[Union[str, Identifier], List[Union[str, Identifier]]]] = empty_list()
    Alias(es)_interactor_B: Optional[Union[Union[str, Identifier], List[Union[str, Identifier]]]] = empty_list()
    Interaction_detection_method(s): Optional[Union[str, "InteractionDetectionMethodEnum"]] = None
    Publication_1st_author(s): Optional[str] = None
    Publication_Identifier(s): Optional[Union[Union[str, Identifier], List[Union[str, Identifier]]]] = empty_list()
    Taxid_interactor_A: Optional[Union[Union[str, TaxidIdentifier], List[Union[str, TaxidIdentifier]]]] = empty_list()
    Taxid_interactor_B: Optional[Union[Union[str, TaxidIdentifier], List[Union[str, TaxidIdentifier]]]] = empty_list()
    Interaction_type(s): Optional[Union[str, "InteractionTypeEnum"]] = None
    Source_database(s): Optional[Union[str, Psi-miIdentifier]] = None
    Interaction_identifier(s): Optional[Union[Union[str, Identifier], List[Union[str, Identifier]]]] = empty_list()
    Confidence_value(s): Optional[Union[str, Intact-miscoreIdentifier]] = None
    Expansion_method(s): Optional[Union[str, "ExpansionMethodEnum"]] = None
    Biological_role(s)_interactor_A: Optional[Union[str, "BiologicalRoleInteractorEnum"]] = None
    Biological_role(s)_interactor_B: Optional[Union[str, "BiologicalRoleInteractorEnum"]] = None
    Experimental_role(s)_interactor_A: Optional[Union[str, "ExperimentalRoleInteractorEnum"]] = None
    Experimental_role(s)_interactor_B: Optional[Union[str, "ExperimentalRoleInteractorEnum"]] = None
    Type(s)_interactor_A: Optional[Union[str, Psi-miIdentifier]] = None
    Type(s)_interactor_B: Optional[Union[str, Psi-miIdentifier]] = None
    Xref(s)_interactor_A: Optional[Union[Union[str, Identifier], List[Union[str, Identifier]]]] = empty_list()
    Xref(s)_interactor_B: Optional[Union[Union[str, Identifier], List[Union[str, Identifier]]]] = empty_list()
    Interaction_Xref(s): Optional[Union[Union[str, "InteractionXrefEnum"], List[Union[str, "InteractionXrefEnum"]]]] = empty_list()
    Annotation(s)_interactor_A: Optional[str] = None
    Annotation(s)_interactor_B: Optional[Union[str, List[str]]] = empty_list()
    Interaction_annotation(s): Optional[Union[Union[str, Identifier], List[Union[str, Identifier]]]] = empty_list()
    Host_organism(s): Optional[Union[Union[str, TaxidIdentifier], List[Union[str, TaxidIdentifier]]]] = empty_list()
    Interaction_parameter(s): Optional[str] = None
    Creation_date: Optional[Union[str, XSDDateTime]] = None
    Update_date: Optional[Union[str, XSDDateTime]] = None
    Checksum(s)_interactor_A: Optional[Union[str, RogidIdentifier]] = None
    Checksum(s)_interactor_B: Optional[str] = None
    Interaction_Checksum(s): Optional[Union[Union[str, Identifier], List[Union[str, Identifier]]]] = empty_list()
    Negative: Optional[Union[str, "NegativeEnum"]] = None
    Feature(s)_interactor_A: Optional[Union[str, List[str]]] = empty_list()
    Feature(s)_interactor_B: Optional[Union[str, List[str]]] = empty_list()
    Stoichiometry(s)_interactor_A: Optional[Union[str, "StoichiometryInteractorEnum"]] = None
    Stoichiometry(s)_interactor_B: Optional[Union[str, "StoichiometryInteractorEnum"]] = None
    Identification_method_participant_A: Optional[Union[str, Psi-miIdentifier]] = None
    Identification_method_participant_B: Optional[Union[str, Psi-miIdentifier]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ID(s)_interactor_A is not None and not isinstance(self.ID(s)_interactor_A, Identifier):
            self.ID(s)_interactor_A = Identifier(self.ID(s)_interactor_A)

        if self.ID(s)_interactor_B is not None and not isinstance(self.ID(s)_interactor_B, Identifier):
            self.ID(s)_interactor_B = Identifier(self.ID(s)_interactor_B)

        if self.Alt._ID(s)_interactor_A is None:
            self.Alt._ID(s)_interactor_A = []
        if not isinstance(self.Alt._ID(s)_interactor_A, list):
            self.Alt._ID(s)_interactor_A = [self.Alt._ID(s)_interactor_A]
        self.Alt._ID(s)_interactor_A = [v if isinstance(v, Identifier) else Identifier(v) for v in self.Alt._ID(s)_interactor_A]

        if self.Alt._ID(s)_interactor_B is None:
            self.Alt._ID(s)_interactor_B = []
        if not isinstance(self.Alt._ID(s)_interactor_B, list):
            self.Alt._ID(s)_interactor_B = [self.Alt._ID(s)_interactor_B]
        self.Alt._ID(s)_interactor_B = [v if isinstance(v, str) else str(v) for v in self.Alt._ID(s)_interactor_B]

        if self.Alias(es)_interactor_A is None:
            self.Alias(es)_interactor_A = []
        if not isinstance(self.Alias(es)_interactor_A, list):
            self.Alias(es)_interactor_A = [self.Alias(es)_interactor_A]
        self.Alias(es)_interactor_A = [v if isinstance(v, Identifier) else Identifier(v) for v in self.Alias(es)_interactor_A]

        if self.Alias(es)_interactor_B is None:
            self.Alias(es)_interactor_B = []
        if not isinstance(self.Alias(es)_interactor_B, list):
            self.Alias(es)_interactor_B = [self.Alias(es)_interactor_B]
        self.Alias(es)_interactor_B = [v if isinstance(v, Identifier) else Identifier(v) for v in self.Alias(es)_interactor_B]

        if self.Interaction_detection_method(s) is not None and not isinstance(self.Interaction_detection_method(s), InteractionDetectionMethodEnum):
            self.Interaction_detection_method(s) = InteractionDetectionMethodEnum(self.Interaction_detection_method(s))

        if self.Publication_1st_author(s) is not None and not isinstance(self.Publication_1st_author(s), str):
            self.Publication_1st_author(s) = str(self.Publication_1st_author(s))

        if self.Publication_Identifier(s) is None:
            self.Publication_Identifier(s) = []
        if not isinstance(self.Publication_Identifier(s), list):
            self.Publication_Identifier(s) = [self.Publication_Identifier(s)]
        self.Publication_Identifier(s) = [v if isinstance(v, Identifier) else Identifier(v) for v in self.Publication_Identifier(s)]

        if self.Taxid_interactor_A is None:
            self.Taxid_interactor_A = []
        if not isinstance(self.Taxid_interactor_A, list):
            self.Taxid_interactor_A = [self.Taxid_interactor_A]
        self.Taxid_interactor_A = [v if isinstance(v, TaxidIdentifier) else TaxidIdentifier(v) for v in self.Taxid_interactor_A]

        if self.Taxid_interactor_B is None:
            self.Taxid_interactor_B = []
        if not isinstance(self.Taxid_interactor_B, list):
            self.Taxid_interactor_B = [self.Taxid_interactor_B]
        self.Taxid_interactor_B = [v if isinstance(v, TaxidIdentifier) else TaxidIdentifier(v) for v in self.Taxid_interactor_B]

        if self.Interaction_type(s) is not None and not isinstance(self.Interaction_type(s), InteractionTypeEnum):
            self.Interaction_type(s) = InteractionTypeEnum(self.Interaction_type(s))

        if self.Source_database(s) is not None and not isinstance(self.Source_database(s), Psi-miIdentifier):
            self.Source_database(s) = Psi-miIdentifier(self.Source_database(s))

        if self.Interaction_identifier(s) is None:
            self.Interaction_identifier(s) = []
        if not isinstance(self.Interaction_identifier(s), list):
            self.Interaction_identifier(s) = [self.Interaction_identifier(s)]
        self.Interaction_identifier(s) = [v if isinstance(v, Identifier) else Identifier(v) for v in self.Interaction_identifier(s)]

        if self.Confidence_value(s) is not None and not isinstance(self.Confidence_value(s), Intact-miscoreIdentifier):
            self.Confidence_value(s) = Intact-miscoreIdentifier(self.Confidence_value(s))

        if self.Expansion_method(s) is not None and not isinstance(self.Expansion_method(s), ExpansionMethodEnum):
            self.Expansion_method(s) = ExpansionMethodEnum(self.Expansion_method(s))

        if self.Biological_role(s)_interactor_A is not None and not isinstance(self.Biological_role(s)_interactor_A, BiologicalRoleInteractorEnum):
            self.Biological_role(s)_interactor_A = BiologicalRoleInteractorEnum(self.Biological_role(s)_interactor_A)

        if self.Biological_role(s)_interactor_B is not None and not isinstance(self.Biological_role(s)_interactor_B, BiologicalRoleInteractorEnum):
            self.Biological_role(s)_interactor_B = BiologicalRoleInteractorEnum(self.Biological_role(s)_interactor_B)

        if self.Experimental_role(s)_interactor_A is not None and not isinstance(self.Experimental_role(s)_interactor_A, ExperimentalRoleInteractorEnum):
            self.Experimental_role(s)_interactor_A = ExperimentalRoleInteractorEnum(self.Experimental_role(s)_interactor_A)

        if self.Experimental_role(s)_interactor_B is not None and not isinstance(self.Experimental_role(s)_interactor_B, ExperimentalRoleInteractorEnum):
            self.Experimental_role(s)_interactor_B = ExperimentalRoleInteractorEnum(self.Experimental_role(s)_interactor_B)

        if self.Type(s)_interactor_A is not None and not isinstance(self.Type(s)_interactor_A, Psi-miIdentifier):
            self.Type(s)_interactor_A = Psi-miIdentifier(self.Type(s)_interactor_A)

        if self.Type(s)_interactor_B is not None and not isinstance(self.Type(s)_interactor_B, Psi-miIdentifier):
            self.Type(s)_interactor_B = Psi-miIdentifier(self.Type(s)_interactor_B)

        if self.Xref(s)_interactor_A is None:
            self.Xref(s)_interactor_A = []
        if not isinstance(self.Xref(s)_interactor_A, list):
            self.Xref(s)_interactor_A = [self.Xref(s)_interactor_A]
        self.Xref(s)_interactor_A = [v if isinstance(v, Identifier) else Identifier(v) for v in self.Xref(s)_interactor_A]

        if self.Xref(s)_interactor_B is None:
            self.Xref(s)_interactor_B = []
        if not isinstance(self.Xref(s)_interactor_B, list):
            self.Xref(s)_interactor_B = [self.Xref(s)_interactor_B]
        self.Xref(s)_interactor_B = [v if isinstance(v, Identifier) else Identifier(v) for v in self.Xref(s)_interactor_B]

        if self.Interaction_Xref(s) is None:
            self.Interaction_Xref(s) = []
        if not isinstance(self.Interaction_Xref(s), list):
            self.Interaction_Xref(s) = [self.Interaction_Xref(s)]
        self.Interaction_Xref(s) = [v if isinstance(v, InteractionXrefEnum) else InteractionXrefEnum(v) for v in self.Interaction_Xref(s)]

        if self.Annotation(s)_interactor_A is not None and not isinstance(self.Annotation(s)_interactor_A, str):
            self.Annotation(s)_interactor_A = str(self.Annotation(s)_interactor_A)

        if self.Annotation(s)_interactor_B is None:
            self.Annotation(s)_interactor_B = []
        if not isinstance(self.Annotation(s)_interactor_B, list):
            self.Annotation(s)_interactor_B = [self.Annotation(s)_interactor_B]
        self.Annotation(s)_interactor_B = [v if isinstance(v, str) else str(v) for v in self.Annotation(s)_interactor_B]

        if self.Interaction_annotation(s) is None:
            self.Interaction_annotation(s) = []
        if not isinstance(self.Interaction_annotation(s), list):
            self.Interaction_annotation(s) = [self.Interaction_annotation(s)]
        self.Interaction_annotation(s) = [v if isinstance(v, Identifier) else Identifier(v) for v in self.Interaction_annotation(s)]

        if self.Host_organism(s) is None:
            self.Host_organism(s) = []
        if not isinstance(self.Host_organism(s), list):
            self.Host_organism(s) = [self.Host_organism(s)]
        self.Host_organism(s) = [v if isinstance(v, TaxidIdentifier) else TaxidIdentifier(v) for v in self.Host_organism(s)]

        if self.Interaction_parameter(s) is not None and not isinstance(self.Interaction_parameter(s), str):
            self.Interaction_parameter(s) = str(self.Interaction_parameter(s))

        if self.Creation_date is not None and not isinstance(self.Creation_date, XSDDateTime):
            self.Creation_date = XSDDateTime(self.Creation_date)

        if self.Update_date is not None and not isinstance(self.Update_date, XSDDateTime):
            self.Update_date = XSDDateTime(self.Update_date)

        if self.Checksum(s)_interactor_A is not None and not isinstance(self.Checksum(s)_interactor_A, RogidIdentifier):
            self.Checksum(s)_interactor_A = RogidIdentifier(self.Checksum(s)_interactor_A)

        if self.Checksum(s)_interactor_B is not None and not isinstance(self.Checksum(s)_interactor_B, str):
            self.Checksum(s)_interactor_B = str(self.Checksum(s)_interactor_B)

        if self.Interaction_Checksum(s) is None:
            self.Interaction_Checksum(s) = []
        if not isinstance(self.Interaction_Checksum(s), list):
            self.Interaction_Checksum(s) = [self.Interaction_Checksum(s)]
        self.Interaction_Checksum(s) = [v if isinstance(v, Identifier) else Identifier(v) for v in self.Interaction_Checksum(s)]

        if self.Negative is not None and not isinstance(self.Negative, NegativeEnum):
            self.Negative = NegativeEnum(self.Negative)

        if self.Feature(s)_interactor_A is None:
            self.Feature(s)_interactor_A = []
        if not isinstance(self.Feature(s)_interactor_A, list):
            self.Feature(s)_interactor_A = [self.Feature(s)_interactor_A]
        self.Feature(s)_interactor_A = [v if isinstance(v, str) else str(v) for v in self.Feature(s)_interactor_A]

        if self.Feature(s)_interactor_B is None:
            self.Feature(s)_interactor_B = []
        if not isinstance(self.Feature(s)_interactor_B, list):
            self.Feature(s)_interactor_B = [self.Feature(s)_interactor_B]
        self.Feature(s)_interactor_B = [v if isinstance(v, str) else str(v) for v in self.Feature(s)_interactor_B]

        if self.Stoichiometry(s)_interactor_A is not None and not isinstance(self.Stoichiometry(s)_interactor_A, StoichiometryInteractorEnum):
            self.Stoichiometry(s)_interactor_A = StoichiometryInteractorEnum(self.Stoichiometry(s)_interactor_A)

        if self.Stoichiometry(s)_interactor_B is not None and not isinstance(self.Stoichiometry(s)_interactor_B, StoichiometryInteractorEnum):
            self.Stoichiometry(s)_interactor_B = StoichiometryInteractorEnum(self.Stoichiometry(s)_interactor_B)

        if self.Identification_method_participant_A is not None and not isinstance(self.Identification_method_participant_A, Psi-miIdentifier):
            self.Identification_method_participant_A = Psi-miIdentifier(self.Identification_method_participant_A)

        if self.Identification_method_participant_B is not None and not isinstance(self.Identification_method_participant_B, Psi-miIdentifier):
            self.Identification_method_participant_B = Psi-miIdentifier(self.Identification_method_participant_B)

        super().__post_init__(**kwargs)


@dataclass
class CausaltabInteraction(MitabInteraction):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MITAB.CausaltabInteraction
    class_class_curie: ClassVar[str] = "mitab:CausaltabInteraction"
    class_name: ClassVar[str] = "causaltab interaction"
    class_model_uri: ClassVar[URIRef] = MITAB.CausaltabInteraction

    Biological_Effect_interactor_A: Optional[Union[str, "BiologicalEffectInteractorEnum"]] = None
    Biological_Effect_interactor_B: Optional[Union[str, "BiologicalEffectInteractorEnum"]] = None
    Causal_Regulatory_Mechanism: Optional[Union[str, "CausalRegulatoryMechanismEnum"]] = None
    Causal_statement: Optional[Union[str, Psi-miIdentifier]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.Biological_Effect_interactor_A is not None and not isinstance(self.Biological_Effect_interactor_A, BiologicalEffectInteractorEnum):
            self.Biological_Effect_interactor_A = BiologicalEffectInteractorEnum(self.Biological_Effect_interactor_A)

        if self.Biological_Effect_interactor_B is not None and not isinstance(self.Biological_Effect_interactor_B, BiologicalEffectInteractorEnum):
            self.Biological_Effect_interactor_B = BiologicalEffectInteractorEnum(self.Biological_Effect_interactor_B)

        if self.Causal_Regulatory_Mechanism is not None and not isinstance(self.Causal_Regulatory_Mechanism, CausalRegulatoryMechanismEnum):
            self.Causal_Regulatory_Mechanism = CausalRegulatoryMechanismEnum(self.Causal_Regulatory_Mechanism)

        if self.Causal_statement is not None and not isinstance(self.Causal_statement, Psi-miIdentifier):
            self.Causal_statement = Psi-miIdentifier(self.Causal_statement)

        super().__post_init__(**kwargs)


# Enumerations
class InteractionDetectionMethodEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="InteractionDetectionMethodEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "psi-mi:\"MI:0107\"(surface plasmon resonance)",
                PermissibleValue(text="psi-mi:"MI:0107"(surface plasmon resonance)",
                                 description="surface plasmon resonance",
                                 meaning=MI["0107"]) )
        setattr(cls, "psi-mi:\"MI:0410\"(3D electron microscopy)",
                PermissibleValue(text="psi-mi:"MI:0410"(3D electron microscopy)",
                                 description="3D electron microscopy",
                                 meaning=MI["0410"]) )
        setattr(cls, "psi-mi:\"MI:0096\"(pull down)",
                PermissibleValue(text="psi-mi:"MI:0096"(pull down)",
                                 description="pull down",
                                 meaning=MI["0096"]) )
        setattr(cls, "psi-mi:\"MI:0007\"(anti tag coimmunoprecipitation)",
                PermissibleValue(text="psi-mi:"MI:0007"(anti tag coimmunoprecipitation)",
                                 description="anti tag coimmunoprecipitation",
                                 meaning=MI["0007"]) )
        setattr(cls, "psi-mi:\"MI:0006\"(anti bait coimmunoprecipitation)",
                PermissibleValue(text="psi-mi:"MI:0006"(anti bait coimmunoprecipitation)",
                                 description="anti bait coimmunoprecipitation",
                                 meaning=MI["0006"]) )
        setattr(cls, "psi-mi:\"MI:0424\"(protein kinase assay)",
                PermissibleValue(text="psi-mi:"MI:0424"(protein kinase assay)",
                                 description="psi-mi:"MI:0424"(protein kinase assay)",
                                 meaning=MI["0424"]) )
        setattr(cls, "psi-mi:\"MI:0676\"(tandem affinity purification)",
                PermissibleValue(text="psi-mi:"MI:0676"(tandem affinity purification)",
                                 description="tandem affinity purification",
                                 meaning=MI["0676"]) )
        setattr(cls, "psi-mi:\"MI:0114\"(x-ray crystallography)",
                PermissibleValue(text="psi-mi:"MI:0114"(x-ray crystallography)",
                                 description="x-ray crystallography",
                                 meaning=MI["0114"]) )

class InteractionTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="InteractionTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "psi-mi:\"MI:0915\"(physical association)",
                PermissibleValue(text="psi-mi:"MI:0915"(physical association)",
                                 description="psi-mi:"MI:0915"(physical association)",
                                 meaning=MI["0915"]) )
        setattr(cls, "psi-mi:\"MI:0407\"(direct interaction)",
                PermissibleValue(text="psi-mi:"MI:0407"(direct interaction)",
                                 description="psi-mi:"MI:0407"(direct interaction)",
                                 meaning=MI["0407"]) )
        setattr(cls, "psi-mi:\"MI:0217\"(phosphorylation reaction)",
                PermissibleValue(text="psi-mi:"MI:0217"(phosphorylation reaction)",
                                 description="psi-mi:"MI:0217"(phosphorylation reaction)",
                                 meaning=MI["0217"]) )
        setattr(cls, "psi-mi:\"MI:0914\"(association)",
                PermissibleValue(text="psi-mi:"MI:0914"(association)",
                                 description="psi-mi:"MI:0914"(association)",
                                 meaning=MI["0914"]) )

class ExpansionMethodEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="ExpansionMethodEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "-",
                PermissibleValue(text="-",
                                 description="-") )
        setattr(cls, "psi-mi:\"MI:1060\"(spoke expansion)",
                PermissibleValue(text="psi-mi:"MI:1060"(spoke expansion)",
                                 description="psi-mi:"MI:1060"(spoke expansion)",
                                 meaning=MI["1060"]) )

class BiologicalRoleInteractorEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="BiologicalRoleInteractorEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "psi-mi:\"MI:0499\"(unspecified role)",
                PermissibleValue(text="psi-mi:"MI:0499"(unspecified role)",
                                 description="psi-mi:"MI:0499"(unspecified role)") )
        setattr(cls, "psi-mi:\"MI:0502\"(enzyme target)",
                PermissibleValue(text="psi-mi:"MI:0502"(enzyme target)",
                                 description="psi-mi:"MI:0502"(enzyme target)") )
        setattr(cls, "psi-mi:\"MI:0501\"(enzyme)",
                PermissibleValue(text="psi-mi:"MI:0501"(enzyme)",
                                 description="psi-mi:"MI:0501"(enzyme)") )

class ExperimentalRoleInteractorEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="ExperimentalRoleInteractorEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "psi-mi:\"MI:0498\"(prey)",
                PermissibleValue(text="psi-mi:"MI:0498"(prey)",
                                 description="psi-mi:"MI:0498"(prey)") )
        setattr(cls, "psi-mi:\"MI:0497\"(neutral component)",
                PermissibleValue(text="psi-mi:"MI:0497"(neutral component)",
                                 description="psi-mi:"MI:0497"(neutral component)") )
        setattr(cls, "psi-mi:\"MI:0496\"(bait)",
                PermissibleValue(text="psi-mi:"MI:0496"(bait)",
                                 description="psi-mi:"MI:0496"(bait)") )

class InteractionXrefEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="InteractionXrefEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "-",
                PermissibleValue(text="-",
                                 description="-") )
        setattr(cls, "go:\"GO:0006468\"(protein phosphorylation)",
                PermissibleValue(text="go:"GO:0006468"(protein phosphorylation)",
                                 description="go:"GO:0006468"(protein phosphorylation)") )
        setattr(cls, "psi-mi:\"MI:0465\"(dip)",
                PermissibleValue(text="psi-mi:"MI:0465"(dip)",
                                 description="psi-mi:"MI:0465"(dip)") )
        setattr(cls, "go:\"GO:0004672\"(protein kinase activity)",
                PermissibleValue(text="go:"GO:0004672"(protein kinase activity)",
                                 description="go:"GO:0004672"(protein kinase activity)") )

class NegativeEnum(EnumDefinitionImpl):

    false = PermissibleValue(text="false",
                                 description="false")

    _defn = EnumDefinition(
        name="NegativeEnum",
    )

class StoichiometryInteractorEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="StoichiometryInteractorEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "-",
                PermissibleValue(text="-",
                                 description="-") )
        setattr(cls, "1",
                PermissibleValue(text="1",
                                 description="1") )

class BiologicalEffectInteractorEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="BiologicalEffectInteractorEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "-",
                PermissibleValue(text="-",
                                 description="-") )

class CausalRegulatoryMechanismEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="CausalRegulatoryMechanismEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "psi-mi:\"MI:2246\"(indirect causal regulation)",
                PermissibleValue(text="psi-mi:"MI:2246"(indirect causal regulation)",
                                 description="psi-mi:"MI:2246"(indirect causal regulation)") )
        setattr(cls, "psi-mi:\"MI:2249\"(post transcriptional regulation)",
                PermissibleValue(text="psi-mi:"MI:2249"(post transcriptional regulation)",
                                 description="psi-mi:"MI:2249"(post transcriptional regulation)") )
        setattr(cls, "psi-mi:\"MI:2248\"(translation regulation)",
                PermissibleValue(text="psi-mi:"MI:2248"(translation regulation)",
                                 description="psi-mi:"MI:2248"(translation regulation)") )
        setattr(cls, "-",
                PermissibleValue(text="-",
                                 description="-") )
        setattr(cls, "psi-mi:\"MI:2247\"(transcriptional regulation)",
                PermissibleValue(text="psi-mi:"MI:2247"(transcriptional regulation)",
                                 description="psi-mi:"MI:2247"(transcriptional regulation)") )

# Slots
class slots:
    pass

slots.ID(s)_interactor_A = Slot(uri=MITAB['ID(s)_interactor_A'], name="ID(s) interactor A", curie=MITAB.curie('ID(s)_interactor_A'),
                   model_uri=MITAB['ID(s)_interactor_A'], domain=None, range=Optional[Union[str, Identifier]])

slots.ID(s)_interactor_B = Slot(uri=MITAB['ID(s)_interactor_B'], name="ID(s) interactor B", curie=MITAB.curie('ID(s)_interactor_B'),
                   model_uri=MITAB['ID(s)_interactor_B'], domain=None, range=Optional[Union[str, Identifier]])

slots.Alt._ID(s)_interactor_A = Slot(uri=MITAB['Alt._ID(s)_interactor_A'], name="Alt. ID(s) interactor A", curie=MITAB.curie('Alt._ID(s)_interactor_A'),
                   model_uri=MITAB['Alt._ID(s)_interactor_A'], domain=None, range=Optional[Union[Union[str, Identifier], List[Union[str, Identifier]]]])

slots.Alt._ID(s)_interactor_B = Slot(uri=MITAB['Alt._ID(s)_interactor_B'], name="Alt. ID(s) interactor B", curie=MITAB.curie('Alt._ID(s)_interactor_B'),
                   model_uri=MITAB['Alt._ID(s)_interactor_B'], domain=None, range=Optional[Union[str, List[str]]])

slots.Alias(es)_interactor_A = Slot(uri=MITAB['Alias(es)_interactor_A'], name="Alias(es) interactor A", curie=MITAB.curie('Alias(es)_interactor_A'),
                   model_uri=MITAB['Alias(es)_interactor_A'], domain=None, range=Optional[Union[Union[str, Identifier], List[Union[str, Identifier]]]])

slots.Alias(es)_interactor_B = Slot(uri=MITAB['Alias(es)_interactor_B'], name="Alias(es) interactor B", curie=MITAB.curie('Alias(es)_interactor_B'),
                   model_uri=MITAB['Alias(es)_interactor_B'], domain=None, range=Optional[Union[Union[str, Identifier], List[Union[str, Identifier]]]])

slots.Interaction_detection_method(s) = Slot(uri=MITAB['Interaction_detection_method(s)'], name="Interaction detection method(s)", curie=MITAB.curie('Interaction_detection_method(s)'),
                   model_uri=MITAB['Interaction_detection_method(s)'], domain=None, range=Optional[Union[str, "InteractionDetectionMethodEnum"]])

slots.Publication_1st_author(s) = Slot(uri=MITAB['Publication_1st_author(s)'], name="Publication 1st author(s)", curie=MITAB.curie('Publication_1st_author(s)'),
                   model_uri=MITAB['Publication_1st_author(s)'], domain=None, range=Optional[str])

slots.Publication_Identifier(s) = Slot(uri=MITAB['Publication_Identifier(s)'], name="Publication Identifier(s)", curie=MITAB.curie('Publication_Identifier(s)'),
                   model_uri=MITAB['Publication_Identifier(s)'], domain=None, range=Optional[Union[Union[str, Identifier], List[Union[str, Identifier]]]])

slots.Taxid_interactor_A = Slot(uri=MITAB.Taxid_interactor_A, name="Taxid interactor A", curie=MITAB.curie('Taxid_interactor_A'),
                   model_uri=MITAB.Taxid_interactor_A, domain=None, range=Optional[Union[Union[str, TaxidIdentifier], List[Union[str, TaxidIdentifier]]]])

slots.Taxid_interactor_B = Slot(uri=MITAB.Taxid_interactor_B, name="Taxid interactor B", curie=MITAB.curie('Taxid_interactor_B'),
                   model_uri=MITAB.Taxid_interactor_B, domain=None, range=Optional[Union[Union[str, TaxidIdentifier], List[Union[str, TaxidIdentifier]]]])

slots.Interaction_type(s) = Slot(uri=MITAB['Interaction_type(s)'], name="Interaction type(s)", curie=MITAB.curie('Interaction_type(s)'),
                   model_uri=MITAB['Interaction_type(s)'], domain=None, range=Optional[Union[str, "InteractionTypeEnum"]])

slots.Source_database(s) = Slot(uri=MITAB['Source_database(s)'], name="Source database(s)", curie=MITAB.curie('Source_database(s)'),
                   model_uri=MITAB['Source_database(s)'], domain=None, range=Optional[Union[str, Psi-miIdentifier]])

slots.Interaction_identifier(s) = Slot(uri=MITAB['Interaction_identifier(s)'], name="Interaction identifier(s)", curie=MITAB.curie('Interaction_identifier(s)'),
                   model_uri=MITAB['Interaction_identifier(s)'], domain=None, range=Optional[Union[Union[str, Identifier], List[Union[str, Identifier]]]])

slots.Confidence_value(s) = Slot(uri=MITAB['Confidence_value(s)'], name="Confidence value(s)", curie=MITAB.curie('Confidence_value(s)'),
                   model_uri=MITAB['Confidence_value(s)'], domain=None, range=Optional[Union[str, Intact-miscoreIdentifier]])

slots.Expansion_method(s) = Slot(uri=MITAB['Expansion_method(s)'], name="Expansion method(s)", curie=MITAB.curie('Expansion_method(s)'),
                   model_uri=MITAB['Expansion_method(s)'], domain=None, range=Optional[Union[str, "ExpansionMethodEnum"]])

slots.Biological_role(s)_interactor_A = Slot(uri=MITAB['Biological_role(s)_interactor_A'], name="Biological role(s) interactor A", curie=MITAB.curie('Biological_role(s)_interactor_A'),
                   model_uri=MITAB['Biological_role(s)_interactor_A'], domain=None, range=Optional[Union[str, "BiologicalRoleInteractorEnum"]])

slots.Biological_role(s)_interactor_B = Slot(uri=MITAB['Biological_role(s)_interactor_B'], name="Biological role(s) interactor B", curie=MITAB.curie('Biological_role(s)_interactor_B'),
                   model_uri=MITAB['Biological_role(s)_interactor_B'], domain=None, range=Optional[Union[str, "BiologicalRoleInteractorEnum"]])

slots.Experimental_role(s)_interactor_A = Slot(uri=MITAB['Experimental_role(s)_interactor_A'], name="Experimental role(s) interactor A", curie=MITAB.curie('Experimental_role(s)_interactor_A'),
                   model_uri=MITAB['Experimental_role(s)_interactor_A'], domain=None, range=Optional[Union[str, "ExperimentalRoleInteractorEnum"]])

slots.Experimental_role(s)_interactor_B = Slot(uri=MITAB['Experimental_role(s)_interactor_B'], name="Experimental role(s) interactor B", curie=MITAB.curie('Experimental_role(s)_interactor_B'),
                   model_uri=MITAB['Experimental_role(s)_interactor_B'], domain=None, range=Optional[Union[str, "ExperimentalRoleInteractorEnum"]])

slots.Type(s)_interactor_A = Slot(uri=MITAB['Type(s)_interactor_A'], name="Type(s) interactor A", curie=MITAB.curie('Type(s)_interactor_A'),
                   model_uri=MITAB['Type(s)_interactor_A'], domain=None, range=Optional[Union[str, Psi-miIdentifier]])

slots.Type(s)_interactor_B = Slot(uri=MITAB['Type(s)_interactor_B'], name="Type(s) interactor B", curie=MITAB.curie('Type(s)_interactor_B'),
                   model_uri=MITAB['Type(s)_interactor_B'], domain=None, range=Optional[Union[str, Psi-miIdentifier]])

slots.Xref(s)_interactor_A = Slot(uri=MITAB['Xref(s)_interactor_A'], name="Xref(s) interactor A", curie=MITAB.curie('Xref(s)_interactor_A'),
                   model_uri=MITAB['Xref(s)_interactor_A'], domain=None, range=Optional[Union[Union[str, Identifier], List[Union[str, Identifier]]]])

slots.Xref(s)_interactor_B = Slot(uri=MITAB['Xref(s)_interactor_B'], name="Xref(s) interactor B", curie=MITAB.curie('Xref(s)_interactor_B'),
                   model_uri=MITAB['Xref(s)_interactor_B'], domain=None, range=Optional[Union[Union[str, Identifier], List[Union[str, Identifier]]]])

slots.Interaction_Xref(s) = Slot(uri=MITAB['Interaction_Xref(s)'], name="Interaction Xref(s)", curie=MITAB.curie('Interaction_Xref(s)'),
                   model_uri=MITAB['Interaction_Xref(s)'], domain=None, range=Optional[Union[Union[str, "InteractionXrefEnum"], List[Union[str, "InteractionXrefEnum"]]]])

slots.Annotation(s)_interactor_A = Slot(uri=MITAB['Annotation(s)_interactor_A'], name="Annotation(s) interactor A", curie=MITAB.curie('Annotation(s)_interactor_A'),
                   model_uri=MITAB['Annotation(s)_interactor_A'], domain=None, range=Optional[str])

slots.Annotation(s)_interactor_B = Slot(uri=MITAB['Annotation(s)_interactor_B'], name="Annotation(s) interactor B", curie=MITAB.curie('Annotation(s)_interactor_B'),
                   model_uri=MITAB['Annotation(s)_interactor_B'], domain=None, range=Optional[Union[str, List[str]]])

slots.Interaction_annotation(s) = Slot(uri=MITAB['Interaction_annotation(s)'], name="Interaction annotation(s)", curie=MITAB.curie('Interaction_annotation(s)'),
                   model_uri=MITAB['Interaction_annotation(s)'], domain=None, range=Optional[Union[Union[str, Identifier], List[Union[str, Identifier]]]])

slots.Host_organism(s) = Slot(uri=MITAB['Host_organism(s)'], name="Host organism(s)", curie=MITAB.curie('Host_organism(s)'),
                   model_uri=MITAB['Host_organism(s)'], domain=None, range=Optional[Union[Union[str, TaxidIdentifier], List[Union[str, TaxidIdentifier]]]])

slots.Interaction_parameter(s) = Slot(uri=MITAB['Interaction_parameter(s)'], name="Interaction parameter(s)", curie=MITAB.curie('Interaction_parameter(s)'),
                   model_uri=MITAB['Interaction_parameter(s)'], domain=None, range=Optional[str])

slots.Creation_date = Slot(uri=MITAB.Creation_date, name="Creation date", curie=MITAB.curie('Creation_date'),
                   model_uri=MITAB.Creation_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.Update_date = Slot(uri=MITAB.Update_date, name="Update date", curie=MITAB.curie('Update_date'),
                   model_uri=MITAB.Update_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.Checksum(s)_interactor_A = Slot(uri=MITAB['Checksum(s)_interactor_A'], name="Checksum(s) interactor A", curie=MITAB.curie('Checksum(s)_interactor_A'),
                   model_uri=MITAB['Checksum(s)_interactor_A'], domain=None, range=Optional[Union[str, RogidIdentifier]])

slots.Checksum(s)_interactor_B = Slot(uri=MITAB['Checksum(s)_interactor_B'], name="Checksum(s) interactor B", curie=MITAB.curie('Checksum(s)_interactor_B'),
                   model_uri=MITAB['Checksum(s)_interactor_B'], domain=None, range=Optional[str])

slots.Interaction_Checksum(s) = Slot(uri=MITAB['Interaction_Checksum(s)'], name="Interaction Checksum(s)", curie=MITAB.curie('Interaction_Checksum(s)'),
                   model_uri=MITAB['Interaction_Checksum(s)'], domain=None, range=Optional[Union[Union[str, Identifier], List[Union[str, Identifier]]]])

slots.Negative = Slot(uri=MITAB.Negative, name="Negative", curie=MITAB.curie('Negative'),
                   model_uri=MITAB.Negative, domain=None, range=Optional[Union[str, "NegativeEnum"]])

slots.Feature(s)_interactor_A = Slot(uri=MITAB['Feature(s)_interactor_A'], name="Feature(s) interactor A", curie=MITAB.curie('Feature(s)_interactor_A'),
                   model_uri=MITAB['Feature(s)_interactor_A'], domain=None, range=Optional[Union[str, List[str]]])

slots.Feature(s)_interactor_B = Slot(uri=MITAB['Feature(s)_interactor_B'], name="Feature(s) interactor B", curie=MITAB.curie('Feature(s)_interactor_B'),
                   model_uri=MITAB['Feature(s)_interactor_B'], domain=None, range=Optional[Union[str, List[str]]])

slots.Stoichiometry(s)_interactor_A = Slot(uri=MITAB['Stoichiometry(s)_interactor_A'], name="Stoichiometry(s) interactor A", curie=MITAB.curie('Stoichiometry(s)_interactor_A'),
                   model_uri=MITAB['Stoichiometry(s)_interactor_A'], domain=None, range=Optional[Union[str, "StoichiometryInteractorEnum"]])

slots.Stoichiometry(s)_interactor_B = Slot(uri=MITAB['Stoichiometry(s)_interactor_B'], name="Stoichiometry(s) interactor B", curie=MITAB.curie('Stoichiometry(s)_interactor_B'),
                   model_uri=MITAB['Stoichiometry(s)_interactor_B'], domain=None, range=Optional[Union[str, "StoichiometryInteractorEnum"]])

slots.Identification_method_participant_A = Slot(uri=MITAB.Identification_method_participant_A, name="Identification method participant A", curie=MITAB.curie('Identification_method_participant_A'),
                   model_uri=MITAB.Identification_method_participant_A, domain=None, range=Optional[Union[str, Psi-miIdentifier]])

slots.Identification_method_participant_B = Slot(uri=MITAB.Identification_method_participant_B, name="Identification method participant B", curie=MITAB.curie('Identification_method_participant_B'),
                   model_uri=MITAB.Identification_method_participant_B, domain=None, range=Optional[Union[str, Psi-miIdentifier]])

slots.Biological_Effect_interactor_A = Slot(uri=MITAB.Biological_Effect_interactor_A, name="Biological Effect interactor A", curie=MITAB.curie('Biological_Effect_interactor_A'),
                   model_uri=MITAB.Biological_Effect_interactor_A, domain=None, range=Optional[Union[str, "BiologicalEffectInteractorEnum"]])

slots.Biological_Effect_interactor_B = Slot(uri=MITAB.Biological_Effect_interactor_B, name="Biological Effect interactor B", curie=MITAB.curie('Biological_Effect_interactor_B'),
                   model_uri=MITAB.Biological_Effect_interactor_B, domain=None, range=Optional[Union[str, "BiologicalEffectInteractorEnum"]])

slots.Causal_Regulatory_Mechanism = Slot(uri=MITAB.Causal_Regulatory_Mechanism, name="Causal Regulatory Mechanism", curie=MITAB.curie('Causal_Regulatory_Mechanism'),
                   model_uri=MITAB.Causal_Regulatory_Mechanism, domain=None, range=Optional[Union[str, "CausalRegulatoryMechanismEnum"]])

slots.Causal_statement = Slot(uri=MITAB.Causal_statement, name="Causal statement", curie=MITAB.curie('Causal_statement'),
                   model_uri=MITAB.Causal_statement, domain=None, range=Optional[Union[str, Psi-miIdentifier]])
