
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Link
from .serializers import LinkSerializer
from rest_framework.request import Request
from django.utils import timezone
class LinkListCreateView(APIView):
    """
    API view for creating and retrieving shortened links.
    """

    def get_base_url(self, request):
        """
        Get the base URL where the server is running.

        Args:
            request (Request): The current HTTP request object.

        Returns:
            str: The base URL.
        """
        return request.build_absolute_uri('/')

    def get(self, request):
        """
        Retrieve a list of all shortened links.

        Args:
            request (Request): The current HTTP request object.

        Returns:
            Response: A Response object containing a list of shortened links.
        """
        links = Link.objects.all()
        serializer = LinkSerializer(links, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new shortened link.

        Args:
            request (Request): The current HTTP request object.

        Returns:
            Response: A Response object containing the created shortened link.
        """
        serializer = LinkSerializer(data=request.data)
        
        if serializer.is_valid():
            # Save the link
            link = serializer.save()
            
            # Get the base URL
            base_url = self.get_base_url(request)
            
            # Construct the complete URL with the base URL and shorten_prefix
            complete_url = base_url + link.shorten_prefix
            
            # Create a response data dictionary with the shorten_prefix and complete URL
            response_data = {
                'shorten_prefix': link.shorten_prefix,
                'complete_url': complete_url,
            }
            
            return Response(response_data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def redirect_to_original_url(request, shorten_prefix):
    """
    Redirect to the original URL associated with the given shorten_prefix.

    Args:
        request (Request): The current HTTP request object.
        shorten_prefix (str): The shorten_prefix to look up.

    Returns:
        HttpResponse: A redirect response to the original URL, or a 404 error if the shorten_prefix is not found or has expired.
    """
    try:
        link = Link.objects.get(shorten_prefix=shorten_prefix)
        
        # Check if the link has expired
        if link.expiration <= timezone.now():
            return HttpResponse('Short link has expired', status=410)  # Return a 410 Gone status
        
        return redirect(link.links)
    except Link.DoesNotExist:
        return HttpResponse('Short link not found', status=404)