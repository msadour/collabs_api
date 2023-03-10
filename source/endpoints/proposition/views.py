from django.db.models import QuerySet
from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from source.endpoints.proposition.models import Proposition
from source.endpoints.proposition.serializers import PropositionSerializer
from source.endpoints.proposition.utils import (
    get_queryset_propositions,
    cancel_proposition,
)


class PropositionViewSet(viewsets.ViewSet):

    permission_classes: list = [IsAuthenticated]
    serializer_class: PropositionSerializer = PropositionSerializer

    def list(self, request: Request) -> Response:
        queryset_proposition: QuerySet = get_queryset_propositions(
            user=request.user, data=request.data
        )
        data: dict = self.serializer_class(queryset_proposition, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

    def create(self, request: Request) -> Response:
        data: dict = request.data.copy()
        data["seller"] = request.user.id
        self.serializer_class().create(validated_data=data)
        return Response(status=status.HTTP_201_CREATED)

    def patch(self, request: Request):
        proposition_id: str = request.data.get("id")
        proposition: Proposition = Proposition.objects.get(proposition_id)
        self.serializer_class().update(
            instance=proposition, validated_data=request.data
        )
        return Response(status=status.HTTP_200_OK)

    def delete(self, request: Request):
        cancel_proposition(data=request.data)
        return Response(status=status.HTTP_204_NO_CONTENT)
