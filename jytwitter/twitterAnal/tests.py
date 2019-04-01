from django.test import TestCase

# Create your tests here.

a = {'a' : 1, 'b' : 2 }

if not 'b' in a.keys():
    print('hi')
    a['b'] = 1
