from rest_framework import pagination

__all__ = ["PageNumberPaginationWithPageCounter"]


class PageNumberPaginationWithPageCounter(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        response = super().get_paginated_response(data)
        response.data["total_pages"] = self.page.paginator.num_pages
        return response
