"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/ucum-bodytemp|4.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/ucum-bodytemp',
 'resolved': True,
 'version': '4.0.1',
 'name': 'BodyTemperatureUnits',
 'title': 'Body Temperature Units',
 'status': 'draft',
 'description': 'UCUM units for recording Body Temperature',
 'compose': {'include': [{'system': 'http://unitsofmeasure.org',
                          'concept': [{'code': 'Cel'}, {'code': '[degF]'}]}]},
 'usages': [{'resourceType': 'Observation',
             'profile': 'http://hl7.org/fhir/StructureDefinition/bodytemp|4.0.1',
             'elementId': 'Observation.value[x]:valueQuantity.code',
             'path': 'Observation.value[x].code',
             'purpose': 'primary',
             'strength': 'required'}]}
