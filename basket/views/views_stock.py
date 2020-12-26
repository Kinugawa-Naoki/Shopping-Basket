from django.shortcuts import redirect, render
from ..forms.forms_stock import Shopping_ListForm, Shopping_ListNameForm
from ..models.models_stock import Shopping_ListModel, Shopping_ListNameModel

# 買い物リストを表示する
def shopping_listfunc(request):
    user_id = request.user
    models = Shopping_ListModel.objects.filter(user_id=user_id).all()
    return render(request, 'shopping_list.html', {'models':models})

# 買い物リストを作成する
def create_shopping_list_func(request):
    forms = Shopping_ListNameForm
    if request.method == 'POST':
        # 入力されたデータをDBに保存
        post_data = request.POST['list_name']
        models = Shopping_ListNameModel(list_name=post_data)
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
    list = Shopping_ListNameModel.objects.filter(user_id=user_id).all
    session = request.session['list_name']
    # 保存したセッションが調べる
    if session is None:
        # 作成済み買い物リストがあるか調べる
        if list is None:
            # 新しいリストを作成
            pass
        else:
            # 買い物リストを選択
            pass

    # セッションがあった時
    else:
        
        forms = Shopping_ListForm(request.POST)
        if request.method == 'POST':
            pass
        else:
            return render(request, 'stock/add_shopping_list.html', {'forms':forms})
    