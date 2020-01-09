from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:

    ##Esto hay q hacerlo
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):

        #Esto es lo que se va a llamar en cada request

        if not request.user.is_anonymous:

            #Si no hago esto, el /admin siempre me redireccionaria a update_profile
            if not request.user.is_staff:
                profile = request.user.profile

                #Si el usuario no tiene foto o bio
                if not profile.picture or not profile.biography:

                    #y si el path que me llega es diferente a update profile o logout
                    #Si no tuviera este if, se generaría un ciclo infinito pq update re-direccionaría a update forever and ever
                    #con logout lo que sucede 
                    if request.path not in [reverse('users:update'), reverse('users:logout')]:
                        return redirect('users:update')

        
        response = self.get_response(request)
        return response

