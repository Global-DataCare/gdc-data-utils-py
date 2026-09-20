"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/condition-clinical|4.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/condition-clinical',
 'resolved': True,
 'version': '4.0.1',
 'name': 'ConditionClinicalStatusCodes',
 'title': 'Condition Clinical Status Codes',
 'status': 'draft',
 'description': 'Preferred value set for Condition Clinical Status.',
 'immutable': True,
 'compose': {'include': [{'system': 'http://terminology.hl7.org/CodeSystem/condition-clinical'}]},
 'usages': [{'resourceType': 'Condition',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/Condition-uv-ips|2.0.1',
             'elementId': 'Condition.clinicalStatus',
             'path': 'Condition.clinicalStatus',
             'purpose': 'primary',
             'strength': 'required'}]}
