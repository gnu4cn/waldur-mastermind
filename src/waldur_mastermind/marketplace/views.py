from __future__ import unicode_literals

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import exceptions, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from waldur_core.core import views as core_views
from waldur_core.structure import filters as structure_filters
from waldur_core.structure import permissions as structure_permissions

from . import serializers, models, filters


class ServiceProviderViewSet(core_views.ActionsViewSet):
    queryset = models.ServiceProvider.objects.all()
    serializer_class = serializers.ServiceProviderSerializer
    lookup_field = 'uuid'
    filter_backends = (structure_filters.GenericRoleFilter, DjangoFilterBackend)
    filter_class = filters.ServiceProviderFilter

    def staff_or_owner(request, view, obj=None):
        return obj and _staff_or_owner(request, obj.customer)

    destroy_permissions = [staff_or_owner]


class CategoryViewSet(core_views.ActionsViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    lookup_field = 'uuid'
    filter_backends = (structure_filters.GenericRoleFilter, DjangoFilterBackend)

    def is_staff(request, view, obj=None):
        if request.user.is_staff:
            return

        raise exceptions.PermissionDenied()

    create_permissions = [is_staff]
    update_permissions = [is_staff]
    partial_update_permissions = [is_staff]
    destroy_permissions = [is_staff]


class OfferingViewSet(core_views.ActionsViewSet):
    queryset = models.Offering.objects.all()
    serializer_class = serializers.OfferingSerializer
    lookup_field = 'uuid'
    filter_backends = (structure_filters.GenericRoleFilter, DjangoFilterBackend)

    @detail_route()
    def screenshots(self, request, uuid):
        offering = self.get_object()
        screenshots = offering.screenshots.all()
        serializer = serializers.ScreenshotSerializer(instance=screenshots, many=True, context={
            'request': request,
        })
        return Response(serializer.data, status=status.HTTP_200_OK)

    def staff_or_owner(request, view, obj=None):
        return obj and _staff_or_owner(request, obj.provider.customer)

    destroy_permissions = [staff_or_owner]


class ScreenshotViewSet(core_views.ActionsViewSet):
    queryset = models.Screenshots.objects.all()
    serializer_class = serializers.ScreenshotSerializer
    lookup_field = 'uuid'
    filter_backends = (structure_filters.GenericRoleFilter, DjangoFilterBackend)
    filter_class = filters.ScreenshotstFilter

    def staff_or_owner(request, view, obj=None):
        return obj and _staff_or_owner(request, obj.offering.provider.customer)

    destroy_permissions = [staff_or_owner]


def _staff_or_owner(request, customer):
    if request.user.is_staff:
        return
    if not structure_permissions._has_owner_access(request.user, customer):
        raise exceptions.PermissionDenied()
