"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/procedure-reason|4.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/procedure-reason',
 'resolved': True,
 'version': '4.0.1',
 'name': 'ProcedureReasonCodes',
 'title': 'Procedure Reason Codes',
 'status': 'draft',
 'description': 'This example value set defines the set of codes that can be used to indicate a '
                'reason for a procedure.',
 'compose': {'include': [{'system': 'http://snomed.info/sct',
                          'filter': [{'property': 'concept', 'op': 'is-a', 'value': '404684003'}]},
                         {'system': 'http://snomed.info/sct',
                          'filter': [{'property': 'concept', 'op': 'is-a', 'value': '71388002'}]}]},
 'usages': [{'resourceType': 'ImagingStudy',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/ImagingStudy-uv-ips|2.0.1',
             'elementId': 'ImagingStudy.reasonCode',
             'path': 'ImagingStudy.reasonCode',
             'purpose': 'primary',
             'strength': 'example'}]}
