from django import forms

class formulario_Cerveza(forms.Form):
    marca = forms.CharField(max_length = 60)
    color = forms.CharField(max_length = 10)
    ibu = forms.CharField(max_length = 5)
    alcohol = forms.CharField(max_length = 4)
    cantMl = forms.IntegerField()


class formulario_Ginebra(forms.Form):
    marca = forms.CharField(max_length = 60)
    sabor = forms.CharField(max_length = 60)
    alcohol = forms.CharField(max_length = 4)
    cantMl = forms.IntegerField()



class formulario_Mezcal(forms.Form):
    marca = forms.CharField(max_length = 60)
    tipoAgave = forms.CharField(max_length = 60)
    clasificacion = forms.CharField(max_length = 20)
    alcohol = forms.CharField(max_length = 4)
    cantMl = forms.IntegerField()