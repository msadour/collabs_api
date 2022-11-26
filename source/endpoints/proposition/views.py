"""Views proposition module."""

from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from source.endpoints.proposition.utils import ActionProposition


class PropositionViewSet(viewsets.ViewSet):
    """Class PropositionViewSet."""

    permission_classes = [IsAuthenticated]

    def list(self, request: Request) -> Response:
        """List user proposition.

        Args:
            request: request sent by the client.

        Returns:
            Response from the server with list of users.
        """
        action = ActionProposition(request=request)
        data: list = action.retrieve_proposition()
        return Response(data, status=status.HTTP_200_OK)

    def create(self, request: Request) -> Response:
        """Make a proposition.

        Args:
            request: request sent by the client.

        Returns:
            Response from the server.
        """
        action = ActionProposition(request=request)
        action.make_proposition()
        return Response(status=status.HTTP_201_CREATED)

    def patch(self, request: Request):
        """Update a proposition.

        Args:
            request: request sent by the client.

        Returns:
            Response from the server.
        """
        action = ActionProposition(request=request)
        action.update_proposition()
        return Response(status=status.HTTP_200_OK)
