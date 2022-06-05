from django.urls import path
from . import views

urlpatterns = [
    path(''                 , views.index           , name = 'index'            ),
    path('notepad'          , views.notepad         , name = 'notepad'          ),
    path('PdfToAudio'       , views.PdfToAudio      , name = 'PdfToAudio'       ),
    path('register'         , views.register        , name = 'register'         ),
    path('login'            , views.login           , name = 'login'            ),
    path('logout'           , views.logout          , name = 'logout'           ),
]
