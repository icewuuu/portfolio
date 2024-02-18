from django.contrib.auth.models import User
from .models import Certificates, Education, Portfolio, Work
from rest_framework import permissions, viewsets

from .serializers import UserSerializer, EducationSerializer, WorkSerializer, CertificatesSerializer, PortfolioSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class EducationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Education to be viewed or edited.
    """
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class WorkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Work to be viewed or edited.
    """
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CertificatesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Certificates to be viewed or edited.
    """
    queryset = Certificates.objects.all()
    serializer_class = CertificatesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PortfolioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Portfolio to be viewed or edited.
    """
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]