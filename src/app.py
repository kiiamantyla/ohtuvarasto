from flask import Flask, render_template, request, redirect, url_for
from models import WarehouseStore

app = Flask(__name__)
store = WarehouseStore()


@app.route('/')
def index():
    warehouses = store.get_all_warehouses()
    return render_template('index.html', warehouses=warehouses)


@app.route('/warehouse/create', methods=['GET', 'POST'])
def create_warehouse():
    if request.method == 'POST':
        name = request.form['name']
        store.add_warehouse(name)
        return redirect(url_for('index'))
    return render_template('create_warehouse.html')


@app.route('/warehouse/<int:warehouse_id>')
def view_warehouse(warehouse_id):
    warehouse = store.get_warehouse(warehouse_id)
    if not warehouse:
        return redirect(url_for('index'))
    return render_template('view_warehouse.html', warehouse=warehouse)


@app.route('/warehouse/<int:warehouse_id>/edit', methods=['GET', 'POST'])
def edit_warehouse(warehouse_id):
    warehouse = store.get_warehouse(warehouse_id)
    if not warehouse:
        return redirect(url_for('index'))
    if request.method == 'POST':
        warehouse.name = request.form['name']
        return redirect(url_for('view_warehouse', warehouse_id=warehouse_id))
    return render_template('edit_warehouse.html', warehouse=warehouse)


@app.route('/warehouse/<int:warehouse_id>/delete', methods=['POST'])
def delete_warehouse(warehouse_id):
    store.delete_warehouse(warehouse_id)
    return redirect(url_for('index'))


@app.route('/warehouse/<int:warehouse_id>/product/add', methods=['GET', 'POST'])
def add_product(warehouse_id):
    warehouse = store.get_warehouse(warehouse_id)
    if not warehouse:
        return redirect(url_for('index'))
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])
        warehouse.add_product(name, price, quantity)
        return redirect(url_for('view_warehouse', warehouse_id=warehouse_id))
    return render_template('add_product.html', warehouse=warehouse)


@app.route(
    '/warehouse/<int:warehouse_id>/product/<int:product_id>/edit',
    methods=['GET', 'POST']
)
def edit_product(warehouse_id, product_id):
    warehouse = store.get_warehouse(warehouse_id)
    if not warehouse:
        return redirect(url_for('index'))
    product = warehouse.get_product(product_id)
    if not product:
        return redirect(url_for('view_warehouse', warehouse_id=warehouse_id))
    if request.method == 'POST':
        product.name = request.form['name']
        product.price = float(request.form['price'])
        product.quantity = int(request.form['quantity'])
        return redirect(url_for('view_warehouse', warehouse_id=warehouse_id))
    return render_template(
        'edit_product.html', warehouse=warehouse, product=product
    )


@app.route(
    '/warehouse/<int:warehouse_id>/product/<int:product_id>/delete',
    methods=['POST']
)
def delete_product(warehouse_id, product_id):
    warehouse = store.get_warehouse(warehouse_id)
    if warehouse:
        warehouse.delete_product(product_id)
    return redirect(url_for('view_warehouse', warehouse_id=warehouse_id))


if __name__ == '__main__':
    app.run(debug=True)
