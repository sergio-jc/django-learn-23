# sergio-01 : print en cada request del user por medio de un middleware
class user_print_middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('user => \n', request.user)

        response = self.get_response(request)

        return response