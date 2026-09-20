"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/report-codes|4.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/report-codes',
 'resolved': True,
 'version': '4.0.1',
 'name': 'LOINCDiagnosticReportCodes',
 'title': 'LOINC Diagnostic Report Codes',
 'status': 'draft',
 'description': 'This value set includes LOINC codes that relate to Diagnostic Observations.',
 'compose': {'include': [{'system': 'http://loinc.org'}]},
 'usages': [{'resourceType': 'DiagnosticReport',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/DiagnosticReport-uv-ips|2.0.1',
             'elementId': 'DiagnosticReport.code',
             'path': 'DiagnosticReport.code',
             'purpose': 'primary',
             'strength': 'preferred'}]}
