import json

from django.core.mail import send_mail
from django.core.serializers import serialize
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *


def process_query(model_query):
    query = model_query
    query = serialize("json", query)
    query = json.loads(query)

    return query



@api_view(['GET'])
def home(request):
    try:
        home_page_carousel = process_query(HomePageCarousel.objects.all())
        experience = process_query(Experience.objects.all())
        clients = process_query(Clients.objects.all())
        expertise = process_query(Expertise.objects.all())
        service_cards = process_query(ServiceCard.objects.all())
        mission = process_query(Mission.objects.all())
        experience_image = process_query(WhyUsImage.objects.all())
        experience_heading = process_query(WhyUsSectionHeading.objects.all())
        experience_points = process_query(WhyUsPoints.objects.all())
        phone_numbers = process_query(PhoneNumbers.objects.all())
        contact_info = process_query(ContactInfo.objects.all())
        
        return Response({
            'status': status.HTTP_200_OK,
            'data': {
                'carousel': home_page_carousel,
                'experience': experience,
                'clients': clients,
                'expertise': expertise,
                'service_cards': service_cards,
                'mission': mission,
                'experience_image': experience_image,
                'experience_heading': experience_heading,
                'experience_points': experience_points,
                'phone_numbers': phone_numbers,
                'contact_info': contact_info
            }
        })

    except Exception as error:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'error': str(error)
        })

@api_view(['GET'])
def footer(request):
    try:
        footer = process_query(Footer.objects.all())
        services = process_query(ServiceCard.objects.all())

        return Response({
            'status': status.HTTP_200_OK,
            'data': {
                'footer': footer,
                'services': services
            }
        })

    except Exception as error:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'error': str(error)
        })

@api_view(['GET'])
def about_us(request):
    try:
        about_page_banner = process_query(AboutPageBanner.objects.all())
        about_page_mission = process_query(AboutPageMission.objects.all())
        about_page_vision = process_query(AboutPageVision.objects.all())

        return Response({
            'status': status.HTTP_200_OK,
            'data': {
                'banner': about_page_banner,
                'mission': about_page_mission,
                'vision': about_page_vision
            }
        })

    except Exception as error:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'error': str(error)
        })

@api_view(['GET'])
def contact_us(request):
    try:
        contact_page_banner = process_query(ContactPageBanner.objects.all())
        phone_numbers = process_query(PhoneNumbers.objects.all())
        contact_info = process_query(ContactInfo.objects.all())

        return Response({
            'status': status.HTTP_200_OK,
            'data': {
                'banner': contact_page_banner,
                'numbers': phone_numbers,
                'contact_info': contact_info
            }
        })

    except Exception as error:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'error': str(error)
        })

@api_view(['GET'])
def service_page(request):
    try:
        service_page_banner = process_query(ServicePageBanner.objects.all())
        service_cards = process_query(ServiceCard.objects.all())

        return Response({
            'status': status.HTTP_200_OK,
            'data': {
                'banner': service_page_banner,
                'cards': service_cards
            }
        })

    except Exception as error:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'error': str(error)
        })

@api_view(['POST'])
def add_subscription(request):
    try:
        if request.method == "POST":
            subscribers = Subscription.objects.all()

            subs = []

            for item in subscribers:
                subs.append(item.subscriber)

            if request.data['email'] in subs:
                return Response({
                    'status': status.HTTP_406_NOT_ACCEPTABLE,
                    'message': "You already subscribed!"
                })
            else:
                print(request.data['email'])
                subscription_ins = Subscription(subscriber = request.data['email'])
                subscription_ins.save()

                return Response({
                    'status': status.HTTP_200_OK,
                    'message': "Thanks for Subscribing!"
                })

    except Exception as error:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'error': str(error)
        })

@csrf_exempt
@api_view(['POST'])
def send_email(request):
    print(request.data['name'])
    print(request.data['number'])
    print(request.data['email'])
    print(request.data['message'])

    try:
        raw_message = f"Name: {request.data['name']}\nEmail: {request.data['email']}\nContact number: {request.data['number']}\n\n{request.data['message']}"

        subject = f"New Message from {request.data['name']}"
        message = raw_message
        from_email = request.data['email']
        recipient_list = ['info@bengaltroopsbd.com']

        send_mail(subject, message, from_email, recipient_list)

        return Response({
            'status': status.HTTP_200_OK,
            'message': 'Mail sent!'
        })
    
    except Exception as error:
        return Response({
            'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
            'message': str(error)
        })