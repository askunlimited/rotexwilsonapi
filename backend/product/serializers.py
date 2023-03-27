from rest_framework import serializers

from .models import Post, Category


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'
    
    
  def create(self, validated_data):
    
    return Category.objects.create(**validated_data)

  
  def update(self, instance, validated_data):
    instance.name = validated_data.get('name', instance.name)
    instance.parent = validated_data.get('parent', instance.parent)
    instance.save()
    return instance
  
  
  
  
  

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = '__all__'
    
  
  def create(self, validated_data):
    
    return Post.objects.create(**validated_data)
  
  
  def update(self, instance, validated_data):
    instance.name = validated_data.get('name', instance.name)
    instance.description = validated_data.get('description', instance.description)
    instance.weight_in_tons = validated_data.get('weight_in_tons', instance.weight_in_tons)
    instance.amount = validated_data.get('amount', instance.amount)
    instance.location = validated_data.get('location', instance.location)
    instance.category = validated_data.get('category', instance.category)
    instance.remark = validated_data.get('remark', instance.remark)
    
    instance.save()
    return instance
  

  def retrieve_instance(self, instance):
    instance = Post.objects.get(id=self.context['request'].data['id'])
    return instance
  