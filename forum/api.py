from tastypie.resources import ModelResource, ALL_WITH_RELATIONS
from tastypie import fields
from tastypie.paginator import Paginator
from .models import *


class PageNumberPaginator(Paginator):
    def page(self):
        output = super(PageNumberPaginator, self).page()
        output['page_number'] = int(self.offset / self.limit) + 1
        return output


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'


class StoryResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user', full=True, null=True)

    class Meta:
        queryset = Story.objects.order_by('created_at')
        resource_name = 'story'
        filtering = {
            'id': ALL_WITH_RELATIONS
        }
        paginator_class = PageNumberPaginator


class QuestionResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user', full=True, null=True)

    class Meta:
        queryset = Question.objects.order_by('created_at')
        resource_name = 'question'
        filtering = {
            'id': ALL_WITH_RELATIONS
        }


class CommentResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user', full=True, null=True)
    question = fields.ForeignKey(QuestionResource, 'question', full=True, null=True)

    class Meta:
        queryset = Comment.objects.order_by('created_at')
        resource_name = 'comment'
        filtering = {
            'id': ALL_WITH_RELATIONS
        }