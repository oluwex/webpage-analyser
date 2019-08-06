from rest_framework.serializers import (
    IntegerField, CharField, Serializer, URLField
)


class TableSerializer(Serializer):
    index = IntegerField(read_only=True)
    number_of_rows = IntegerField(read_only=True)
    table_head = CharField(read_only=True)


class AnalysisSerializer(Serializer):
    number_of_tables = IntegerField(read_only=True)
    result_summary = TableSerializer(many=True, read_only=True)


class SearchSerializer(Serializer):
    url = URLField(write_only=True)