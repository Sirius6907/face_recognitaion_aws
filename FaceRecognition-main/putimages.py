
import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('image_01.jpeg','Chandan Kumar Behera'),
      ('image_02.jpeg','Abinash Behera'),
      ('image_03.jpeg','Akash Kumar Singh'),
      ('image_04.jpeg','Chandan Kumar Behera'),
      ('image_05.jpeg','Abinash Behera'),
      ('image_06.jpeg','Akash Kumar Singh')
     
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('testansarbucket','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})
