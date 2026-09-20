"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/clinicalimpression-prognosis',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/clinicalimpression-prognosis',
 'resolved': True,
 'version': '4.0.1',
 'name': 'ClinicalImpressionPrognosis',
 'title': 'Clinical Impression Prognosis',
 'status': 'draft',
 'description': 'Example value set for clinical impression prognosis.',
 'compose': {'include': [{'system': 'http://snomed.info/sct',
                          'filter': [{'property': 'concept',
                                      'op': 'is-a',
                                      'value': '365858006'}]}]},
 'usages': [{'resourceType': 'ClinicalImpression',
             'profile': 'http://hl7.org/fhir/StructureDefinition/ClinicalImpression|4.0.1',
             'elementId': 'ClinicalImpression.prognosisCodeableConcept',
             'path': 'ClinicalImpression.prognosisCodeableConcept',
             'purpose': 'primary',
             'strength': 'example'}]}
