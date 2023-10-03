fields_dict = {
    'from': fromField,
    'category': incident_category,
    'incident-title': incident_title,
    'incident_status': incident_status,
    'siem_incident_link': siem_incident_link,
    'destination-ip': destination_ip,
    'source-ip': source_ip,
    'target_hostname': target_hostname,
    'event-severity': event_severity,
    'pravilo': rule_name,
    'rule_description': rule_description,
    'event_raw_1': event_raw_1,
    'event_raw_2': event_raw_2,
    'event_raw_3': event_raw_3,
    'event_raw_4': event_raw_4,
    'event_raw_5': event_raw_5,
    'event_raw_6': event_raw_6,
    'event_raw_7': event_raw_7,
    'event_raw_8': event_raw_8,
    'event_raw_9': event_raw_9,
    'event_raw_10': event_raw_10,
    'raw-events': raw_events,
    'incident_id': incident_id,
    'incident_last_occurrence_time': incident_last_occurrence_time,
    'incident_first_occurrence_time': incident_first_occurrence_time,
    'incident_count': str(incident_count)
}

custom_fields_helper = CustomFieldHelper()

for name, value in fields_dict.items():
    if value is not None:
        custom_fields_helper.add_string(name, value)
custom_fields = custom_fields_helper.build()

print(incident_title)
case = Case(title=incident_title,
            tlp=3,
            flag=False,
            tags=['Test'],
            description=incident_title,
            customFields=custom_fields)
thehiveresponse = api.create_case(case)
