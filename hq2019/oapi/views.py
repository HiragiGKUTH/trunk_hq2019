from rest_framework import viewsets
from rest_framework.response import Response
from oapi.models import Product, Wishlist, Popularity

from oapi.serializers import ProductSerializer, WishlistSerializer, PopularitySerializer


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
        # set parameters
        line_userid = request.query_params.get("userid")
        product_id = request.query_params.get("pid")

        # param check
        if line_userid == None or product_id == None:
            return Response("400 . Missing of query params", status=403)

        # product existance test
        try:
            p = Product.objects.get(p_id=str(product_id))
        except:
            return Response("400 . called product_id is not assigned", status=403)

        # save if wishlist is not assigned
        try: 
            Wishlist.objects.get(l_id=line_userid, product=p)
        except:
            # persist
            w = Wishlist(l_id=line_userid, product=p)
            w.save()

            # increase popularity
            obj, created = Popularity.objects.get_or_create(product=p)
            if created:
                obj.scan_count = 1
            else:
                obj.scan_count += 1
            obj.save()
            return Response("200 OK")
        return Response("400 . wishlist is already assigned", status=403)
            
    def destroy(self, request, pk):
        line_userid = request.query_params.get("userid")
        product_id = request.query_params.get("pid")
        
        if pk == "0" and line_userid != None:
            w = Wishlist.objects.filter(l_id=line_userid)
            w.delete()
            return Response("200 OK")
        
        if line_userid == None or product_id == None:
            return Response("400 . invalid userid or pid")
        p = Product.objects.get(p_id=product_id)
        w = Wishlist.objects.filter(l_id=line_userid, product=p, persisted=False)
        w.delete();
        return Response("200 OK")

class PopularityViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Popularity.objects.all()
        res = PopularitySerializer(queryset, many=True)
        return Response(res.data)
