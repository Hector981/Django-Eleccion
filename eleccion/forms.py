from django import forms
from .models import Candidato
from .models import Casilla
from .models import Funcionario
from .models import Eleccion
from .models import Rol
from .models import Eleccioncomite
from .models import Voto
from .models import Votocandidato
from .models import Funcionariocasilla
from .models import Imeiautorizado

class CasillaForm(forms.ModelForm):  
    class Meta:  
        model = Casilla
        fields = '__all__'  

class CandidatoForm(forms.ModelForm):  
    class Meta:  
        model = Candidato
        fields = '__all__'  

class FuncionarioForm(forms.ModelForm):  
    class Meta:  
        model = Funcionario
        fields = '__all__'  


class EleccionForm(forms.ModelForm):  
    class Meta:  
        model = Eleccion
        fields = '__all__'  

class RolForm(forms.ModelForm):  
    class Meta:  
        model = Rol
        fields = '__all__'  

class EleccionComiteForm(forms.ModelForm):  
    class Meta:  
        model = Eleccioncomite
        fields = '__all__'

class VotoForm(forms.ModelForm):  
    class Meta:  
        model = Voto
        fields = '__all__'

class VotoCandidatoForm(forms.ModelForm):  
    class Meta:  
        model = Votocandidato
        fields = '__all__'

class FuncionarioCasillaForm(forms.ModelForm):  
    class Meta:  
        model = Funcionariocasilla
        fields = '__all__'

class ImeiautorizadoForm(forms.ModelForm):  
    class Meta:  
        model = Imeiautorizado
        fields = '__all__'