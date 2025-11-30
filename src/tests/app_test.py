import unittest
from app import app, store


class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        store.warehouses.clear()
        store._next_id = 1

    def test_index_empty(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Warehouses', response.data)
        self.assertIn(b'No warehouses yet', response.data)

    def test_create_warehouse_get(self):
        response = self.client.get('/warehouse/create')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Create New Warehouse', response.data)

    def test_create_warehouse_post(self):
        response = self.client.post(
            '/warehouse/create',
            data={'name': 'Test Warehouse'},
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Warehouse', response.data)

    def test_view_warehouse(self):
        store.add_warehouse('My Warehouse')
        response = self.client.get('/warehouse/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'My Warehouse', response.data)

    def test_view_nonexistent_warehouse_redirects(self):
        response = self.client.get('/warehouse/999')
        self.assertEqual(response.status_code, 302)

    def test_edit_warehouse_get(self):
        store.add_warehouse('Original Name')
        response = self.client.get('/warehouse/1/edit')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Original Name', response.data)

    def test_edit_warehouse_post(self):
        store.add_warehouse('Original Name')
        response = self.client.post(
            '/warehouse/1/edit',
            data={'name': 'New Name'},
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'New Name', response.data)

    def test_delete_warehouse(self):
        store.add_warehouse('To Delete')
        response = self.client.post(
            '/warehouse/1/delete',
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'No warehouses yet', response.data)

    def test_add_product_get(self):
        store.add_warehouse('Test Warehouse')
        response = self.client.get('/warehouse/1/product/add')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Add Product', response.data)

    def test_add_product_post(self):
        store.add_warehouse('Test Warehouse')
        response = self.client.post(
            '/warehouse/1/product/add',
            data={'name': 'Test Product', 'price': '10.99', 'quantity': '5'},
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Product', response.data)
        self.assertIn(b'10.99', response.data)

    def test_edit_product_get(self):
        warehouse = store.add_warehouse('Test Warehouse')
        warehouse.add_product('Original Product', 5.0, 10)
        response = self.client.get('/warehouse/1/product/1/edit')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Original Product', response.data)

    def test_edit_product_post(self):
        warehouse = store.add_warehouse('Test Warehouse')
        warehouse.add_product('Original Product', 5.0, 10)
        response = self.client.post(
            '/warehouse/1/product/1/edit',
            data={'name': 'Updated Product', 'price': '15.99', 'quantity': '20'},
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Updated Product', response.data)

    def test_delete_product(self):
        warehouse = store.add_warehouse('Test Warehouse')
        warehouse.add_product('To Delete', 5.0, 10)
        response = self.client.post(
            '/warehouse/1/product/1/delete',
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'No products in this warehouse', response.data)
