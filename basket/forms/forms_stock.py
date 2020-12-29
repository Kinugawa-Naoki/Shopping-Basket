from django import forms

class Shopping_ListForm(forms.Form):
    list_name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'name':'list_name'}),
        label='買い物リスト名',
        max_length=50,
        )
    memo = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'text',  'name':'memo_0'}),
        label='メモ',
        max_length=50,
        required=False
        )

class ProductForm(forms.Form):
    list_name = forms.CharField(
        widget=forms.Select(attrs={'class':'form-control', 'name':'list_name'}),
        label='買い物リスト名',
        max_length=50,
        required=True
        )
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'text', 'name':'name_0'}),
        label='品名',
        max_length=50,
        required=True
        )
    quantity = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'text',  'name':'quantity_0'}),
        label='個数',
        max_length=50,
        required=False
        )
