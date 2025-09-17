import random
from datetime import datetime, timedelta

def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return (start + timedelta(days=random_days)).strftime('%Y-%m-%d')

with open('insert_all_tables.sql', 'w', encoding='utf-8') as f:

    # customers 表（100条）
    for i in range(1, 101):
        name = f'客户{i}'
        gender = 'M' if i % 2 == 1 else 'F'
        phone = f'1380000{str(i).zfill(4)}'
        email = f'user{i}@test.com'
        address = f'城市{random.randint(1, 20)}区{random.choice("ABCD")}'
        created_at = random_date(datetime(2022,1,1), datetime(2022,12,31))
        sql = f"INSERT INTO customers VALUES ({i}, '{name}', '{gender}', '{phone}', '{email}', '{address}', '{created_at}');\n"
        f.write(sql)

    # products 表（100条）
    categories = ['手机', '笔记本', '手表', '平板', '配件', '家电', '音响', '耳机', '显示器', '路由器']
    for i in range(1, 101):
        name = f'产品{i}'
        category = categories[i % len(categories)]
        price = round(random.uniform(200, 20000), 2)
        stock = random.randint(10, 200)
        created_at = random_date(datetime(2022,1,1), datetime(2022,12,31))
        sql = f"INSERT INTO products VALUES ({i}, '{name}', '{category}', {price}, {stock}, '{created_at}');\n"
        f.write(sql)

    # orders 表（100条）
    statuses = ['已支付', '已取消', '待支付']
    for i in range(1, 101):
        customer_id = random.randint(1, 100)
        order_date = random_date(datetime(2023,1,1), datetime(2023,6,30))
        status = statuses[i % len(statuses)]
        total_amount = round(random.uniform(100, 50000), 2)
        sql = f"INSERT INTO orders VALUES ({i}, {customer_id}, '{order_date}', '{status}', {total_amount});\n"
        f.write(sql)

    # order_items 表（5000条）
    for i in range(1, 5001):
        order_id = random.randint(1, 100)
        product_id = random.randint(1, 100)
        quantity = random.randint(1, 10)
        unit_price = round(random.uniform(100, 20000), 2)
        amount = round(unit_price * quantity, 2)
        sql = f"INSERT INTO order_items VALUES ({i}, {order_id}, {product_id}, {quantity}, {unit_price}, {amount});\n"
        f.write(sql)

    # categories 表（100条）
    cat_names = ['手机', '笔记本', '手表', '平板', '配件', '家用电器', '办公设备', '耳机', '显示器',
                 '打印机', '移动电源', '智能音响', '键盘', '鼠标', '网络设备', '路由器', '内存条', '硬盘', '主板', '显卡']
    for i in range(1, 101):
        name = f"{cat_names[i % len(cat_names)]}{(i - 1) // len(cat_names) + 1}"
        parent_id = 'NULL'
        sql = f"INSERT INTO categories VALUES ({i}, '{name}', {parent_id});\n"
        f.write(sql)

    # sales 表（5000条）
    for i in range(1, 5001):
        product_id = random.randint(1, 100)
        sale_date = random_date(datetime(2023,1,1), datetime(2023,6,30))
        quantity = random.randint(1, 10)
        revenue = round(random.uniform(100, 20000), 2) * quantity
        sql = f"INSERT INTO sales VALUES ({i}, {product_id}, '{sale_date}', {quantity}, {revenue});\n"
        f.write(sql)

    # staff 表（100条）
    positions = ['销售经理', '财务主管', '门店店员', '门店经理']
    for i in range(1, 101):
        name = f'员工{i}'
        position = positions[i % len(positions)]
        phone = f'1370000{str(i).zfill(4)}'
        email = f'staff{i}@test.com'
        sql = f"INSERT INTO staff VALUES ({i}, '{name}', '{position}', '{phone}', '{email}');\n"
        f.write(sql)

    # store 表（100条）
    for i in range(1, 101):
        name = f"门店{i}"
        location = f"城市{random.randint(1, 20)}区{random.choice('ABCD')}"
        manager_id = random.randint(1, 100)
        sql = f"INSERT INTO store VALUES ({i}, '{name}', '{location}', {manager_id});\n"
        f.write(sql)

    # inventory 表（5000条）
    for i in range(1, 5001):
        store_id = random.randint(1, 100)
        product_id = random.randint(1, 100)
        stock = random.randint(0, 300)
        last_update = random_date(datetime(2023,1,1), datetime(2023,6,30))
        sql = f"INSERT INTO inventory VALUES ({i}, {store_id}, {product_id}, {stock}, '{last_update}');\n"
        f.write(sql)

    # payments 表（5000条）
    methods = ['信用卡', '支付宝', '微信', '现金']
    for i in range(1, 5001):
        order_id = random.randint(1, 100)
        payment_date = random_date(datetime(2023,1,1), datetime(2023,6,30))
        method = methods[i % len(methods)]
        amount = round(random.uniform(100, 50000), 2)
        sql = f"INSERT INTO payments VALUES ({i}, {order_id}, '{payment_date}', '{method}', {amount});\n"
        f.write(sql)

print("All SQL insert data generated successfully in insert_all_tables.sql!")
