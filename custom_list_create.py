from rest_framework import generics

class CustomListCreateAPIView(generics.ListCreateAPIView):

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request

        return context

    
    def filter_queryset(self, queryset):
        print("queryset BEFORE filters: \n", queryset)
        result = super().filter_queryset(queryset)
        print("queryset AFTER filters: \n", result)
        return result
    

    def paginate_queryset(self, queryset):
        result = super().paginate_queryset(queryset)
        print('queryset AFTER pagination: \n', result)
        return result