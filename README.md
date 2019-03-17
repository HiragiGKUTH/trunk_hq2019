# 仕様

## Product

* プロダクトIDから商品詳細を取得
	* Req
		* GET /api/products/{id}/
	* Res
		* 
```
[
	{
		"p_id": "hoge",
		"name": "fuga",
		"price": 1000,
		"img_url": "url to image"
	}
]
```

## Wishlist

* LINE UserIdに紐付けられたウィッシュリストに登録された**商品詳細の一覧**を取得する、ユーザーIDが不正だったり、与えられない場合すべての**ウィッシュリスト**を返す
	* Req
		* GET /api/wishlist/
		* Query userid=1
	* Res
		* 
```
[
	{
		"p_id": "hoge",
		"name": "fuga",
		"price": 1000,
		"img_url": "url to image"
	}
	,...2個以上ありえる...
]
```
	* Res(クエリが不正な時)
```
[
	{
	意味のないデータ
	}
]
```

* 指定されたユーザーIDのウィッシュリストに指定されたプロダクトIDを追加
	* Req
		* POST /api/wishlist/
		* Query userid=1 pid=1
	* Res
		* 200 OK
			* 正常に追加された
		* 400 . ----
			* 既に登録されている、プロダクトIDが存在しない、クエリ名が間違えている、など正常に登録されていないとき

* 指定されたユーザーIDの指定されたプロダクトIDの商品を削除
	* Req
		* DELETE /api/wishlist/1/
		* Query userid=1 pid=1
	* Res
		* 200 OK
			* 正常に削除**された**
		* 400 . ----
			* 指定されたウィッシュリストが存在しない
			
* 指定されたユーザーIDのすべてのウィッシュリストを削除
  * Req
    * DELETE /api/wishlist/0/
    * Query userid=1
  * Res
    * 200 OK
      * 正常に削除された
