from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class ListRetrieveUpdateViewSetMixin(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    pass


class RetrieveUpdateViewSetMixin(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    pass


class CreateRetrieveUpdateViewSetMixin(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    pass


class ListCreateRetrieveViewSetMixin(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    pass


class ListCreateViewSetMixin(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    pass


class ListViewSetMixin(
    mixins.ListModelMixin,
    GenericViewSet
):
    pass


class ListRetrieveViewSetMixin(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    pass


class DestroyViewSetMixin(
    mixins.DestroyModelMixin,
    GenericViewSet
):
    pass


class ListCreateRetrieveUpdateDestroySetMixin(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    pass


class ListRetrieveUpdateDestroySetMixin(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    pass


class ListCreateRetrieveUpdateSetMixin(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    pass


class ListRetrieveCreateSetMixinCreateViewSetMixin(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet
):
    pass


class ListRetrieveCreateDestroySetMixin(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    pass
