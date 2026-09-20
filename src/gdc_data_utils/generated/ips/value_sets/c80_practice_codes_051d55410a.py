"""Generated deduplicated IPS ValueSet; do not edit."""

from .chunks.c80_practice_codes_051d55410a_include_0_0 import VALUE_SET_CHUNK as VALUE_SET_CHUNK_0_0
from .chunks.c80_practice_codes_051d55410a_include_0_1 import VALUE_SET_CHUNK as VALUE_SET_CHUNK_0_1

VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/c80-practice-codes',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/c80-practice-codes',
 'resolved': True,
 'version': '4.0.1',
 'name': 'PracticeSettingCodeValueSet',
 'title': 'Practice Setting Code Value Set',
 'status': 'active',
 'description': 'This is the code representing the clinical specialty of the clinician or provider '
                'who interacted with, treated, or provided a service to/for the patient. The value '
                'set used for clinical specialty has been limited by HITSP to the value set '
                'reproduced from HITSP C80 Table 2-149 Clinical Specialty Value Set Definition.',
 'compose': {'include': [{'system': 'http://snomed.info/sct',
                          'concept': [*VALUE_SET_CHUNK_0_0, *VALUE_SET_CHUNK_0_1]}]},
 'usages': [{'resourceType': 'DocumentReference',
             'profile': 'http://hl7.org/fhir/StructureDefinition/DocumentReference|4.0.1',
             'elementId': 'DocumentReference.context.practiceSetting',
             'path': 'DocumentReference.context.practiceSetting',
             'purpose': 'primary',
             'strength': 'example'}]}
