from decimal import Decimal
from django.conf import settings
from products.models import Product
from django.http import HttpResponse
from django.shortcuts import render, redirect


class Cart(object):

    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self,product, quantity=1, action=None):
        """
        Add a product to the cart or update its quantity.
        """
        slug = product.slug
        newItem = True
        if str(product.productid) not in self.cart.keys():
            print(self.cart)
            self.cart[product.productid]={
                    'userid':self.request.user.id,
                    'title':slug,
                    'quantity': quantity,
                    'price': str(product.price),
                    'photo' : product.photo.url,
                    'productid':product.productid
                    }
        else:
            newItem = True
            print('okk')
            for key,value in self.cart.items():
                if key == str(product.productid):
                    print('okkk')
                    value['quantity'] = value['quantity'] + quantity
                    newItem = False
                    self.save()
                    break
            if newItem == True:
                print('okkkk')
                self.cart[product.productid]={
                    'userid': self.request,
                    'title':slug,
                    'quantity': quantity,
                    'price': str(product.price),
                    'photo' : product.photo.url,
                    'productid':product.productid

                    }



        self.save()
    # def add(self,product, quantity=1, action=None):
    #     """
    #     Add a product to the cart or update its quantity.
    #     """
    #     slug = product.slug
    #     newItem = True
    #     if str(product.productid) not in self.cart.keys():
    #         print(self.cart)
    #         self.cart[product.productid]={
    #                 'userid':self.request.user.id,
    #                 'title':slug,
    #                 'quantity': 1,
    #                 'price': str(product.price),
    #                 'photo' : product.photo.url,
    #                 'productid':product.productid
    #                 }
    #     else:
    #         newItem = True
    #         print('okk')
    #         for key,value in self.cart.items():
    #             if key == str(product.productid):
    #                 print('okkk')
    #                 value['quantity'] = value['quantity'] + 1
    #                 newItem = False
    #                 self.save()
    #                 break
    #         if newItem == True:
    #             print('okkkk')
    #             self.cart[product.productid]={
    #                 'userid': self.request,
    #                 'title':slug,
    #                 'quantity': 1,
    #                 'price': str(product.price),
    #                 'photo' : product.photo.url,
    #                 'productid':product.productid

    #                 }



    #     self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.productid)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def decrement(self,product):
        for key,value in self.cart.items():
            if key == str(product.productid):
                print('okkk')
                value['quantity'] = value['quantity'] - 1
                if(value['quantity'] < 1):
                    return redirect('cart:cart_detail')
                self.save()
                break
            else:
                print("Something Wrong")


    def clear(self):
        # empty cart
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True
