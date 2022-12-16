from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from source.endpoints.proposition.utils import ActionProposition


class PropositionViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]

    def list(self, request: Request) -> Response:
        action = ActionProposition(request=request)
        data: list = action.retrieve_proposition()
        return Response(data, status=status.HTTP_200_OK)

    def create(self, request: Request) -> Response:
        action = ActionProposition(request=request)
        action.make_proposition()
        return Response(status=status.HTTP_201_CREATED)

    def patch(self, request: Request):
        action = ActionProposition(request=request)
        action.update_proposition()
        return Response(status=status.HTTP_200_OK)
