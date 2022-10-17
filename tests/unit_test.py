from  unittest import TestCase
from models import Property

class TestUtils(TestCase):

    def setUp(self):
        self.data = {'status': ['pre_venta'], 'city': ['bogota']}
        self.property = Property()

    def test_get_properties_with_data(self):
        result = self.property.get_property_by_state(self.data)
        self.assertTrue(result)

    def test_get_properties_without_data(self):
        result = self.property.get_property_by_state({})
        self.assertFalse(result)

    def test_get_properties_without_status(self):
        self.data.pop('status')
        result = self.property.get_property_by_state({})
        self.assertFalse(result)