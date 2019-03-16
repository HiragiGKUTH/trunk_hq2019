from rest_framework import viewsets
from rest_framework.response import Response
from oapi.models import Product, Wishlist

from oapi.serializers import ProductSerializer, WishlistSerializer


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return  Response(serializer.data)

    def retrieve(self, request, pk):
        res = Product.objects.get(p_id=pk)
        serializer = ProductSerializer(res, many=False)
        return Response(serializer.data)

class WishlistViewSet(viewsets.ViewSet):
    def list(self, request):
        line_userid = request.query_params.get("userid")
        if line_userid == None:
            res = Wishlist.objects.all()
            slz = WishlistSerializer(res, many=True)
            return Response(slz.data)

        wishes_from_userid = Wishlist.objects.filter(l_id=line_userid).values()
        ids = [x["product_id"] for x in wishes_from_userid]
        res = Product.objects.filter(p_id__in=ids)
        res = ProductSerializer(res, many=True)
        return Response(res.data);

    def create(self, request):
        line_userid = request.query_params.get("userid")
        product_id = request.query_params.get("pid")
        if line_userid == None or product_id == None:
            return Response("403 Bad Request. Missing of query params", status=403)

        try:
            p = Product.objects.get(p_id=str(product_id))
        except:
            return Response("403 Bad Request. called product_id is not assigned", status=403)

        try: 
            Wishlist.objects.get(l_id=line_userid, product=p)
        except:
            w = Wishlist(l_id=line_userid, product=p)
            w.save()
            return Response("200 OK")
        return Response("403 Bad Request. wishlist is already assigned", status=403)
            
