"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/allergyintolerance-clinical|4.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/allergyintolerance-clinical',
 'resolved': True,
 'version': '4.0.1',
 'name': 'AllergyIntoleranceClinicalStatusCodes',
 'title': 'AllergyIntolerance Clinical Status Codes',
 'status': 'draft',
 'description': 'Preferred value set for AllergyIntolerance Clinical Status.',
 'immutable': True,
 'compose': {'include': [{'system': 'http://terminology.hl7.org/CodeSystem/allergyintolerance-clinical'}]},
 'usages': [{'resourceType': 'AllergyIntolerance',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/AllergyIntolerance-uv-ips|2.0.1',
             'elementId': 'AllergyIntolerance.clinicalStatus',
             'path': 'AllergyIntolerance.clinicalStatus',
             'purpose': 'primary',
             'strength': 'required'}]}
