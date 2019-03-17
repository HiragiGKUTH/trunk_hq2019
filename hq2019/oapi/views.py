from rest_framework import viewsets
from rest_framework.response import Response
from oapi.models import Product, Wishlist

from oapi.serializers import ProductSerializer, WishlistSerializer


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return  Response(serializer.data, headers={"Access-Control-Allow-Origin": "*"})

    def retrieve(self, request, pk):
        res = Product.objects.get(p_id=pk)
        serializer = ProductSerializer(res, many=False)
        return Response(serializer.data, headers={"Access-Control-Allow-Origin": "*"})

class WishlistViewSet(viewsets.ViewSet):
    def list(self, request):
        line_userid = request.query_params.get("userid")
        if line_userid == None:
            res = Wishlist.objects.all()
            slz = WishlistSerializer(res, many=True)
            return Response(slz.data,  headers={"Access-Control-Allow-Origin": "*"})

        wishes_from_userid = Wishlist.objects.filter(l_id=line_userid).values()
        ids = [x["product_id"] for x in wishes_from_userid]
        res = Product.objects.filter(p_id__in=ids)
        res = ProductSerializer(res, many=True)
        return Response(res.data);

    def create(self, request):
        line_userid = request.query_params.get("userid")
        product_id = request.query_params.get("pid")
        if line_userid == None or product_id == None:
            return Response("400 . Missing of query params", status=403)

        try:
            p = Product.objects.get(p_id=str(product_id))
        except:
            return Response("400 . called product_id is not assigned", status=403)

        try: 
            Wishlist.objects.get(l_id=line_userid, product=p)
        except:
            w = Wishlist(l_id=line_userid, product=p)
            w.save()
            return Response("200 OK")
        return Response("400 . wishlist is already assigned", status=403)
            
    def destroy(self, request, pk):
        line_userid = request.query_params.get("userid")
        product_id = request.query_params.get("pid")
        if line_userid == None or product_id == None:
            return Response("400 . invalid userid")
        p = Product.objects.get(p_id=product_id)
        w = Wishlist.objects.filter(l_id=line_userid, product=p, persisted=False)
        w.delete();
        return Response("200 OK")
