from django import forms

class Shopping_ListNameForm(forms.Form):
    list_name = forms.ChoiceField(
        widget=forms.TextInput(attrs={'class':'form-control', 'name':'list_name'}),
        label='買い物リスト名'
        )

class Shopping_ListForm(forms.Form):
    list_name = forms.ChoiceField(
        widget=forms.Select(attrs={'class':'form-control', 'name':'list_name'}),
        label='買い物リスト名'
        )
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'text', 'name':'name_0'}),
        label='品名'
        )
    quantity = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'text',  'name':'quantity_0'}),
        label='個数'
        )
    memo = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'text',  'name':'memo_0'}),
        label='メモ',
        required=False
        )
