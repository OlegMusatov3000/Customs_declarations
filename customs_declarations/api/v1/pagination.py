from rest_framework import pagination


class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return pagination.Response({
            'result': data
        })
