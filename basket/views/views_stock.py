from django.shortcuts import redirect, render
from ..forms.forms_stock import Shopping_ListForm, ProductForm
from ..models.models_stock import Shopping_ListModel, ProductModel


# 本サービスの使い方
def how_to_usefunc(request):
    return render(request, 'how_to_use.html', {'some_data':'some_data'})

# すべての買い物リストを表示する
def all_shopping_listfunc(request):
    # useridが一致する買い物リストを取得
    user_id = request.user
    list_models = Shopping_ListModel.objects.filter(user_id=user_id).all()
    product_models = ProductModel.objects.filter(user_id=user_id).all()
    list_product_dic = {}
    for list_name in list_models:
        product_models = product_models.filter(list_name=list_name).all()
        if len(product_models) == 0:
            list_product_dic[list_name] = 'blank'
        else:
            list_product_dic[list_name] = product_models
    return render(request, 'stock/shopping_list.html', {'list_product_dic':list_product_dic})

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
    list_models = Shopping_ListModel.objects.filter(user_id=user_id).all().values()
    product_form = ProductForm(data=request.POST)
    list_choice = []
    # POST
    if request.method == 'POST':
        if product_form.is_valid():
            # ShoppingListModelに登録
            id = product_form.cleaned_data.get('list_name')
            list_query = Shopping_ListModel.objects.filter(id=id).get()
            name = product_form.cleaned_data.get('name')
            quantity = product_form.cleaned_data.get('quantity')
            new_product_model = ProductModel(list_name=list_query, name=name, quantity=quantity)
            new_product_model.save()
            return redirect('add_shopping_list')
        else:
            return render(request, 'stock/add_shopping_list.html', {'Error':'Error'})
    # GET
    else:
        # セッションが存在する場合
        try:
            session = request.session['list_name']
            list_models = Shopping_ListModel.objects.get(list_name=session)
            list_choice.append((list_models.id,session))
            product_form.fields['list_name'].widget.choices = list_choice
            del request.session['list_name']
            return render(request, 'stock/add_shopping_list.html', {'forms':product_form})

        # セッションがない場合
        except KeyError:
            # 作成済み買い物リストがない時
            if len(list_models) == 0:
                # 新しいリストを作成
                return redirect('create_shopping_list')
            
            # 作成済み買い物リストが存在するとき
            else:
                for a in list_models:
                    list_choice.append((a['id'], a['list_name']))
                # 買い物リストを選択
                product_form.fields['list_name'].widget.choices = list_choice
                return render(request, 'stock/add_shopping_list.html', {'forms':product_form})

# 買い物リストを削除する
def delete_shopping_list_func(request):
    pass
