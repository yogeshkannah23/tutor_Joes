from django.core.management.base import BaseCommand
from shop.models import Product
from typing import Any
import pandas as pd
import random


class Command(BaseCommand):

    help = "this will insert the post data"

    def handle(self,*args:Any,**options:Any):

        df=pd.read_excel(r"C:\Users\kanni\OneDrive\Desktop\New folder\products.xlsx")
        print(df)
        print(df.shape)
        df=df.drop("Serial Number",axis=1)
        print(df)
        print(df.shape)
        
        # for product_name,category,old_price,new_price,description,seller,image_url in df:
        #     Product.objects.create(name=product_name,product_image=image_url,quantity=self.get_rand(1,10),original_price=old_price,selling_price=new_price,description=description,status=self.get_rand(0,1),vendor=seller,trending=self.get_rand(0,1),category=category)

        # self.stdout.write(self.style.SUCCESS("Data inserted"))
        for index,row in df.iterrows():
            Product.objects.create(name=row["Product Name"],product_image=row["Image URL"],quantity=self.get_rand(1,10),original_price=row["Old Price"],selling_price=row["New Price"],description=row["Description"],status=self.get_rand(0,1),vendor=row["Seller"],trending=self.get_rand(0,1))

        self.stdout.write(self.style.SUCCESS("Data inserted"))
       

    def get_rand(self,x,y):
        # Generate a random number between 1 and 10
        random_number = random.randint(x, y)
        # Print the random number
        return random_number
