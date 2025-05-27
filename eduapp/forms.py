from django import forms
from .models import Student
from django.core.validators import MinValueValidator, MaxValueValidator

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'gender', 'email', 'course', 'average_score']

    name = forms.CharField(
        label='ФИО',
        widget=forms.TextInput(attrs={'placeholder': 'Введите ФИО'})
    )
    gender = forms.ChoiceField(
        label='Пол',
        choices=Student.GENDER_CHOICES,
        widget=forms.Select()
    )
    email = forms.EmailField(
        label='Электронная почта',
        widget=forms.EmailInput(attrs={'placeholder': 'example@mail.ru'})
    )
    course = forms.IntegerField(
        label='Курс',
        validators=[MinValueValidator(1), MaxValueValidator(4)],
        widget=forms.NumberInput(attrs={'placeholder': 'От 1 до 4', 'min': 1, 'max': 4})
    )
    average_score = forms.DecimalField(
        label='Средний балл',
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        max_digits=4,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'placeholder': 'От 0 до 10', 'min': 0, 'max': 10, 'step': '0.01'})
    )