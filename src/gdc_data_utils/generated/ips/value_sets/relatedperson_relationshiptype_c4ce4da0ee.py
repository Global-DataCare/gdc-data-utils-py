"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/relatedperson-relationshiptype',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/relatedperson-relationshiptype',
 'resolved': True,
 'version': '4.0.1',
 'name': 'PatientRelationshipType',
 'title': 'Patient relationship type',
 'status': 'draft',
 'description': 'A set of codes that can be used to indicate the relationship between a Patient '
                'and a Related Person.',
 'compose': {'include': [{'system': 'http://terminology.hl7.org/CodeSystem/v2-0131'},
                         {'system': 'http://terminology.hl7.org/CodeSystem/v3-RoleCode',
                          'filter': [{'property': 'concept',
                                      'op': 'is-a',
                                      'value': '_PersonalRelationshipRoleType'}]}]},
 'usages': [{'resourceType': 'RelatedPerson',
             'profile': 'http://hl7.org/fhir/StructureDefinition/RelatedPerson|4.0.1',
             'elementId': 'RelatedPerson.relationship',
             'path': 'RelatedPerson.relationship',
             'purpose': 'primary',
             'strength': 'preferred'}]}
