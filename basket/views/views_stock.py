from django.shortcuts import redirect, render
from ..forms.forms_stock import Shopping_ListForm, ProductForm
from ..models.models_stock import Shopping_ListModel, ProductModel
from datetime import datetime

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
    list_forms = Shopping_ListForm(request.POST)
    user_id = request.user
    if request.method == 'POST':
        post_data = request.POST['list_name']
        # すでにDBに存在するか確認する
        list_models = Shopping_ListModel.objects.filter(list_name=post_data).all()
        if len(list_models) != 0:
            return render(request, 'stock/create_shopping_list.html', {'forms':list_forms, 'Error_Name':post_data})
        # 入力されたデータをDBに保存
        new_list_models = Shopping_ListModel(user_id=user_id, list_name=post_data)
        new_list_models.save()
        # セッションに保存する
        request.session['list_name'] = post_data
        # 商品の追加に進む
        return redirect('add_shopping_list')
    else:
        return render(request, 'stock/create_shopping_list.html', {'forms':list_forms})

# 買い物リストに商品を追加
def add_shopping_list_func(request):
    user_id = request.user
    list_models = Shopping_ListModel.objects.filter(user_id=user_id).all()
    product_model = ProductModel()
    product_form = ProductForm(data=request.POST)
    list_choice = []
    for a in list_models.values():
        print(a['created_date'])
    # POST
    if request.method == 'POST':
        if product_form.is_valid():
            # ShoppingListModelに登録後
            list_models.filter(list_name=product_form)
            return redirect('add_shopping_list')
    # GET
    else:
        # セッションが存在する場合
        try:
            session = request.session['list_name']
            list_choice.append((session,session))
            product_form.fields['list_name'].widget.choices = list_choice
            del request.session['list_name']
            return render(request, 'stock/add_shopping_list.html', {'forms':product_form})

        # セッションがない場合
        except KeyError:
            # 作成済み買い物リストがあるか調べる
            if len(list_models) == 0:
                # 新しいリストを作成
                return redirect('create_shopping_list')
            else:
                for a in list_models.values('list_name'):
                    list_choice.append((a['list_name'], a['list_name']))
                # 買い物リストを選択
                product_form.fields['list_name'].widget.choices = list_choice
                return render(request, 'stock/add_shopping_list.html', {'forms':product_form})
