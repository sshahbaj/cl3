import tkinter
from tkinter import *
import os
import boto3


root = tkinter.Tk()

the_lable = Label(root, text="Welcome To AWS app shahbaj")
the_lable.grid()

topFrame = Frame(root,width=500,height=50)
topFrame.grid()

bottomFrame = Frame(root,width=500,height=800)
bottomFrame.grid()

s3 = boto3.resource('s3')

def bucket_create():
    s3.create_bucket(Bucket='mybucket1991996', CreateBucketConfiguration={
    'LocationConstraint': 'ap-south-1'})
    
def get_s3_keys():
    conn = boto3.client('s3')
    for key in conn.list_objects(Bucket='mybucket1991996')['Contents']:
        print(key['Key'])


def list_bucket():
    for bucket in s3.buckets.all():
        print(bucket.name)
    
def store_data():
    bucket_name = 'mybucket1991996'
    data = 'car1.jpg'
    s3.Object(bucket_name, data).put(Body=open(data, 'rb'))

    print('File {} uploaded to {}.'.format(data, bucket_name)) 
    print("\nfile inserted\n")

def remove_bucket():
    bucket_name = 'mybucket1991996'
    bucket = s3.Bucket(bucket_name)
    for key in bucket.objects.all():
        key.delete()
    bucket.delete()
   

button_1 = Button(bottomFrame,text="Create Bucket", fg="green",command = bucket_create)
button_1.grid(row=1,column=1)

lable_2=Label(topFrame,text="To execute ls command on google cloud press ls Botton ")
lable_2.grid(row=3,column=0)
button_2 = Button(bottomFrame,text="ls", fg="green",command = get_s3_keys)
button_2.grid(row=2,column=1)

button_3 = Button(bottomFrame,text="list buckets", fg="green",command = list_bucket)
button_3.grid(row=3,column=1)

button_4 = Button(bottomFrame,text="insert a file into a bucket", fg="green",command = store_data)
button_4.grid(row=4,column=1)

button_5 = Button(bottomFrame,text="remove bucket", fg="green",command = remove_bucket)
button_5.grid(row=5,column=1)

root.mainloop()
