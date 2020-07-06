# Blender Add-on: toggle_view
toggle_viewはViewport上でのオブジェクトので見た目を1ボタンで切り替えるアドオンです。  
切り替えの処理はUndoしません。(Undo Historyに記録されません）  
モデリングやアニメーション中に負荷の軽い状態⇔負荷の重い状態を切り替えて作業できます。  

具体的には以下の処理を行います。  
- 指定したcollectionの表示をON/OFFする
- 指定したcollectionの中のオブジェクトのモディファイア表示をON/OFFする
- Viewport Shadingを指定した設定に切り替える
<br>

toggle_view can toggle the appearances on the 3D viewport by one click.    
This process won't be registered on Undo History.     
You can toggle the visiblity between heavy state and light one.    

## 導入方法_Installation
最新版ダウンロードは[こちら](https://github.com/3str6/toggle_view/releases/download/v1.0/toggle_view.zip)  
1.編集 > プリファレンス... > アドオン > インストール > ダウンロードした.zipを選択します。  
2.下のリストに「3D View: Toggle View」が表示されるのでチェックを入れて有効化します。  
3.3Dビュー > サイドバー（Nキー） > ツール タブ > Toggle Collection, Toggle Viewport Shading パネルが追加されています。  
<br>
Download from [here](https://github.com/3str6/toggle_view/releases/download/v1.0/toggle_view.zip)  
1.Edit > Preference... > Add-on > Install > Select the downloaded workspace_importer.zip.  
2.Enable '3D View: Toggle View'.  
3.View3d > Sidebar(N-key) > Tool Tab > Toggle Collection, Toggle Viewport Shading Panel is added.  

## 機能一覧_Functions
### Toggle Collection
#### Collection  
表示をON/OFFしたいCollectionを指定します。  
Collection to toggle the visibility of.  
#### Toggle Visibility  
指定したCollectionの表示をON/OFFします。  
Toggle the visiblity of the specified colletion.  

### Toggle Viewport Shading
#### Collection
モディファイアの表示をON/OFFしたいCollectionを指定します。  
Collection to toggele modifiers' visibility of.  
#### Toggle Shading
Viewport Shadingと、指定したCollection中のオブジェクトのモディファイヤ表示をON/OFFします。   
Toggle Viewport Shading and the modifiers-visibility of the objects in the specified collection.  
#### Recursive Collection
ONにすると、Collectionの中にあるCollection中のオブジェクトのモディファイア表示もON/OFFします。   
ON: Operate collections in the specified collecion too.  
#### Toggle All Screens
ONにすると、すべてのスクリーンのViewport Shadingを切り替えます。  
ON: Toggle Viewport Shading of all screens.  
#### Toggle Viewport Shading
ONにすると、Viewport Shadingを切り替えます。  
ON: Toggle Viewport Shading.  
#### Shading Setting
切り替えたいViewport Shadingの設定を記録します。A, Bの2パターンを記録できます。  
Register A：現在のiewport Shading設定をパターンAに記録します。  
Register B：現在のiewport Shading設定をパターンAに記録します。  

You can register 2 patterns of Viewport Shading here.  
Register A: Register current Viewport Shading setting as pattern A.  
Register B: Register current Viewport Shading setting as pattern B.  
#### Toggle Modifiers
ONにすると、モディファイア表示を切り替えます。  
ON: Toggle the visibility of modifiers.  
#### Modifier Type
モディファイア表示を切り替えたいモディファイアの種類を指定します。  
Choose Modifier type to toggle.  
#### Object Type
モディファイア表示を切り替えたいオブジェクトの種類を指定します。  
Choose Object type to toggle the modifiers-visibility.  

## 類似機能を持つアドオンの紹介_Other Addons
- Batch Ops
- Pie Menus
- Collection Manager
