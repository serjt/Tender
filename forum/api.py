from sqlite3 import IntegrityError

from tastypie.exceptions import BadRequest
from tastypie.resources import ModelResource, ALL_WITH_RELATIONS
from tastypie import fields
from .models import *
from tastypie.authorization import Authorization


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        Authorization=Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']

    def obj_create(self, bundle, request=None, **kwargs):

        username, password = bundle.data['username'], bundle.data['password']
        try:
            bundle.obj = User.objects.create_user(username, '', password)
        except IntegrityError:
            raise BadRequest('That username already exists')
        return bundle


class StoryResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user', full=True, null=True)

    class Meta:
        queryset = Story.objects.order_by('created_at')
        resource_name = 'story'
        filtering = {
            'id': ALL_WITH_RELATIONS
        }
        allowed_methods = ['get', 'post', 'put', 'delete']


class QuestionResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user', full=True, null=True)

    class Meta:
        queryset = Question.objects.order_by('created_at')
        resource_name = 'question'
        filtering = {
            'id': ALL_WITH_RELATIONS
        }
        allowed_methods = ['get', 'post', 'put', 'delete']


class CommentResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user', full=True, null=True)
    question = fields.ForeignKey(QuestionResource, 'question', full=True, null=True)

    class Meta:
        queryset = Comment.objects.order_by('created_at')
        resource_name = 'comment'
        filtering = {
            'id': ALL_WITH_RELATIONS
        }
        allowed_methods = ['get', 'post', 'put', 'delete']