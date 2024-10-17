from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib.auth import logout
from django.contrib import messages

def index(request):
    categorias = Categoria.objects.all()  
    fundaciones = Ong.objects.all()
    return render(request, 'ongCrowndfunding/index.html', {
        'fundaciones': fundaciones,
        'categorias': categorias,
    })
def donar(request):
    categorias = Categoria.objects.all()  
    return render(request, 'ongCrowndfunding/donar.html', {
        'categorias': categorias,
    })

def registroView(request):
    categorias = Categoria.objects.all()
    registro = RegistroForm()
    return render(request, 'ongCrowndfunding/registro.html', {
        'categorias': categorias,
        'form':registro
    })

def crearCampañasView(request):
    categorias = Categoria.objects.all()
    crearCampaña = OngForm()
    return render(request, 'ongCrowndfunding/crearCampañas.html', {
        'categorias': categorias,
        'form':crearCampaña
    })

def campañasView(request):
    fundaciones = Ong.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'ongCrowndfunding/gestionCampañas/campañas.html', {
        'fundaciones': fundaciones,
        'categorias': categorias,
    })

def reportesView(request):
    fundaciones = Ong.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'ongCrowndfunding/gestionCampañas/reportes.html', {
        'fundaciones': fundaciones,
        'categorias': categorias,
    })

def transaccionesView(request):
    transacciones = Transaccion.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'ongCrowndfunding/gestionCampañas/transacciones.html', {
        'transacciones': transacciones,
        'categorias': categorias,
    })
    
def logout_view(request):
    logout(request)
    print("Cerrando Sesion...")
    return redirect('index')

#Crear campañas
@login_required
def CrearOng(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        descripcion = request.POST["descripcion"]
        objetivo = request.POST["objetivo"]
        imagen = request.POST["imagen"]
        id_categoria = request.POST["id_categoria"]

        # Asegúrate de que el id_categoria se obtiene correctamente
        categoria = Categoria.objects.get(id_categoria=id_categoria)

        # Crea la instancia de Ong con el usuario que ha iniciado sesión
        fundacion = Ong.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            objetivo=objetivo,
            imagen=imagen,
            fundador=request.user,  # Aquí estableces el fundador como el usuario que ha iniciado sesión
            id_categoria=categoria,
        )
        context = {'mensaje': "Ok, datos grabados..."}

        return redirect('crearCampañas')
    
    else:
        categorias = Categoria.objects.all()
        context = {'categorias': categorias}
        return render(request, 'ongCrowndfunding/crearCampañas.html', context)
    
#registro
def registro(request):
    if request.method == "POST":
        registro = RegistroForm(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect(to="login")
        print("Registro exitosamente")
    else:
        registro = RegistroForm()
    return render(request, 'ongCrowndfunding/registro.html', {'form':registro})

#Donar
@login_required
def DonarFundacion(request, ong_id):
    ong = get_object_or_404(Ong, id=ong_id)  # Captura la ONG según el ID

    if request.method == "POST":
        monto_donado = request.POST["monto_donado"]
        
        # Crea la transacción con la ONG capturada
        Transaccion.objects.create(
            donante=request.user,
            fundacion=ong,
            monto_donado=monto_donado
        )
        messages.success(request, "Ok, datos grabados...")
        return redirect('Donar', ong_id=ong_id)  # Redirige de vuelta a la vista de donación (opcional)
    
    return render(request, 'ongCrowndfunding/Donar.html', {'ong': ong})