"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/condition-code',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/condition-code',
 'resolved': True,
 'version': '4.0.1',
 'name': 'Condition/Problem/DiagnosisCodes',
 'title': 'Condition/Problem/Diagnosis Codes',
 'status': 'draft',
 'description': 'Example value set for Condition/Problem/Diagnosis codes.',
 'compose': {'include': [{'system': 'http://snomed.info/sct',
                          'filter': [{'property': 'concept', 'op': 'is-a', 'value': '404684003'}]},
                         {'system': 'http://snomed.info/sct',
                          'concept': [{'code': '160245001',
                                       'display': 'No current problems or disability'}]}]},
 'usages': [{'resourceType': 'ClinicalImpression',
             'profile': 'http://hl7.org/fhir/StructureDefinition/ClinicalImpression|4.0.1',
             'elementId': 'ClinicalImpression.finding.itemCodeableConcept',
             'path': 'ClinicalImpression.finding.itemCodeableConcept',
             'purpose': 'primary',
             'strength': 'example'}]}
