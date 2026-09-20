"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/investigation-sets',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/investigation-sets',
 'resolved': True,
 'version': '4.0.1',
 'name': 'InvestigationType',
 'title': 'Investigation Type',
 'status': 'draft',
 'description': 'Example value set for investigation type.',
 'compose': {'include': [{'system': 'http://snomed.info/sct',
                          'concept': [{'code': '271336007', 'display': 'Examination / signs'},
                                      {'code': '160237006', 'display': 'History/symptoms'}]}]},
 'usages': [{'resourceType': 'ClinicalImpression',
             'profile': 'http://hl7.org/fhir/StructureDefinition/ClinicalImpression|4.0.1',
             'elementId': 'ClinicalImpression.investigation.code',
             'path': 'ClinicalImpression.investigation.code',
             'purpose': 'primary',
             'strength': 'example'}]}
