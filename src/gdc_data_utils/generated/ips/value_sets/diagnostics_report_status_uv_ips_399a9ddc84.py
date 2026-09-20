"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/uv/ips/ValueSet/diagnostics-report-status-uv-ips|2.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/uv/ips/ValueSet/diagnostics-report-status-uv-ips',
 'resolved': True,
 'version': '2.0.1',
 'name': 'DiagnosticReportStatusUvIps',
 'title': 'Diagnostics Report Status Codes - IPS',
 'status': 'active',
 'description': 'IPS Diagnostic Report status codes allowable for diagnostics reports.  This value '
                'set includes all status codes except \\"entered-in-error\\" from '
                'http://hl7.org/fhir/diagnostic-report-status.',
 'immutable': False,
 'compose': {'include': [{'system': 'http://hl7.org/fhir/diagnostic-report-status',
                          'version': '4.0.1'}],
             'exclude': [{'system': 'http://hl7.org/fhir/diagnostic-report-status',
                          'version': '4.0.1',
                          'filter': [{'property': 'concept',
                                      'op': 'is-a',
                                      'value': 'entered-in-error'}]}]},
 'usages': [{'resourceType': 'DiagnosticReport',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/DiagnosticReport-uv-ips|2.0.1',
             'elementId': 'DiagnosticReport.status',
             'path': 'DiagnosticReport.status',
             'purpose': 'primary',
             'strength': 'required'}]}
