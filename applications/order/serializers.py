from rest_framework import serializers

from applications.product.models import Product
from applications.order.tasks import send_confirm_link
from applications.order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Order
        exclude = ['confirm_code', 'order_confirm']

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        order.create_confirm_code()
        order.save()
        send_confirm_link.delay(order.user.email, order.confirm_code)
        return order

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        product = Product.objects.get(id=rep['product']).title
        rep['order_confirm'] = instance.order_confirm
        rep['product'] = product
        return rep

    def validate(self, attrs):
        product = attrs['product']
        count = attrs['count']
        if product.amount < count:
            raise serializers.ValidationError(f'вы не можете заказать такое количество, осталось {product.amount}')
        return attrs