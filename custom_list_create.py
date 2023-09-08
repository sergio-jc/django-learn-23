from rest_framework import generics

class CustomListCreateAPIView(generics.ListCreateAPIView):
    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            print("queryset BEFORE filters", queryset)
            queryset = backend().filter_queryset(self.request, queryset, self)
            print("queryset AFTER filters", queryset)
        return queryset
    

    def paginate_queryset(self, queryset):
        if self.paginator is None:
            return None
        print('queryset AFTER  pagination', queryset)
        return self.paginator.paginate_queryset(queryset, self.request, view=self)