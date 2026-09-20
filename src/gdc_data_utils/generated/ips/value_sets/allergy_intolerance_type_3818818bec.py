"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/allergy-intolerance-type|4.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/allergy-intolerance-type',
 'resolved': True,
 'version': '4.0.1',
 'name': 'AllergyIntoleranceType',
 'title': 'AllergyIntoleranceType',
 'status': 'draft',
 'description': 'Identification of the underlying physiological mechanism for a Reaction Risk.',
 'immutable': True,
 'compose': {'include': [{'system': 'http://hl7.org/fhir/allergy-intolerance-type'}]},
 'usages': [{'resourceType': 'AllergyIntolerance',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/AllergyIntolerance-uv-ips|2.0.1',
             'elementId': 'AllergyIntolerance.type',
             'path': 'AllergyIntolerance.type',
             'purpose': 'primary',
             'strength': 'required'}]}
