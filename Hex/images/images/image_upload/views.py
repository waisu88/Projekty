from rest_framework import generics, mixins
from rest_framework.response import Response
from .models import Image, Thumbnail, Profile, BinaryImage
from .serializers import ImageSerializer, ThumbnailSerializer, BinaryImageSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from easy_thumbnails.files import get_thumbnailer
from datetime import datetime, timedelta

from rest_framework.views import APIView
from rest_framework.decorators import api_view
import base64
from django.forms.models import model_to_dict


class ImageDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        image_id = self.kwargs['pk']  
        profile = Profile.objects.filter(user=self.request.user)
        return Image.objects.filter(uploaded_by=profile[0], id=image_id) 
           
image_detail_api_view = ImageDetailAPIView.as_view()



class ImageListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        profile = Profile.objects.filter(user=self.request.user)
        return Image.objects.filter(uploaded_by=profile[0])

    
    def perform_create(self, image_serializer):
        profile = Profile.objects.filter(user=self.request.user)[0]
        image_serializer.save(uploaded_by=profile)
        self.create_thumbnails(image_serializer)
        
        
    def get_thumbnail_serializer(self, *args, **kwargs):
        return ThumbnailSerializer(*args, **kwargs)
  

    def create_thumbnails(self, image_serializer):
        base_image = Image.objects.last()
        created_by = base_image.uploaded_by
        granted_tier = created_by.granted_tier
        print(base_image.image.url)
        # thumbnail_serializer = self.get_thumbnail_serializer(data=self.request.data, many=True)
        thumbnail_sizes = []
        if granted_tier.thumbnail_200px:
            thumbnail_sizes.append(200)
        if granted_tier.thumbnail_400px:
            thumbnail_sizes.append(400)    
        if granted_tier.arbitrary_thumbnail_size:
            thumbnail_sizes.append(granted_tier.arbitrary_thumbnail_size)
        for th_size in thumbnail_sizes:        
            thumbnailer = get_thumbnailer(base_image.image)
            th = thumbnailer.get_thumbnail({'size': (th_size, th_size), 'crop': True})
            Thumbnail.objects.create(created_by=created_by, base_image=base_image, thumbnail_image=str(th), thumbnail_size=th_size)

image_list_create_api_view = ImageListCreateAPIView.as_view()

class ThumbnailListAPIView(generics.ListAPIView):    
    serializer_class = ThumbnailSerializer
    permission_classes = [IsAuthenticated]
    # lookup_field = 'pk'


    def get_queryset(self, *args, **kwargs):
        base_image_id = self.kwargs['pk']  
        profile = Profile.objects.filter(user=self.request.user)
        return Thumbnail.objects.filter(created_by=profile[0], base_image=base_image_id)


thumbnail_list_api_view = ThumbnailListAPIView.as_view()




# from sorl.thumbnail import get_thumbnail
# Create your views here.

# @api_view(["GET", "POST"])
# def api_view(request, *args, **kwargs):
    
#     return Response(data)

# class ExpiringLinkAPIView(APIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = ExpiringLinkSerializer

#     def get(self, *args, **kwargs):
#         base_image_id = self.kwargs.get('pk')
#         print(base_image_id)
#         profile = Profile.objects.filter(user=self.request.user)
#         base_image = Image.objects.get(pk=base_image_id)
#         print(base_image)
#         # expiring_links = ExpiringLink.objects.filter(created_by=profile[0], base_image=base_image) 
#         model_data = ExpiringLink.objects.filter(created_by=profile[0], base_image=base_image)
#         print(model_data)
#         print(bool(model_data))
#         if model_data:
#             data = model_to_dict(model_data, fields='__all__')
#             print(data)
#             return Response(data)   
#         return Response({"message": "Expiring link not created yet"})  
#         # return Response(expiring_links)
        

#     def post(self, request, *args, **kwargs):
#         base_image_id = self.kwargs['pk']
#         print(base_image_id)
#         profile = Profile.objects.filter(user=self.request.user)[0]
#         base_image = Image.objects.get(pk=base_image_id)
#         serializer = ExpiringLinkSerializer(data=self.request.data)

#         data = self.request.POST.copy()
#         seconds_to_expiration = self.request.data['seconds_to_expiration']
#         data['created'] = datetime.now()
#         data['expiration_date'] = datetime.now() + timedelta(seconds=int(seconds_to_expiration))
#         # data['base_image'] = base_image
#         # print(profile)
#         # data['created_by'] = profile
#         # print(base_image.id)
#         # print(data)
        
#         # print(serializer)
#         # print("ok")
#         if serializer.is_valid():
            
#             serializer.save(created_by=profile, base_image=base_image)
#             print(serializer.data)
#             print("ok")
#             return Response({"message": "Successfully created"})
#         return Response()
#         #     print(ExpiringLink.objects.last())
#         # cre = ExpiringLink.objects.last().created
#         # exp = ExpiringLink.objects.last().expiration_date
#         # print(cre)
#         # print(exp)
#         # print(cre>exp)
#         # print(cre<exp)

# expiring_link_api_view = ExpiringLinkAPIView.as_view()
# class BinaryImageDetailAPIView(generics.RetrieveAPIView):
#     serializer_class = BinaryImageSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self, *args, **kwargs):
#         # image_id = self.kwargs['pk']  
#         profile = Profile.objects.filter(user=self.request.user)
#         return BinaryImage.objects.first()
           
# binary_image_detail_api_view = BinaryImageDetailAPIView.as_view()


class BinaryImageListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = BinaryImageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        base_image_id = self.kwargs['pk']
        profile = Profile.objects.filter(user=self.request.user)        
        return BinaryImage.objects.filter(created_by=profile[0], base_image=base_image_id) 

    def perform_create(self, serializer):
        base_image_id = self.kwargs['pk']
        profile = Profile.objects.filter(user=self.request.user)[0]
        base_image = Image.objects.get(pk=base_image_id)
        # # serializer = ExpiringLinkSerializer(data=self.request.data)
        # print(serializer)
        data = self.request.POST.copy()
        seconds = self.request.data['seconds_to_expiration']
        serializer.created = datetime.now()
        serializer.expiration_date = datetime.now() + timedelta(seconds=int(seconds))
        # serializer.created_by = profile
        # serializer.base_image = base_image
        print("--------------------------------------------")
        
        
        
        import cv2
        if base_image.image:

            print(base_image.image.url[1:])
            img = cv2.imread("media/uploads/2023/02/18/szymon_8aT7vbZ.JPG")
            down_width = 860
            down_height = 640
            down_points = (down_width, down_height)

            resized_down = cv2.resize(img, down_points, interpolation=cv2.INTER_LINEAR)

            gray = cv2.cvtColor(resized_down, cv2.COLOR_BGR2GRAY)
            ret, tresh1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

            # converting to its binary form
            bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
            cv2.imshow('Binary', gray)
            cv2.waitKey()
        # cv2.imshow('Original image',img)
        # cv2.imshow('Gray image', gray)
        # cv2.waitKey(0)
            cv2.destroyAllWindows()

            filename = 'uploads/binary.png'
            save = cv2.imwrite(filename, tresh1)
            if save:
                print("GREAT!!!!")
            else:
                print('chujnia')
            print(tresh1)
    







        # print(base_image.image)
        # binary_image = base64.b64encode(base_image.image.read())
        # # print(binary_image)
        print("--------------------------------------------")
      
        # print(build_absolute_uri(base_image))
        # data['expiring_link'] = base_image.image.url

        
        if serializer.is_valid():
            
            serializer.save(created_by=profile, base_image=base_image, binary_image=filename)
        #     # urlaa = serializer.data['binary_image']

        #     print("ok")
            return Response({"message": "Successfully created"})
        return Response()
#         #     print(ExpiringLink
        # if serializer.is_valid():
        #     serializer.save(expiration_date=x)
            

        #     # x += timedelta(seconds=seconds)
        #     print(x)
            
        # cre = ExpiringLink.objects.last().created
        # exp = ExpiringLink.objects.last().expiration_date
        # print(cre)
        # print(exp)
        # print(cre>exp)
        # print(cre<exp)
        
        # serializer.save(created_by=profile)




binary_image_list_create_api_view = BinaryImageListCreateAPIView.as_view()





# class ExpiringLinkListCreateAPIView(generics.ListCreateAPIView):
#     serializer_class = ExpiringLinkSerializer
#     permission_classes = [IsAuthenticated]




#     def get_queryset(self, *args, **kwargs):
#         base_image_id = self.kwargs['pk']
#         profile = Profile.objects.filter(user=self.request.user)
#         return ExpiringLink.objects.filter(created_by=profile[0], base_image=base_image_id) 

#     def perform_create(self, serializer):
#         base_image_id = self.kwargs['pk']
#         profile = Profile.objects.filter(user=self.request.user)[0]
#         base_image = Image.objects.get(pk=base_image_id)
#         # serializer = ExpiringLinkSerializer(data=self.request.data)
#         print(serializer)
#         data = self.request.POST.copy()
#         print("--------------------------------------------")
#         import base64
#         print(base_image.image)
#         binary_image = base64.b64encode(base_image.image.read())
#         print(binary_image)
#         print("--------------------------------------------")
#         seconds = self.request.data['seconds_to_expiration']
#         data['created'] = datetime.now()
#         data['expiration_date'] = datetime.now() + timedelta(seconds=int(seconds))
#         data['created_by'] = profile
#         data['base_image'] = base_image
#         # print(build_absolute_uri(base_image))
#         # data['expiring_link'] = base_image.image.url
#         print(data)
#         # serializer = serializer(data=data)
#         # if serializer.is_valid():
#         #     serializer.save(expiration_date=x)
            

#         #     # x += timedelta(seconds=seconds)
#         #     print(x)
            
#         # cre = ExpiringLink.objects.last().created
#         # exp = ExpiringLink.objects.last().expiration_date
#         # print(cre)
#         # print(exp)
#         # print(cre>exp)
#         # print(cre<exp)
        
#         # serializer.save(created_by=profile)
        















# expiring_link_list_create_api_view = ExpiringLinkListCreateAPIView.as_view()












