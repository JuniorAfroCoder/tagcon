# mixins.py
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAdminUser
from django.http import HttpResponse
from rest_framework.response import Response
import csv
import pandas as pd
from rest_framework import status


class ExportMixin:
    export_fields = [] 
    export_filename = "exported_data"

    def get_export_queryset(self):
        return self.filter_queryset(self.get_queryset()).values(*self.export_fields)

    @action(detail=False, methods=['get'], url_path='export/csv')
    @permission_classes([IsAdminUser])
    def export_csv(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{self.export_filename}.csv"'

        writer = csv.writer(response)
        writer.writerow(self.export_fields)

        for obj in self.get_export_queryset():
            writer.writerow([obj.get(field, '') for field in self.export_fields])

        return response

    @action(detail=False, methods=['get'], url_path='export/excel')
    @permission_classes([IsAdminUser])
    def export_excel(self, request):
        queryset = list(self.get_export_queryset())
        df = pd.DataFrame(queryset)
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename="{self.export_filename}.xlsx"'
        df.to_excel(response, index=False)
        return response

class SimplePostResponseMixin:
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"status": "ok"}, status=status.HTTP_200_OK)
