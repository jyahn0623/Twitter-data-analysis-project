from django.test import TestCase

# Create your tests here.

a = {
    'test' : {

    },
}

a['test']['hi'] = ['김밥', '안주영']
print(a['test'].keys())
