"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/procedure-code',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/procedure-code',
 'resolved': True,
 'version': '4.0.1',
 'name': 'ProcedureCodes(SNOMEDCT)',
 'title': 'Procedure Codes (SNOMED CT)',
 'status': 'draft',
 'description': 'Procedure Code: All SNOMED CT procedure codes.',
 'compose': {'include': [{'system': 'http://snomed.info/sct',
                          'filter': [{'property': 'concept', 'op': 'is-a', 'value': '71388002'}]}]},
 'usages': [{'resourceType': 'CarePlan',
             'profile': 'http://hl7.org/fhir/StructureDefinition/CarePlan|4.0.1',
             'elementId': 'CarePlan.activity.detail.code',
             'path': 'CarePlan.activity.detail.code',
             'purpose': 'primary',
             'strength': 'example'}]}
