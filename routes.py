from flask import Blueprint, render_template, redirect, url_for, request
from models import Product, db, User
from flask_login import login_required, current_user
import coinbase_commerce

main_bp = Blueprint('main', __name__)

client = coinbase_commerce.Client(api_key=os.getenv('COINBASE_API_KEY'))

@main_bp.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@main_bp.route('/sell', methods=['GET', 'POST'])
@login_required
def sell():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        price = request.form.get('price')
        download_link = request.form.get('download_link')
        
        product = Product(title=title, description=description, price=price, download_link=download_link, user_id=current_user.id)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('main.index'))
    
    return render_template('sell.html')

@main_bp.route('/product/<int:product_id>')
def product(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product.html', product=product)

@main_bp.route('/buy/<int:product_id>', methods=['POST'])
@login_required
def buy(product_id):
    product = Product.query.get_or_404(product_id)
    charge_data = {
        'name': product.title,
        'description': product.description,
        'pricing_type': 'fixed_price',
        'local_price': {
            'amount': product.price,
            'currency': 'BTC'
        },
        'metadata': {
            'user_id': current_user.id,
            'product_id': product.id
        },
        'redirect_url': url_for('main.success', product_id=product.id, _external=True),
        'cancel_url': url_for('main.index', _external=True)
    }
    
    charge = client.charge.create(**charge_data)
    
    return redirect(charge['hosted_url'])

@main_bp.route('/success/<int:product_id>')
@login_required
def success(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('success.html', product=product)
