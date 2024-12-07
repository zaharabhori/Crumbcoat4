from django.shortcuts import render
from django.http import HttpResponse
import boto3
from django.shortcuts import render
# Create your views here.

def index(request):
    return HttpResponse("Hello World")



# AWS S3 configurations
AWS_S3_BUCKET_NAME = 'crumbcoat.bucket'  # Replace with your bucket name
AWS_REGION = 'ap-south-1'              # Replace with your region (e.g., 'us-east-1')

def gallery_view(request):
    # Create an S3 client
    s3_client = boto3.client('s3', region_name=AWS_REGION)

    # List objects in the bucket
    response = s3_client.list_objects_v2(Bucket=AWS_S3_BUCKET_NAME, Prefix='pics/')
    
    # Extract image URLs
    images = []
    if 'Contents' in response:
        for obj in response['Contents']:
            image_url = f"https://{AWS_S3_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/{obj['Key']}"
            # Optional: Use folder-based filtering if needed
            images.append({'url': image_url, 'key': obj['Key']})
    
    # Pass the image URLs to the template
    return render(request, 'gallery.html', {'images': images})