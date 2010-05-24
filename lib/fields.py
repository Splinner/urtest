# File encoding: utf-8

from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import CheckboxSelectMultiple

class UrtestPasswordField(forms.CharField):
    """
    Локальное поле для ввода пароля

    Ограничивает min/max_length и виджет
    """
    def __init__(self, *args, **kwargs):
        forms.CharField.__init__(self,
                                 min_length=5,
                                 max_length=30,
                                 widget=forms.PasswordInput(render_value=False),
                                 *args, **kwargs)


class UrtestFIOField(forms.RegexField):
    """
    Локальное поле для ФИО

    Ограничивает валидацию и сообщения
    """
    fio_regexp = (u'^[А-ЯA-Z][A-ZА-Яa-zа-я ]*(-[A-ZА-Яa-zа-я ]+)?$')
    generic_error = {"invalid": "Неправильно введены данные"}

    def __init__(self, *args, **kwargs):
        forms.RegexField.__init__(self,
                                  regex=self.fio_regexp,
                                  error_messages=self.generic_error,
                                  *args, **kwargs)


class UrtestTextAreaField(forms.CharField):
    """
    Локальное поле для больших текстов

    Ограничивает max_length и виджет
    """
    def __init__(self, *args, **kwargs):
        forms.CharField.__init__(self,
                                 max_length=600,
                                 widget=forms.Textarea,
                                 *args, **kwargs)


class UrtestPassportSeriesField(forms.RegexField):
    """
    Локальное поле для серии паспорта

    Ограничивает max_length и виджет
    """
    passport_series_reg = '(^\d{4}$)'
    generic_error = {"invalid": "Должно быть введено ровно 4 цифры"}

    def __init__(self, *args, **kwargs):
        forms.RegexField.__init__(self,
                                  regex=self.passport_series_reg,
                                  error_messages=self.generic_error,
                                  *args, **kwargs)


class UrtestPassportNumberField(forms.RegexField):
    """
    Локальное поле для номера паспорта

    Ограничивает max_length и виджет
    """
    passport_series_reg = '(^\d{6}$)'
    generic_error = {"invalid": "Должно быть введено ровно 6 цифр"}

    def __init__(self, *args, **kwargs):
        forms.RegexField.__init__(self,
                                  regex=self.passport_series_reg,
                                  error_messages=self.generic_error,
                                  *args, **kwargs)


class UrtestinnNumberField(forms.RegexField):
    """
    Локальное поле для инн

    Ограничивает max_length
    """
    inn_regex = '(^\d{0,10}$)'
    generic_error = {"invalid": "Должно быть введено не более 10 цифр"}

    def __init__(self, *args, **kwargs):
        forms.RegexField.__init__(self,
                                  regex=self.inn_regex,
                                  error_messages=self.generic_error,
                                  *args, **kwargs)



class UrtestNumberField(forms.RegexField):
    """
    Локальное поле для чисел

    Ограничивает max_length
    """
    inn_regex = '(^\d{0,50}$)'
    generic_error = {"invalid": "Должно быть введено не более 50 цифр"}

    def __init__(self, *args, **kwargs):
        forms.RegexField.__init__(self,
                                  regex=self.inn_regex,
                                  error_messages=self.generic_error,
                                  *args, **kwargs)