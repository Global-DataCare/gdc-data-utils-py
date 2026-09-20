"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/device-statement-status|4.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/device-statement-status',
 'resolved': True,
 'version': '4.0.1',
 'name': 'DeviceUseStatementStatus',
 'title': 'DeviceUseStatementStatus',
 'status': 'draft',
 'description': 'A coded concept indicating the current status of the Device Usage.',
 'immutable': True,
 'compose': {'include': [{'system': 'http://hl7.org/fhir/device-statement-status'}]},
 'usages': [{'resourceType': 'DeviceUseStatement',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/DeviceUseStatement-uv-ips|2.0.1',
             'elementId': 'DeviceUseStatement.status',
             'path': 'DeviceUseStatement.status',
             'purpose': 'primary',
             'strength': 'required'}]}
