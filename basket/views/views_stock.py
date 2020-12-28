from django.db import models
from django.shortcuts import redirect, render
from ..forms.forms_stock import Shopping_ListForm, Shopping_ListNameForm
from ..models.models_stock import Shopping_ListModel, Shopping_ListNameModel

# 本サービスの使い方
def how_to_usefunc(request):
    return render(request, 'how_to_use.html', {'some_data':'some_data'})

# 買い物リストを表示する
def shopping_listfunc(request):
    user_id = request.user
    models = Shopping_ListModel.objects.filter(user_id=user_id).all()
    return render(request, 'shopping_list.html', {'models':models})

# 買い物リストを作成する
def create_shopping_list_func(request):
    forms = Shopping_ListNameForm(request.POST)
    user_id = request.user
    if request.method == 'POST':
        post_data = request.POST['list_name']
        # すでにDBに存在するか確認する
        models = Shopping_ListNameModel.objects.filter(list_name=post_data).all()
        if len(models) != 0:
            return render(request, 'stock/create_shopping_list.html', {'forms':forms, 'Error_Name':post_data})
        # 入力されたデータをDBに保存
        models = Shopping_ListNameModel(user_id=user_id, list_name=post_data)
        models.save()
        # セッションに保存する
        request.session['list_name'] = post_data
        # 商品の追加に進む
        return redirect('add_shopping_list')
    else:
        return render(request, 'stock/create_shopping_list.html', {'forms':forms})

# 買い物リストに商品を追加
def add_shopping_list_func(request):
    user_id = request.user
    name_models = Shopping_ListNameModel.objects.filter(user_id=user_id).all()
    model = Shopping_ListModel()
    forms = Shopping_ListForm(request.POST)
    list_choice = []
    # POST
    if request.method == 'POST':
        print(request.POST['list_name'])
        print(request.POST['name'])
        print(request.POST['quantity'])
        print(request.POST['memo'])
        pass
    # GET
    else:
        # セッションが存在する場合
        try:
            session = request.session['list_name']
            list_choice.append((session,session))
            forms.fields['list_name'].choices = list_choice
            del request.session['list_name']
            return render(request, 'stock/add_shopping_list.html', {'forms':forms})

        # セッションがない場合
        except KeyError:
            # 作成済み買い物リストがあるか調べる
            if len(name_models) == 0:
                # 新しいリストを作成
                return redirect('create_shopping_list')
            else:
                for a in name_models.values('list_name'):
                    list_choice.append((a['list_name'], a['list_name']))
                # 買い物リストを選択
                forms.fields['list_name'].choices = list_choice
                return render(request, 'stock/add_shopping_list.html', {'forms':forms, 'list_name':'None'})



