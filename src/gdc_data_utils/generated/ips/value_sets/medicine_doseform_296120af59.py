"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/uv/ips/ValueSet/medicine-doseform|2.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/uv/ips/ValueSet/medicine-doseform',
 'resolved': True,
 'version': '2.0.1',
 'name': 'MedicineDoseFormUvIps',
 'title': 'Medicine EDQM Doseform - IPS',
 'status': 'active',
 'description': 'While SNOMED remains a preferred binding for medicine doseform, EDQM (European '
                'Directorate for the Quality of Medicines and Healthcare) doseform codes are '
                'allowed as additional binding. \n'
                '\n'
                'This Value Set includes all the EDQM Standard Terms having:  \n'
                '[Concept Status] = ‘C’\xa0AND  \n'
                "[Concept Class] IN (‘PDF’, ‘CMT’, ‘CDF’, ‘PFT') AND  \n"
                "[Domain] = 'H+V'  \n"
                '\n'
                "C = 'Current'; PDF = 'Pharmaceutical dose form'; CMT = 'Combined terms'; CDF = "
                "'Combined pharmaceutical dose form'; PFT = 'Patient Friendly'; H+V = 'Human and "
                "Veterinary'",
 'immutable': False,
 'compose': {'include': [{'system': 'http://standardterms.edqm.eu',
                          'filter': [{'property': 'status', 'op': '=', 'value': 'C'},
                                     {'property': 'class', 'op': '=', 'value': 'PDF'},
                                     {'property': 'domain', 'op': '=', 'value': 'H+V'}]},
                         {'system': 'http://standardterms.edqm.eu',
                          'filter': [{'property': 'status', 'op': '=', 'value': 'C'},
                                     {'property': 'class', 'op': '=', 'value': 'CMT'},
                                     {'property': 'domain', 'op': '=', 'value': 'H+V'}]},
                         {'system': 'http://standardterms.edqm.eu',
                          'filter': [{'property': 'status', 'op': '=', 'value': 'C'},
                                     {'property': 'class', 'op': '=', 'value': 'CDF'},
                                     {'property': 'domain', 'op': '=', 'value': 'H+V'}]},
                         {'system': 'http://standardterms.edqm.eu',
                          'filter': [{'property': 'status', 'op': '=', 'value': 'C'},
                                     {'property': 'class', 'op': '=', 'value': 'PFT'},
                                     {'property': 'domain', 'op': '=', 'value': 'H+V'}]}]},
 'usages': [{'resourceType': 'Medication',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/Medication-uv-ips|2.0.1',
             'elementId': 'Medication.form',
             'path': 'Medication.form',
             'purpose': 'additional',
             'strength': 'preferred'}]}
