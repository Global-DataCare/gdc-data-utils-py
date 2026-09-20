"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/document-reference-status|4.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/document-reference-status',
 'resolved': True,
 'version': '4.0.1',
 'name': 'DocumentReferenceStatus',
 'title': 'DocumentReferenceStatus',
 'status': 'draft',
 'description': 'The status of the document reference.',
 'immutable': True,
 'compose': {'include': [{'system': 'http://hl7.org/fhir/document-reference-status'}]},
 'usages': [{'resourceType': 'DocumentReference',
             'profile': 'http://hl7.org/fhir/StructureDefinition/DocumentReference|4.0.1',
             'elementId': 'DocumentReference.status',
             'path': 'DocumentReference.status',
             'purpose': 'primary',
             'strength': 'required'}]}
