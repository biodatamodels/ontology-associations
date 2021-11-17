# Auto generated from signor.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-05-27 10:07
# Schema: example
#
# id: https://w3id.org/example
# description: example
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
from linkml_model.types import String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
EXAMPLE = CurieNamespace('example', 'https://w3id.org/example')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = EXAMPLE


# Types
class BTOIdentifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "BTO identifier"
    type_model_uri = EXAMPLE.BTOIdentifier


class Identifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "identifier"
    type_model_uri = EXAMPLE.Identifier


# Class references



@dataclass
class Example(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXAMPLE.Example
    class_class_curie: ClassVar[str] = "example:Example"
    class_name: ClassVar[str] = "example"
    class_model_uri: ClassVar[URIRef] = EXAMPLE.Example

    ENTITYA: Optional[str] = None
    TYPEA: Optional[Union[str, "TYPEAEnum"]] = None
    IDA: Optional[str] = None
    DATABASEA: Optional[Union[str, "DATABASEAEnum"]] = None
    ENTITYB: Optional[str] = None
    TYPEB: Optional[Union[str, "TYPEBEnum"]] = None
    IDB: Optional[str] = None
    DATABASEB: Optional[Union[str, "DATABASEBEnum"]] = None
    EFFECT: Optional[Union[str, "EFFECTEnum"]] = None
    MECHANISM: Optional[Union[str, "MECHANISMEnum"]] = None
    RESIDUE: Optional[str] = None
    SEQUENCE: Optional[str] = None
    TAX_ID: Optional[Union[str, "TAXIDEnum"]] = None
    CELL_DATA: Optional[Union[str, BTOIdentifier]] = None
    TISSUE_DATA: Optional[Union[str, BTOIdentifier]] = None
    MODULATOR_COMPLEX: Optional[Union[str, "MODULATORCOMPLEXEnum"]] = None
    TARGET_COMPLEX: Optional[Union[str, "TARGETCOMPLEXEnum"]] = None
    MODIFICATIONA: Optional[Union[str, Identifier]] = None
    MODASEQ: Optional[Union[str, "MODASEQEnum"]] = None
    MODIFICATIONB: Optional[Union[str, Identifier]] = None
    MODBSEQ: Optional[Union[str, "MODBSEQEnum"]] = None
    PMID: Optional[str] = None
    DIRECT: Optional[Union[str, "DIRECTEnum"]] = None
    NOTES: Optional[str] = None
    ANNOTATOR: Optional[str] = None
    SENTENCE: Optional[Union[str, List[str]]] = empty_list()
    SCORE: Optional[str] = None
    SIGNOR_ID: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ENTITYA is not None and not isinstance(self.ENTITYA, str):
            self.ENTITYA = str(self.ENTITYA)

        if self.TYPEA is not None and not isinstance(self.TYPEA, TYPEAEnum):
            self.TYPEA = TYPEAEnum(self.TYPEA)

        if self.IDA is not None and not isinstance(self.IDA, str):
            self.IDA = str(self.IDA)

        if self.DATABASEA is not None and not isinstance(self.DATABASEA, DATABASEAEnum):
            self.DATABASEA = DATABASEAEnum(self.DATABASEA)

        if self.ENTITYB is not None and not isinstance(self.ENTITYB, str):
            self.ENTITYB = str(self.ENTITYB)

        if self.TYPEB is not None and not isinstance(self.TYPEB, TYPEBEnum):
            self.TYPEB = TYPEBEnum(self.TYPEB)

        if self.IDB is not None and not isinstance(self.IDB, str):
            self.IDB = str(self.IDB)

        if self.DATABASEB is not None and not isinstance(self.DATABASEB, DATABASEBEnum):
            self.DATABASEB = DATABASEBEnum(self.DATABASEB)

        if self.EFFECT is not None and not isinstance(self.EFFECT, EFFECTEnum):
            self.EFFECT = EFFECTEnum(self.EFFECT)

        if self.MECHANISM is not None and not isinstance(self.MECHANISM, MECHANISMEnum):
            self.MECHANISM = MECHANISMEnum(self.MECHANISM)

        if self.RESIDUE is not None and not isinstance(self.RESIDUE, str):
            self.RESIDUE = str(self.RESIDUE)

        if self.SEQUENCE is not None and not isinstance(self.SEQUENCE, str):
            self.SEQUENCE = str(self.SEQUENCE)

        if self.TAX_ID is not None and not isinstance(self.TAX_ID, TAXIDEnum):
            self.TAX_ID = TAXIDEnum(self.TAX_ID)

        if self.CELL_DATA is not None and not isinstance(self.CELL_DATA, BTOIdentifier):
            self.CELL_DATA = BTOIdentifier(self.CELL_DATA)

        if self.TISSUE_DATA is not None and not isinstance(self.TISSUE_DATA, BTOIdentifier):
            self.TISSUE_DATA = BTOIdentifier(self.TISSUE_DATA)

        if self.MODULATOR_COMPLEX is not None and not isinstance(self.MODULATOR_COMPLEX, MODULATORCOMPLEXEnum):
            self.MODULATOR_COMPLEX = MODULATORCOMPLEXEnum(self.MODULATOR_COMPLEX)

        if self.TARGET_COMPLEX is not None and not isinstance(self.TARGET_COMPLEX, TARGETCOMPLEXEnum):
            self.TARGET_COMPLEX = TARGETCOMPLEXEnum(self.TARGET_COMPLEX)

        if self.MODIFICATIONA is not None and not isinstance(self.MODIFICATIONA, Identifier):
            self.MODIFICATIONA = Identifier(self.MODIFICATIONA)

        if self.MODASEQ is not None and not isinstance(self.MODASEQ, MODASEQEnum):
            self.MODASEQ = MODASEQEnum(self.MODASEQ)

        if self.MODIFICATIONB is not None and not isinstance(self.MODIFICATIONB, Identifier):
            self.MODIFICATIONB = Identifier(self.MODIFICATIONB)

        if self.MODBSEQ is not None and not isinstance(self.MODBSEQ, MODBSEQEnum):
            self.MODBSEQ = MODBSEQEnum(self.MODBSEQ)

        if self.PMID is not None and not isinstance(self.PMID, str):
            self.PMID = str(self.PMID)

        if self.DIRECT is not None and not isinstance(self.DIRECT, DIRECTEnum):
            self.DIRECT = DIRECTEnum(self.DIRECT)

        if self.NOTES is not None and not isinstance(self.NOTES, str):
            self.NOTES = str(self.NOTES)

        if self.ANNOTATOR is not None and not isinstance(self.ANNOTATOR, str):
            self.ANNOTATOR = str(self.ANNOTATOR)

        if self.SENTENCE is None:
            self.SENTENCE = []
        if not isinstance(self.SENTENCE, list):
            self.SENTENCE = [self.SENTENCE]
        self.SENTENCE = [v if isinstance(v, str) else str(v) for v in self.SENTENCE]

        if self.SCORE is not None and not isinstance(self.SCORE, str):
            self.SCORE = str(self.SCORE)

        if self.SIGNOR_ID is not None and not isinstance(self.SIGNOR_ID, str):
            self.SIGNOR_ID = str(self.SIGNOR_ID)

        super().__post_init__(**kwargs)


# Enumerations
class TYPEAEnum(EnumDefinitionImpl):

    antibody = PermissibleValue(text="antibody",
                                       description="antibody")
    stimulus = PermissibleValue(text="stimulus",
                                       description="stimulus")
    complex = PermissibleValue(text="complex",
                                     description="complex")
    phenotype = PermissibleValue(text="phenotype",
                                         description="phenotype")
    protein = PermissibleValue(text="protein",
                                     description="protein")
    chemical = PermissibleValue(text="chemical",
                                       description="chemical")
    mirna = PermissibleValue(text="mirna",
                                 description="mirna")
    proteinfamily = PermissibleValue(text="proteinfamily",
                                                 description="proteinfamily")
    smallmolecule = PermissibleValue(text="smallmolecule",
                                                 description="smallmolecule")

    _defn = EnumDefinition(
        name="TYPEAEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "fusion protein",
                PermissibleValue(text="fusion protein",
                                 description="fusion protein") )

class DATABASEAEnum(EnumDefinitionImpl):

    SIGNOR = PermissibleValue(text="SIGNOR",
                                   description="SIGNOR")
    DRUGBANK = PermissibleValue(text="DRUGBANK",
                                       description="DRUGBANK")
    miRBase = PermissibleValue(text="miRBase",
                                     description="miRBase")
    UNIPROT = PermissibleValue(text="UNIPROT",
                                     description="UNIPROT")
    PUBCHEM = PermissibleValue(text="PUBCHEM",
                                     description="PUBCHEM")
    ChEBI = PermissibleValue(text="ChEBI",
                                 description="ChEBI")

    _defn = EnumDefinition(
        name="DATABASEAEnum",
    )

class TYPEBEnum(EnumDefinitionImpl):

    stimulus = PermissibleValue(text="stimulus",
                                       description="stimulus")
    complex = PermissibleValue(text="complex",
                                     description="complex")
    phenotype = PermissibleValue(text="phenotype",
                                         description="phenotype")
    protein = PermissibleValue(text="protein",
                                     description="protein")
    chemical = PermissibleValue(text="chemical",
                                       description="chemical")
    mirna = PermissibleValue(text="mirna",
                                 description="mirna")
    proteinfamily = PermissibleValue(text="proteinfamily",
                                                 description="proteinfamily")
    smallmolecule = PermissibleValue(text="smallmolecule",
                                                 description="smallmolecule")

    _defn = EnumDefinition(
        name="TYPEBEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "fusion protein",
                PermissibleValue(text="fusion protein",
                                 description="fusion protein") )

class DATABASEBEnum(EnumDefinitionImpl):

    SIGNOR = PermissibleValue(text="SIGNOR",
                                   description="SIGNOR")
    miRBase = PermissibleValue(text="miRBase",
                                     description="miRBase")
    UNIPROT = PermissibleValue(text="UNIPROT",
                                     description="UNIPROT")
    PUBCHEM = PermissibleValue(text="PUBCHEM",
                                     description="PUBCHEM")
    ChEBI = PermissibleValue(text="ChEBI",
                                 description="ChEBI")

    _defn = EnumDefinition(
        name="DATABASEBEnum",
    )

class EFFECTEnum(EnumDefinitionImpl):

    unknown = PermissibleValue(text="unknown",
                                     description="unknown")

    _defn = EnumDefinition(
        name="EFFECTEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "up-regulates activity",
                PermissibleValue(text="up-regulates activity",
                                 description="up-regulates activity") )
        setattr(cls, "up-regulates quantity",
                PermissibleValue(text="up-regulates quantity",
                                 description="up-regulates quantity") )
        setattr(cls, "down-regulates",
                PermissibleValue(text="down-regulates",
                                 description="down-regulates") )
        setattr(cls, "down-regulates quantity by repression",
                PermissibleValue(text="down-regulates quantity by repression",
                                 description="down-regulates quantity by repression") )
        setattr(cls, "up-regulates quantity by stabilization",
                PermissibleValue(text="up-regulates quantity by stabilization",
                                 description="up-regulates quantity by stabilization") )
        setattr(cls, "down-regulates quantity",
                PermissibleValue(text="down-regulates quantity",
                                 description="down-regulates quantity") )
        setattr(cls, "down-regulates quantity by destabilization",
                PermissibleValue(text="down-regulates quantity by destabilization",
                                 description="down-regulates quantity by destabilization") )
        setattr(cls, "up-regulates quantity by expression",
                PermissibleValue(text="up-regulates quantity by expression",
                                 description="up-regulates quantity by expression") )
        setattr(cls, "up-regulates",
                PermissibleValue(text="up-regulates",
                                 description="up-regulates") )
        setattr(cls, "form complex",
                PermissibleValue(text="form complex",
                                 description="form complex") )
        setattr(cls, "down-regulates activity",
                PermissibleValue(text="down-regulates activity",
                                 description="down-regulates activity") )

class MECHANISMEnum(EnumDefinitionImpl):

    deubiquitination = PermissibleValue(text="deubiquitination",
                                                       description="deubiquitination")
    acetylation = PermissibleValue(text="acetylation",
                                             description="acetylation")
    neddylation = PermissibleValue(text="neddylation",
                                             description="neddylation")
    glycosylation = PermissibleValue(text="glycosylation",
                                                 description="glycosylation")
    binding = PermissibleValue(text="binding",
                                     description="binding")
    relocalization = PermissibleValue(text="relocalization",
                                                   description="relocalization")
    cleavage = PermissibleValue(text="cleavage",
                                       description="cleavage")
    isomerization = PermissibleValue(text="isomerization",
                                                 description="isomerization")
    methylation = PermissibleValue(text="methylation",
                                             description="methylation")
    oxidation = PermissibleValue(text="oxidation",
                                         description="oxidation")
    ubiquitination = PermissibleValue(text="ubiquitination",
                                                   description="ubiquitination")
    dephosphorylation = PermissibleValue(text="dephosphorylation",
                                                         description="dephosphorylation")
    phosphorylation = PermissibleValue(text="phosphorylation",
                                                     description="phosphorylation")
    deacetylation = PermissibleValue(text="deacetylation",
                                                 description="deacetylation")
    demethylation = PermissibleValue(text="demethylation",
                                                 description="demethylation")
    sumoylation = PermissibleValue(text="sumoylation",
                                             description="sumoylation")
    lipidation = PermissibleValue(text="lipidation",
                                           description="lipidation")
    desumoylation = PermissibleValue(text="desumoylation",
                                                 description="desumoylation")
    tyrosination = PermissibleValue(text="tyrosination",
                                               description="tyrosination")
    palmitoylation = PermissibleValue(text="palmitoylation",
                                                   description="palmitoylation")
    hydroxylation = PermissibleValue(text="hydroxylation",
                                                 description="hydroxylation")

    _defn = EnumDefinition(
        name="MECHANISMEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "chemical inhibition",
                PermissibleValue(text="chemical inhibition",
                                 description="chemical inhibition") )
        setattr(cls, "guanine nucleotide exchange factor",
                PermissibleValue(text="guanine nucleotide exchange factor",
                                 description="guanine nucleotide exchange factor") )
        setattr(cls, "catalytic activity",
                PermissibleValue(text="catalytic activity",
                                 description="catalytic activity") )
        setattr(cls, "gtpase-activating protein",
                PermissibleValue(text="gtpase-activating protein",
                                 description="gtpase-activating protein") )
        setattr(cls, "transcriptional regulation",
                PermissibleValue(text="transcriptional regulation",
                                 description="transcriptional regulation") )
        setattr(cls, "post translational modification",
                PermissibleValue(text="post translational modification",
                                 description="post translational modification") )
        setattr(cls, "post transcriptional regulation",
                PermissibleValue(text="post transcriptional regulation",
                                 description="post transcriptional regulation") )
        setattr(cls, "small molecule catalysis",
                PermissibleValue(text="small molecule catalysis",
                                 description="small molecule catalysis") )
        setattr(cls, "s-nitrosylation",
                PermissibleValue(text="s-nitrosylation",
                                 description="s-nitrosylation") )
        setattr(cls, "ADP-ribosylation",
                PermissibleValue(text="ADP-ribosylation",
                                 description="ADP-ribosylation") )
        setattr(cls, "chemical activation",
                PermissibleValue(text="chemical activation",
                                 description="chemical activation") )
        setattr(cls, "translation regulation",
                PermissibleValue(text="translation regulation",
                                 description="translation regulation") )

class TAXIDEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="TAXIDEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "10030",
                PermissibleValue(text="10030",
                                 description="10030") )
        setattr(cls, "9543",
                PermissibleValue(text="9543",
                                 description="9543") )
        setattr(cls, "8355",
                PermissibleValue(text="8355",
                                 description="8355") )
        setattr(cls, "10090",
                PermissibleValue(text="10090",
                                 description="10090") )
        setattr(cls, "9600",
                PermissibleValue(text="9600",
                                 description="9600") )
        setattr(cls, "9615",
                PermissibleValue(text="9615",
                                 description="9615") )
        setattr(cls, "7227",
                PermissibleValue(text="7227",
                                 description="7227") )
        setattr(cls, "9031",
                PermissibleValue(text="9031",
                                 description="9031") )
        setattr(cls, "6239",
                PermissibleValue(text="6239",
                                 description="6239") )
        setattr(cls, "9606",
                PermissibleValue(text="9606",
                                 description="9606") )
        setattr(cls, "9825",
                PermissibleValue(text="9825",
                                 description="9825") )
        setattr(cls, "99606",
                PermissibleValue(text="99606",
                                 description="99606") )
        setattr(cls, "93934",
                PermissibleValue(text="93934",
                                 description="93934") )
        setattr(cls, "10036",
                PermissibleValue(text="10036",
                                 description="10036") )
        setattr(cls, "9913",
                PermissibleValue(text="9913",
                                 description="9913") )
        setattr(cls, "4932",
                PermissibleValue(text="4932",
                                 description="4932") )
        setattr(cls, "960",
                PermissibleValue(text="960",
                                 description="960") )
        setattr(cls, "-1",
                PermissibleValue(text="-1",
                                 description="-1") )
        setattr(cls, "452646",
                PermissibleValue(text="452646",
                                 description="452646") )
        setattr(cls, "10029",
                PermissibleValue(text="10029",
                                 description="10029") )
        setattr(cls, "9006",
                PermissibleValue(text="9006",
                                 description="9006") )
        setattr(cls, "9935",
                PermissibleValue(text="9935",
                                 description="9935") )
        setattr(cls, "9608",
                PermissibleValue(text="9608",
                                 description="9608") )
        setattr(cls, "1792",
                PermissibleValue(text="1792",
                                 description="1792") )
        setattr(cls, "9823",
                PermissibleValue(text="9823",
                                 description="9823") )
        setattr(cls, "10116",
                PermissibleValue(text="10116",
                                 description="10116") )
        setattr(cls, "9609",
                PermissibleValue(text="9609",
                                 description="9609") )
        setattr(cls, "9534",
                PermissibleValue(text="9534",
                                 description="9534") )
        setattr(cls, "9060",
                PermissibleValue(text="9060",
                                 description="9060") )

class MODULATORCOMPLEXEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="MODULATORCOMPLEXEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "SIGNOR-C301",
                PermissibleValue(text="SIGNOR-C301",
                                 description="SIGNOR-C301") )
        setattr(cls, "SIGNOR-C3",
                PermissibleValue(text="SIGNOR-C3",
                                 description="SIGNOR-C3") )
        setattr(cls, "SIGNOR-C8",
                PermissibleValue(text="SIGNOR-C8",
                                 description="SIGNOR-C8") )
        setattr(cls, "SIGNOR-C16",
                PermissibleValue(text="SIGNOR-C16",
                                 description="SIGNOR-C16") )
        setattr(cls, "SIGNOR-C135",
                PermissibleValue(text="SIGNOR-C135",
                                 description="SIGNOR-C135") )
        setattr(cls, "SIGNOR-C306",
                PermissibleValue(text="SIGNOR-C306",
                                 description="SIGNOR-C306") )
        setattr(cls, "SIGNOR-C7",
                PermissibleValue(text="SIGNOR-C7",
                                 description="SIGNOR-C7") )
        setattr(cls, "SIGNOR-C14",
                PermissibleValue(text="SIGNOR-C14",
                                 description="SIGNOR-C14") )
        setattr(cls, "SIGNOR-C303",
                PermissibleValue(text="SIGNOR-C303",
                                 description="SIGNOR-C303") )
        setattr(cls, "SIGNOR-C85",
                PermissibleValue(text="SIGNOR-C85",
                                 description="SIGNOR-C85") )
        setattr(cls, "SIGNOR-C17",
                PermissibleValue(text="SIGNOR-C17",
                                 description="SIGNOR-C17") )
        setattr(cls, "SIGNOR-C305",
                PermissibleValue(text="SIGNOR-C305",
                                 description="SIGNOR-C305") )
        setattr(cls, "SIGNOR-C297",
                PermissibleValue(text="SIGNOR-C297",
                                 description="SIGNOR-C297") )
        setattr(cls, "SIGNOR-C29",
                PermissibleValue(text="SIGNOR-C29",
                                 description="SIGNOR-C29") )
        setattr(cls, "SIGNOR-C298",
                PermissibleValue(text="SIGNOR-C298",
                                 description="SIGNOR-C298") )
        setattr(cls, "SIGNOR-C60",
                PermissibleValue(text="SIGNOR-C60",
                                 description="SIGNOR-C60") )
        setattr(cls, "SIGNOR-C5",
                PermissibleValue(text="SIGNOR-C5",
                                 description="SIGNOR-C5") )
        setattr(cls, "SIGNOR-C21",
                PermissibleValue(text="SIGNOR-C21",
                                 description="SIGNOR-C21") )
        setattr(cls, "SIGNOR-C54",
                PermissibleValue(text="SIGNOR-C54",
                                 description="SIGNOR-C54") )
        setattr(cls, "SIGNOR-C13",
                PermissibleValue(text="SIGNOR-C13",
                                 description="SIGNOR-C13") )
        setattr(cls, "SIGNOR-C15",
                PermissibleValue(text="SIGNOR-C15",
                                 description="SIGNOR-C15") )
        setattr(cls, "SIGNOR-C300",
                PermissibleValue(text="SIGNOR-C300",
                                 description="SIGNOR-C300") )
        setattr(cls, "SIGNOR-C136",
                PermissibleValue(text="SIGNOR-C136",
                                 description="SIGNOR-C136") )
        setattr(cls, "SIGNOR-C110",
                PermissibleValue(text="SIGNOR-C110",
                                 description="SIGNOR-C110") )
        setattr(cls, "SIGNOR-C6",
                PermissibleValue(text="SIGNOR-C6",
                                 description="SIGNOR-C6") )
        setattr(cls, "SIGNOR-C2",
                PermissibleValue(text="SIGNOR-C2",
                                 description="SIGNOR-C2") )
        setattr(cls, "SIGNOR-C18",
                PermissibleValue(text="SIGNOR-C18",
                                 description="SIGNOR-C18") )
        setattr(cls, "SIGNOR-C319",
                PermissibleValue(text="SIGNOR-C319",
                                 description="SIGNOR-C319") )
        setattr(cls, "SIGNOR-C83",
                PermissibleValue(text="SIGNOR-C83",
                                 description="SIGNOR-C83") )

class TARGETCOMPLEXEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="TARGETCOMPLEXEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "SIGNOR-C3",
                PermissibleValue(text="SIGNOR-C3",
                                 description="SIGNOR-C3") )
        setattr(cls, "SIGNOR-C106",
                PermissibleValue(text="SIGNOR-C106",
                                 description="SIGNOR-C106") )
        setattr(cls, "SIGNOR-C8",
                PermissibleValue(text="SIGNOR-C8",
                                 description="SIGNOR-C8") )
        setattr(cls, "SIGNOR-C89",
                PermissibleValue(text="SIGNOR-C89",
                                 description="SIGNOR-C89") )
        setattr(cls, "SIGNOR-C16",
                PermissibleValue(text="SIGNOR-C16",
                                 description="SIGNOR-C16") )
        setattr(cls, "SIGNOR-C129",
                PermissibleValue(text="SIGNOR-C129",
                                 description="SIGNOR-C129") )
        setattr(cls, "SIGNOR-C306",
                PermissibleValue(text="SIGNOR-C306",
                                 description="SIGNOR-C306") )
        setattr(cls, "SIGNOR-C7",
                PermissibleValue(text="SIGNOR-C7",
                                 description="SIGNOR-C7") )
        setattr(cls, "SIGNOR-C14",
                PermissibleValue(text="SIGNOR-C14",
                                 description="SIGNOR-C14") )
        setattr(cls, "SIGNOR-C302",
                PermissibleValue(text="SIGNOR-C302",
                                 description="SIGNOR-C302") )
        setattr(cls, "SIGNOR-C50",
                PermissibleValue(text="SIGNOR-C50",
                                 description="SIGNOR-C50") )
        setattr(cls, "SIGNOR-C85",
                PermissibleValue(text="SIGNOR-C85",
                                 description="SIGNOR-C85") )
        setattr(cls, "SIGNOR-C17",
                PermissibleValue(text="SIGNOR-C17",
                                 description="SIGNOR-C17") )
        setattr(cls, "SIGNOR-C305",
                PermissibleValue(text="SIGNOR-C305",
                                 description="SIGNOR-C305") )
        setattr(cls, "SIGNOR-C29",
                PermissibleValue(text="SIGNOR-C29",
                                 description="SIGNOR-C29") )
        setattr(cls, "SIGNOR-C242",
                PermissibleValue(text="SIGNOR-C242",
                                 description="SIGNOR-C242") )
        setattr(cls, "SIGNOR-C295",
                PermissibleValue(text="SIGNOR-C295",
                                 description="SIGNOR-C295") )
        setattr(cls, "SIGNOR-C9",
                PermissibleValue(text="SIGNOR-C9",
                                 description="SIGNOR-C9") )
        setattr(cls, "SIGNOR-C98",
                PermissibleValue(text="SIGNOR-C98",
                                 description="SIGNOR-C98") )
        setattr(cls, "SIGNOR-C21",
                PermissibleValue(text="SIGNOR-C21",
                                 description="SIGNOR-C21") )
        setattr(cls, "SIGNOR-C308",
                PermissibleValue(text="SIGNOR-C308",
                                 description="SIGNOR-C308") )
        setattr(cls, "SIGNOR-C263",
                PermissibleValue(text="SIGNOR-C263",
                                 description="SIGNOR-C263") )
        setattr(cls, "SIGNOR-C30",
                PermissibleValue(text="SIGNOR-C30",
                                 description="SIGNOR-C30") )
        setattr(cls, "SIGNOR-C92",
                PermissibleValue(text="SIGNOR-C92",
                                 description="SIGNOR-C92") )
        setattr(cls, "SIGNOR-C123",
                PermissibleValue(text="SIGNOR-C123",
                                 description="SIGNOR-C123") )
        setattr(cls, "SIGNOR-C77",
                PermissibleValue(text="SIGNOR-C77",
                                 description="SIGNOR-C77") )
        setattr(cls, "SIGNOR-C13",
                PermissibleValue(text="SIGNOR-C13",
                                 description="SIGNOR-C13") )
        setattr(cls, "SIGNOR-C15",
                PermissibleValue(text="SIGNOR-C15",
                                 description="SIGNOR-C15") )
        setattr(cls, "SIGNOR-C110",
                PermissibleValue(text="SIGNOR-C110",
                                 description="SIGNOR-C110") )
        setattr(cls, "SIGNOR-C6",
                PermissibleValue(text="SIGNOR-C6",
                                 description="SIGNOR-C6") )
        setattr(cls, "SIGNOR-C154",
                PermissibleValue(text="SIGNOR-C154",
                                 description="SIGNOR-C154") )
        setattr(cls, "SIGNOR-C2",
                PermissibleValue(text="SIGNOR-C2",
                                 description="SIGNOR-C2") )
        setattr(cls, "SIGNOR-C88",
                PermissibleValue(text="SIGNOR-C88",
                                 description="SIGNOR-C88") )
        setattr(cls, "SIGNOR-C68",
                PermissibleValue(text="SIGNOR-C68",
                                 description="SIGNOR-C68") )
        setattr(cls, "SIGNOR-C12",
                PermissibleValue(text="SIGNOR-C12",
                                 description="SIGNOR-C12") )
        setattr(cls, "SIGNOR-C18",
                PermissibleValue(text="SIGNOR-C18",
                                 description="SIGNOR-C18") )
        setattr(cls, "SIGNOR-C125",
                PermissibleValue(text="SIGNOR-C125",
                                 description="SIGNOR-C125") )
        setattr(cls, "SIGNOR-C128",
                PermissibleValue(text="SIGNOR-C128",
                                 description="SIGNOR-C128") )
        setattr(cls, "SIGNOR-C167",
                PermissibleValue(text="SIGNOR-C167",
                                 description="SIGNOR-C167") )
        setattr(cls, "SIGNOR-C127",
                PermissibleValue(text="SIGNOR-C127",
                                 description="SIGNOR-C127") )

class MODASEQEnum(EnumDefinitionImpl):

    GGAKRHRkVLRDNIQ = PermissibleValue(text="GGAKRHRkVLRDNIQ",
                                                     description="GGAKRHRkVLRDNIQ")
    SGRPRTTsFAESCKP = PermissibleValue(text="SGRPRTTsFAESCKP",
                                                     description="SGRPRTTsFAESCKP")
    GPGEQQKrKIVLDPS = PermissibleValue(text="GPGEQQKrKIVLDPS",
                                                     description="GPGEQQKrKIVLDPS")
    VDFREYEyDLKWEFP = PermissibleValue(text="VDFREYEyDLKWEFP",
                                                     description="VDFREYEyDLKWEFP")
    KDRDGYEsSYRRRTL = PermissibleValue(text="KDRDGYEsSYRRRTL",
                                                     description="KDRDGYEsSYRRRTL")
    KGQKYFDsGDYNMAK = PermissibleValue(text="KGQKYFDsGDYNMAK",
                                                     description="KGQKYFDsGDYNMAK")
    ELPTRVSsPVFGATS = PermissibleValue(text="ELPTRVSsPVFGATS",
                                                     description="ELPTRVSsPVFGATS")
    LPTPTKMtPRSRILV = PermissibleValue(text="LPTPTKMtPRSRILV",
                                                     description="LPTPTKMtPRSRILV")
    SFDERQPyAHMNGGR = PermissibleValue(text="SFDERQPyAHMNGGR",
                                                     description="SFDERQPyAHMNGGR")
    SAAQLAStPFHKLPV = PermissibleValue(text="SAAQLAStPFHKLPV",
                                                     description="SAAQLAStPFHKLPV")
    SDSPREQdSESQTLD = PermissibleValue(text="SDSPREQdSESQTLD",
                                                     description="SDSPREQdSESQTLD")
    IFGATDYtSSIDVWS = PermissibleValue(text="IFGATDYtSSIDVWS",
                                                     description="IFGATDYtSSIDVWS")
    EENMTETdAFYKREM = PermissibleValue(text="EENMTETdAFYKREM",
                                                     description="EENMTETdAFYKREM")
    ASHLGLArSNLDEDI = PermissibleValue(text="ASHLGLArSNLDEDI",
                                                     description="ASHLGLArSNLDEDI")
    IHGSESMdSGISLDN = PermissibleValue(text="IHGSESMdSGISLDN",
                                                     description="IHGSESMdSGISLDN")
    SPGCEESdAGKEKLP = PermissibleValue(text="SPGCEESdAGKEKLP",
                                                     description="SPGCEESdAGKEKLP")
    SGPINDTdANPRYKI = PermissibleValue(text="SGPINDTdANPRYKI",
                                                     description="SGPINDTdANPRYKI")
    CTTKTSTrIVGGTNS = PermissibleValue(text="CTTKTSTrIVGGTNS",
                                                     description="CTTKTSTrIVGGTNS")
    HKDMQLGrLHMKTLL = PermissibleValue(text="HKDMQLGrLHMKTLL",
                                                     description="HKDMQLGrLHMKTLL")
    TRKLMEFsEHCAIIL = PermissibleValue(text="TRKLMEFsEHCAIIL",
                                                     description="TRKLMEFsEHCAIIL")
    KTKESLGrKIQIQRS = PermissibleValue(text="KTKESLGrKIQIQRS",
                                                     description="KTKESLGrKIQIQRS")
    DTNITEVdAASVYTL = PermissibleValue(text="DTNITEVdAASVYTL",
                                                     description="DTNITEVdAASVYTL")
    SESTNHIySNLANCS = PermissibleValue(text="SESTNHIySNLANCS",
                                                     description="SESTNHIySNLANCS")
    MLEERKTyVNTTLYE = PermissibleValue(text="MLEERKTyVNTTLYE",
                                                     description="MLEERKTyVNTTLYE")
    KSKGRASsSGNQESS = PermissibleValue(text="KSKGRASsSGNQESS",
                                                     description="KSKGRASsSGNQESS")
    CLHNFLTdGVPAEGA = PermissibleValue(text="CLHNFLTdGVPAEGA",
                                                     description="CLHNFLTdGVPAEGA")
    PAPQAVQdNPAMPTS = PermissibleValue(text="PAPQAVQdNPAMPTS",
                                                     description="PAPQAVQdNPAMPTS")
    VAKVDDPkLANSEFL = PermissibleValue(text="VAKVDDPkLANSEFL",
                                                     description="VAKVDDPkLANSEFL")
    DHAEAALyKNLLHSK = PermissibleValue(text="DHAEAALyKNLLHSK",
                                                     description="DHAEAALyKNLLHSK")
    AQQDGKDyIVLPISE = PermissibleValue(text="AQQDGKDyIVLPISE",
                                                     description="AQQDGKDyIVLPISE")

    _defn = EnumDefinition(
        name="MODASEQEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "T-->L",
                PermissibleValue(text="T-->L",
                                 description="T-->L") )
        setattr(cls, "KGQAGLQrALEILQE;TPLQLFEgRRNRRRR",
                PermissibleValue(text="KGQAGLQrALEILQE;TPLQLFEgRRNRRRR",
                                 description="KGQAGLQrALEILQE;TPLQLFEgRRNRRRR") )
        setattr(cls, "SPSVRCSsMS;SVRCSSMs",
                PermissibleValue(text="SPSVRCSsMS;SVRCSSMs",
                                 description="SPSVRCSsMS;SVRCSSMs") )
        setattr(cls, "NMMDILTtPSMAKPR;PRQDYSRtPGQVLSL",
                PermissibleValue(text="NMMDILTtPSMAKPR;PRQDYSRtPGQVLSL",
                                 description="NMMDILTtPSMAKPR;PRQDYSRtPGQVLSL") )
        setattr(cls, "GGAKRHRkVLRDNIQ;GLGKGGAkRHRKVLR",
                PermissibleValue(text="GGAKRHRkVLRDNIQ;GLGKGGAkRHRKVLR",
                                 description="GGAKRHRkVLRDNIQ;GLGKGGAkRHRKVLR") )
        setattr(cls, "DDYHNPGyLVVLPDS;SMESIDDyVNVPESG",
                PermissibleValue(text="DDYHNPGyLVVLPDS;SMESIDDyVNVPESG",
                                 description="DDYHNPGyLVVLPDS;SMESIDDyVNVPESG") )
        setattr(cls, "EEEGAPDyENLQELN;SLDGSREyVNVSQEL",
                PermissibleValue(text="EEEGAPDyENLQELN;SLDGSREyVNVSQEL",
                                 description="EEEGAPDyENLQELN;SLDGSREyVNVSQEL") )
        setattr(cls, "HKDMQLGrLHMKTLL;KEILRPRrTLQKKIE",
                PermissibleValue(text="HKDMQLGrLHMKTLL;KEILRPRrTLQKKIE",
                                 description="HKDMQLGrLHMKTLL;KEILRPRrTLQKKIE") )
        setattr(cls, "QPAARRRrSVQLTEK;ASHLGLArSNLDEDI",
                PermissibleValue(text="QPAARRRrSVQLTEK;ASHLGLArSNLDEDI",
                                 description="QPAARRRrSVQLTEK;ASHLGLArSNLDEDI") )
        setattr(cls, "kGGKGLGK;SGRGKGGkGLGKGGA",
                PermissibleValue(text="kGGKGLGK;SGRGKGGkGLGKGGA",
                                 description="kGGKGLGK;SGRGKGGkGLGKGGA") )
        setattr(cls, "GMISLMKrPPGFSPF;PPGFSPFrSSRIGEI",
                PermissibleValue(text="GMISLMKrPPGFSPF;PPGFSPFrSSRIGEI",
                                 description="GMISLMKrPPGFSPF;PPGFSPFrSSRIGEI") )

class MODBSEQEnum(EnumDefinitionImpl):

    TYVDPHTyEDPNQAV = PermissibleValue(text="TYVDPHTyEDPNQAV",
                                                     description="TYVDPHTyEDPNQAV")
    KVSSTHYyLLPERPP = PermissibleValue(text="KVSSTHYyLLPERPP",
                                                     description="KVSSTHYyLLPERPP")
    QPLSKSSsSPELQTL = PermissibleValue(text="QPLSKSSsSPELQTL",
                                                     description="QPLSKSSsSPELQTL")
    GETRFTDtRKDEQER = PermissibleValue(text="GETRFTDtRKDEQER",
                                                     description="GETRFTDtRKDEQER")
    PQHVRAHsSPASLQL = PermissibleValue(text="PQHVRAHsSPASLQL",
                                                     description="PQHVRAHsSPASLQL")
    RAGETRFtDTRKDEQ = PermissibleValue(text="RAGETRFtDTRKDEQ",
                                                     description="RAGETRFtDTRKDEQ")
    FTSTEPQyQPGENL = PermissibleValue(text="FTSTEPQyQPGENL",
                                                   description="FTSTEPQyQPGENL")
    TSVYESPySDPEELK = PermissibleValue(text="TSVYESPySDPEELK",
                                                     description="TSVYESPySDPEELK")
    EANSRCQtPIKMKPN = PermissibleValue(text="EANSRCQtPIKMKPN",
                                                     description="EANSRCQtPIKMKPN")
    SVSETDDyAEIIDEE = PermissibleValue(text="SVSETDDyAEIIDEE",
                                                     description="SVSETDDyAEIIDEE")
    HIIENPQyFSDACVH = PermissibleValue(text="HIIENPQyFSDACVH",
                                                     description="HIIENPQyFSDACVH")
    ASHLGLArSNLDEDI = PermissibleValue(text="ASHLGLArSNLDEDI",
                                                     description="ASHLGLArSNLDEDI")
    PSHDRSRtVSASSTG = PermissibleValue(text="PSHDRSRtVSASSTG",
                                                     description="PSHDRSRtVSASSTG")
    PPPGSLEyLCLPAGG = PermissibleValue(text="PPPGSLEyLCLPAGG",
                                                     description="PPPGSLEyLCLPAGG")
    RPHFPQFsYSASGTA = PermissibleValue(text="RPHFPQFsYSASGTA",
                                                     description="RPHFPQFsYSASGTA")
    LLPTPPLsPSRRSGL = PermissibleValue(text="LLPTPPLsPSRRSGL",
                                                     description="LLPTPPLsPSRRSGL")
    HDHTGFLtEYVATRW = PermissibleValue(text="HDHTGFLtEYVATRW",
                                                     description="HDHTGFLtEYVATRW")
    ANLRKLNsRLFVIRG = PermissibleValue(text="ANLRKLNsRLFVIRG",
                                                     description="ANLRKLNsRLFVIRG")

    _defn = EnumDefinition(
        name="MODBSEQEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "sAEVIHQV;VQGAGTSyRNVLQAA",
                PermissibleValue(text="sAEVIHQV;VQGAGTSyRNVLQAA",
                                 description="sAEVIHQV;VQGAGTSyRNVLQAA") )
        setattr(cls, "PSSDSLSsPTLLAL;AAAHRKGsSSNEPSS",
                PermissibleValue(text="PSSDSLSsPTLLAL;AAAHRKGsSSNEPSS",
                                 description="PSSDSLSsPTLLAL;AAAHRKGsSSNEPSS") )
        setattr(cls, "GFPSKTDsPSCEYSR;GSLCSVFsPSFVQWE;GADSDVEtPSNFGKY",
                PermissibleValue(text="GFPSKTDsPSCEYSR;GSLCSVFsPSFVQWE;GADSDVEtPSNFGKY",
                                 description="GFPSKTDsPSCEYSR;GSLCSVFsPSFVQWE;GADSDVEtPSNFGKY") )
        setattr(cls, "ESENSGDsGYPSEKR;SGDSGYPsEKRGELD",
                PermissibleValue(text="ESENSGDsGYPSEKR;SGDSGYPsEKRGELD",
                                 description="ESENSGDsGYPSEKR;SGDSGYPsEKRGELD") )
        setattr(cls, "T-->E",
                PermissibleValue(text="T-->E",
                                 description="T-->E") )

class DIRECTEnum(EnumDefinitionImpl):

    NO = PermissibleValue(text="NO",
                           description="NO")
    UNK = PermissibleValue(text="UNK",
                             description="UNK")
    YES = PermissibleValue(text="YES",
                             description="YES")

    _defn = EnumDefinition(
        name="DIRECTEnum",
    )

# Slots
class slots:
    pass

slots.ENTITYA = Slot(uri=EXAMPLE.ENTITYA, name="ENTITYA", curie=EXAMPLE.curie('ENTITYA'),
                   model_uri=EXAMPLE.ENTITYA, domain=None, range=Optional[str])

slots.TYPEA = Slot(uri=EXAMPLE.TYPEA, name="TYPEA", curie=EXAMPLE.curie('TYPEA'),
                   model_uri=EXAMPLE.TYPEA, domain=None, range=Optional[Union[str, "TYPEAEnum"]])

slots.IDA = Slot(uri=EXAMPLE.IDA, name="IDA", curie=EXAMPLE.curie('IDA'),
                   model_uri=EXAMPLE.IDA, domain=None, range=Optional[str])

slots.DATABASEA = Slot(uri=EXAMPLE.DATABASEA, name="DATABASEA", curie=EXAMPLE.curie('DATABASEA'),
                   model_uri=EXAMPLE.DATABASEA, domain=None, range=Optional[Union[str, "DATABASEAEnum"]])

slots.ENTITYB = Slot(uri=EXAMPLE.ENTITYB, name="ENTITYB", curie=EXAMPLE.curie('ENTITYB'),
                   model_uri=EXAMPLE.ENTITYB, domain=None, range=Optional[str])

slots.TYPEB = Slot(uri=EXAMPLE.TYPEB, name="TYPEB", curie=EXAMPLE.curie('TYPEB'),
                   model_uri=EXAMPLE.TYPEB, domain=None, range=Optional[Union[str, "TYPEBEnum"]])

slots.IDB = Slot(uri=EXAMPLE.IDB, name="IDB", curie=EXAMPLE.curie('IDB'),
                   model_uri=EXAMPLE.IDB, domain=None, range=Optional[str])

slots.DATABASEB = Slot(uri=EXAMPLE.DATABASEB, name="DATABASEB", curie=EXAMPLE.curie('DATABASEB'),
                   model_uri=EXAMPLE.DATABASEB, domain=None, range=Optional[Union[str, "DATABASEBEnum"]])

slots.EFFECT = Slot(uri=EXAMPLE.EFFECT, name="EFFECT", curie=EXAMPLE.curie('EFFECT'),
                   model_uri=EXAMPLE.EFFECT, domain=None, range=Optional[Union[str, "EFFECTEnum"]])

slots.MECHANISM = Slot(uri=EXAMPLE.MECHANISM, name="MECHANISM", curie=EXAMPLE.curie('MECHANISM'),
                   model_uri=EXAMPLE.MECHANISM, domain=None, range=Optional[Union[str, "MECHANISMEnum"]])

slots.RESIDUE = Slot(uri=EXAMPLE.RESIDUE, name="RESIDUE", curie=EXAMPLE.curie('RESIDUE'),
                   model_uri=EXAMPLE.RESIDUE, domain=None, range=Optional[str])

slots.SEQUENCE = Slot(uri=EXAMPLE.SEQUENCE, name="SEQUENCE", curie=EXAMPLE.curie('SEQUENCE'),
                   model_uri=EXAMPLE.SEQUENCE, domain=None, range=Optional[str])

slots.TAX_ID = Slot(uri=EXAMPLE.TAX_ID, name="TAX_ID", curie=EXAMPLE.curie('TAX_ID'),
                   model_uri=EXAMPLE.TAX_ID, domain=None, range=Optional[Union[str, "TAXIDEnum"]])

slots.CELL_DATA = Slot(uri=EXAMPLE.CELL_DATA, name="CELL_DATA", curie=EXAMPLE.curie('CELL_DATA'),
                   model_uri=EXAMPLE.CELL_DATA, domain=None, range=Optional[Union[str, BTOIdentifier]])

slots.TISSUE_DATA = Slot(uri=EXAMPLE.TISSUE_DATA, name="TISSUE_DATA", curie=EXAMPLE.curie('TISSUE_DATA'),
                   model_uri=EXAMPLE.TISSUE_DATA, domain=None, range=Optional[Union[str, BTOIdentifier]])

slots.MODULATOR_COMPLEX = Slot(uri=EXAMPLE.MODULATOR_COMPLEX, name="MODULATOR_COMPLEX", curie=EXAMPLE.curie('MODULATOR_COMPLEX'),
                   model_uri=EXAMPLE.MODULATOR_COMPLEX, domain=None, range=Optional[Union[str, "MODULATORCOMPLEXEnum"]])

slots.TARGET_COMPLEX = Slot(uri=EXAMPLE.TARGET_COMPLEX, name="TARGET_COMPLEX", curie=EXAMPLE.curie('TARGET_COMPLEX'),
                   model_uri=EXAMPLE.TARGET_COMPLEX, domain=None, range=Optional[Union[str, "TARGETCOMPLEXEnum"]])

slots.MODIFICATIONA = Slot(uri=EXAMPLE.MODIFICATIONA, name="MODIFICATIONA", curie=EXAMPLE.curie('MODIFICATIONA'),
                   model_uri=EXAMPLE.MODIFICATIONA, domain=None, range=Optional[Union[str, Identifier]])

slots.MODASEQ = Slot(uri=EXAMPLE.MODASEQ, name="MODASEQ", curie=EXAMPLE.curie('MODASEQ'),
                   model_uri=EXAMPLE.MODASEQ, domain=None, range=Optional[Union[str, "MODASEQEnum"]])

slots.MODIFICATIONB = Slot(uri=EXAMPLE.MODIFICATIONB, name="MODIFICATIONB", curie=EXAMPLE.curie('MODIFICATIONB'),
                   model_uri=EXAMPLE.MODIFICATIONB, domain=None, range=Optional[Union[str, Identifier]])

slots.MODBSEQ = Slot(uri=EXAMPLE.MODBSEQ, name="MODBSEQ", curie=EXAMPLE.curie('MODBSEQ'),
                   model_uri=EXAMPLE.MODBSEQ, domain=None, range=Optional[Union[str, "MODBSEQEnum"]])

slots.PMID = Slot(uri=EXAMPLE.PMID, name="PMID", curie=EXAMPLE.curie('PMID'),
                   model_uri=EXAMPLE.PMID, domain=None, range=Optional[str])

slots.DIRECT = Slot(uri=EXAMPLE.DIRECT, name="DIRECT", curie=EXAMPLE.curie('DIRECT'),
                   model_uri=EXAMPLE.DIRECT, domain=None, range=Optional[Union[str, "DIRECTEnum"]])

slots.NOTES = Slot(uri=EXAMPLE.NOTES, name="NOTES", curie=EXAMPLE.curie('NOTES'),
                   model_uri=EXAMPLE.NOTES, domain=None, range=Optional[str])

slots.ANNOTATOR = Slot(uri=EXAMPLE.ANNOTATOR, name="ANNOTATOR", curie=EXAMPLE.curie('ANNOTATOR'),
                   model_uri=EXAMPLE.ANNOTATOR, domain=None, range=Optional[str])

slots.SENTENCE = Slot(uri=EXAMPLE.SENTENCE, name="SENTENCE", curie=EXAMPLE.curie('SENTENCE'),
                   model_uri=EXAMPLE.SENTENCE, domain=None, range=Optional[Union[str, List[str]]])

slots.SCORE = Slot(uri=EXAMPLE.SCORE, name="SCORE", curie=EXAMPLE.curie('SCORE'),
                   model_uri=EXAMPLE.SCORE, domain=None, range=Optional[str])

slots.SIGNOR_ID = Slot(uri=EXAMPLE.SIGNOR_ID, name="SIGNOR_ID", curie=EXAMPLE.curie('SIGNOR_ID'),
                   model_uri=EXAMPLE.SIGNOR_ID, domain=None, range=Optional[str])
