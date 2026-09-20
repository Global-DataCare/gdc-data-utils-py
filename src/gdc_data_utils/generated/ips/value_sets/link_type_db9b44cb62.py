"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/link-type|4.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/link-type',
 'resolved': True,
 'version': '4.0.1',
 'name': 'LinkType',
 'title': 'LinkType',
 'status': 'active',
 'description': 'The type of link between this patient resource and another patient resource.',
 'immutable': True,
 'compose': {'include': [{'system': 'http://hl7.org/fhir/link-type'}]},
 'usages': [{'resourceType': 'Patient',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/Patient-uv-ips|2.0.1',
             'elementId': 'Patient.link.type',
             'path': 'Patient.link.type',
             'purpose': 'primary',
             'strength': 'required'}]}
