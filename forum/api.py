from sqlite3 import IntegrityError
from tastypie.constants import ALL
from tastypie.exceptions import BadRequest
from tastypie.resources import ModelResource, ALL_WITH_RELATIONS
from tastypie import fields
from .models import *
from tastypie.authorization import Authorization, DjangoAuthorization


class UserResource(ModelResource):
    class Meta:
        resource_name = 'user'
        queryset = User.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']
        filtering = {
            'id':ALL,
            'username': ALL_WITH_RELATIONS,
            'password': ALL_WITH_RELATIONS,
            'email': ALL_WITH_RELATIONS,
        }

    def obj_create(self, bundle, request=None, **kwargs):

        username, password, email = bundle.data['username'], bundle.data['password'], bundle.data['email']
        try:
            bundle.obj = User.objects.create_user(username=username, password=password, email=email)
        except IntegrityError:
            raise BadRequest('That username already exists')
        return bundle


class StoryResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user', null=True)

    class Meta:
        queryset = Story.objects.order_by('created_at')
        resource_name = 'story'
        filtering = {
            'id': ALL,
            'user': ALL_WITH_RELATIONS
        }
        allowed_methods = ['get', 'post', 'put', 'delete']
        authorization = Authorization()


class QuestionResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user', full=True, null=True)

    class Meta:
        queryset = Question.objects.order_by('created_at')
        resource_name = 'question'
        filtering = {
            'id': ALL,
            'user':ALL_WITH_RELATIONS
        }
        allowed_methods = ['get', 'post', 'put', 'delete']
        authorization = Authorization()


class CommentResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user', full=True, null=True)
    question = fields.ForeignKey(QuestionResource, 'question', full=True, null=True)

    class Meta:
        queryset = Comment.objects.order_by('created_at')
        resource_name = 'comment'
        filtering = {
            'id': ALL,
            'question':ALL_WITH_RELATIONS,
            'user':ALL_WITH_RELATIONS,
        }
        allowed_methods = ['get', 'post', 'put', 'delete']

        authorization = Authorization()

