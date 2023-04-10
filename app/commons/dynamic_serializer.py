from django.utils.functional import cached_property
from rest_framework.serializers import ModelSerializer


class DynamicFieldsModelSerializer(ModelSerializer):
    """
    see: https://www.django-rest-framework.org/api-guide/serializers/#example
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        # request = kwargs.get('context', {}).get('request')
        # requested_fields = request.GET.get('data', '') if request else None
        # requested_fields = \
        #     requested_fields.split(',') if requested_fields else None
        fields = kwargs.pop('fields', None)
        exclude_fields = kwargs.pop('exclude_fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
        
        if exclude_fields is not None:
            excluded = set(exclude_fields)
            existing = set(self.fields)
            for field_name in existing & excluded:
                self.fields.pop(field_name)

    @cached_property
    def request(self):
        return self.context.get("request", None)
