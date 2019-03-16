# テーマ

* 関西の「食」をテクノロジーで楽しくする
aaa

## 仕様

* 商品取得
GET /product/{id}/
Res:

```json:res.json
[
  {
    "name":"hoge",
    "price":1000,
  }
]
```

* ほしいものリスト追加
POST /wishlist?userid=1000
Res:
200 OK

* ほしいものリストの取得
GET /wishlist
Res:

```
[
  {
    "name":"hoge",
    "price":1000,
    "image": "url to image"
  },  
  {
    "name":"fuga",
    "price":2000,
    "image": "url to image"
  },
]
```
