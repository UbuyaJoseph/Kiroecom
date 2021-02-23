## E-shop project

### This project simulates an e-commerce platform, with the functionality of a local user (ugandan) being able to purchace a product from an international store ( e.g. eBay) using local currency wallet ( with local currency UGX).

To run this application, follow the steps:( after cloning the repository.)
```
1. pip3 install -r requirements.txt

2. python3 manage.py migrate  (django ORM)

3. python3 manage.py runserver ( development server)

4. gunicorn Estore.wsgi ( running production server)
```