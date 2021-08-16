from django.http import HttpResponse
from rest_framework.decorators import api_view,  permission_classes
from django.views.decorators.csrf import csrf_exempt

@api_view(['GET'])
def test_api(request):
    user_agent=request.META['HTTP_USER_AGENT']
    template = f'<h3>Conectado desde {user_agent}</h3>' 
    return HttpResponse(template)


@api_view(['GET'])
def test_api2(request):
    '''
    permite probar si esta funcionando correctamente la Api enviardo como parametro GET 'msj'
    ej: http://localhost:8000/e_commerce/api/test/?msj=hola
    '''
    
    msj= request.GET.get('msj','No hay parametro \'msj\'!!')
    template= f'<h1> {msj} </h1>'  
    return  HttpResponse(template)


@api_view(['POST'])
@permission_classes([])
def suma_post_api(request):
    '''
    procedimiento para probar solicitudes POST a la API
    espera dos parametros 
        param1 y param2 
    devuelve la suma de ambos
    '''
    param1=request.POST.get('param1')
    param2=request.POST.get('param2')
    template= f'{int(param1)+int(param2)}'
    return HttpResponse(template)

