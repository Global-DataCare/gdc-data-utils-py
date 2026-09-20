"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://terminology.hl7.org/ValueSet/v3-SubstanceAdminSubstitutionReason',
 'canonicalUrl': 'http://terminology.hl7.org/ValueSet/v3-SubstanceAdminSubstitutionReason',
 'resolved': True,
 'version': '2014-03-26',
 'name': 'v3.SubstanceAdminSubstitutionReason',
 'title': 'V3 Value SetSubstanceAdminSubstitutionReason',
 'status': 'active',
 'description': 'No Description Provided',
 'immutable': False,
 'compose': {'include': [{'system': 'http://terminology.hl7.org/CodeSystem/v3-ActReason',
                          'filter': [{'property': 'concept',
                                      'op': 'is-a',
                                      'value': '_SubstanceAdminSubstitutionReason'}]}],
             'exclude': [{'system': 'http://terminology.hl7.org/CodeSystem/v3-ActReason',
                          'concept': [{'code': '_SubstanceAdminSubstitutionReason'}]}]},
 'usages': [{'resourceType': 'MedicationDispense',
             'profile': 'http://hl7.org/fhir/StructureDefinition/MedicationDispense|4.0.1',
             'elementId': 'MedicationDispense.substitution.reason',
             'path': 'MedicationDispense.substitution.reason',
             'purpose': 'primary',
             'strength': 'example'}]}
