"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/doc-typecodes|4.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/doc-typecodes',
 'resolved': True,
 'version': '4.0.1',
 'name': 'FHIRDocumentTypeCodes',
 'title': 'FHIR Document Type Codes',
 'status': 'draft',
 'description': "FHIR Document Codes - all LOINC codes where scale type = 'DOC'.",
 'compose': {'include': [{'system': 'http://loinc.org',
                          'filter': [{'property': 'SCALE_TYP', 'op': '=', 'value': 'Doc'}]}]},
 'usages': [{'resourceType': 'Composition',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/Composition-uv-ips|2.0.1',
             'elementId': 'Composition.type',
             'path': 'Composition.type',
             'purpose': 'primary',
             'strength': 'preferred'}]}
