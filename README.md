Есть вот такая конструкция в запросе по АПИ на питоне. Как бы вы сделали так, чтобы поля CustomFields генерировались динамически? Скажем, если нет значения - не добавлялись в инцидент.

```
custom_fields = CustomFieldHelper() \
        .add_string('from', fromField) \
        .add_string('category', incident_category) \
        .add_string('incident-title', incident_title) \
        .add_string('incident_status', incident_status)\
        .add_string('siem_incident_link', siem_incident_link)\
        .add_string('destination-ip', destination_ip) \
        .add_string('source-ip', source_ip) \
        .add_string('target_hostname', target_hostname)\
        .add_string('event-severity', event_severity) \
        .add_string('pravilo', rule_name) \
        .add_string('rule_description', rule_description) \
        .add_string('event_raw_1', event_raw_1) \
        .add_string('event_raw_2', event_raw_2) \
        .add_string('event_raw_3', event_raw_3) \
        .add_string('event_raw_4', event_raw_4) \
        .add_string('event_raw_5', event_raw_5) \
        .add_string('event_raw_6', event_raw_6) \
        .add_string('event_raw_7', event_raw_7) \
        .add_string('event_raw_8', event_raw_8) \
        .add_string('event_raw_9', event_raw_9) \
        .add_string('event_raw_10', event_raw_10) \
        .add_string('raw-events', raw_events) \
        .add_string('incident_id', incident_id) \
        .add_string('incident_last_occurrence_time', incident_last_occurrence_time) \
        .add_string('incident_first_occurrence_time', incident_first_occurrence_time) \
        .add_string('incident_count', str(incident_count)) \
        .build()
    print(incident_title)
    case = Case(title=incident_title,
                tlp=3,
                flag=False,
                tags=['Test'],
                description=incident_title,
                customFields=custom_fields)
    thehiveresponse = api.create_case(case)
```

Подробнее о АПИ можно посмотреть здесь -  https://thehive-project.github.io/TheHive4py/reference/api/
