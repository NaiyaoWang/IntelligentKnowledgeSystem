CREATE TABLE customers (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    gender CHAR(1),
    phone VARCHAR(20),
    email VARCHAR(100),
    address VARCHAR(100),
    created_at DATE
);

CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    category VARCHAR(30),
    price DECIMAL(10,2),
    stock INT,
    created_at DATE
);

CREATE TABLE orders (
    id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    status VARCHAR(20),
    total_amount DECIMAL(10,2)
);

CREATE TABLE order_items (
    id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    unit_price DECIMAL(10,2),
    amount DECIMAL(10,2)
);

CREATE TABLE categories (
    id INT PRIMARY KEY,
    name VARCHAR(30),
    parent_id INT
);

CREATE TABLE sales (
    id INT PRIMARY KEY,
    product_id INT,
    sale_date DATE,
    quantity INT,
    revenue DECIMAL(10,2)
);

CREATE TABLE staff (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    position VARCHAR(30),
    phone VARCHAR(20),
    email VARCHAR(100)
);

CREATE TABLE store (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    location VARCHAR(100),
    manager_id INT
);

CREATE TABLE inventory (
    id INT PRIMARY KEY,
    store_id INT,
    product_id INT,
    stock INT,
    last_update DATE
);

CREATE TABLE payments (
    id INT PRIMARY KEY,
    order_id INT,
    payment_date DATE,
    method VARCHAR(20),
    amount DECIMAL(10,2)
);


-- customers 表及字段注释
COMMENT ON TABLE customers IS '客户信息表，记录客户基本资料';
COMMENT ON COLUMN customers.id IS '客户ID，主键';
COMMENT ON COLUMN customers.name IS '客户姓名';
COMMENT ON COLUMN customers.gender IS '客户性别（M男 F女）';
COMMENT ON COLUMN customers.phone IS '联系方式';
COMMENT ON COLUMN customers.email IS '电子邮件地址';
COMMENT ON COLUMN customers.address IS '地址';
COMMENT ON COLUMN customers.created_at IS '客户创建时间';

-- products 表及字段注释
COMMENT ON TABLE products IS '产品信息表，记录销售产品明细';
COMMENT ON COLUMN products.id IS '产品ID，主键';
COMMENT ON COLUMN products.name IS '产品名称';
COMMENT ON COLUMN products.category IS '产品所属类别';
COMMENT ON COLUMN products.price IS '单价';
COMMENT ON COLUMN products.stock IS '库存数量';
COMMENT ON COLUMN products.created_at IS '产品录入时间';

-- orders 表及字段注释
COMMENT ON TABLE orders IS '订单信息表';
COMMENT ON COLUMN orders.id IS '订单ID，主键';
COMMENT ON COLUMN orders.customer_id IS '客户ID，外键，关联customers表';
COMMENT ON COLUMN orders.order_date IS '下单日期';
COMMENT ON COLUMN orders.status IS '订单状态';
COMMENT ON COLUMN orders.total_amount IS '订单总金额';

-- order_items 表及字段注释
COMMENT ON TABLE order_items IS '订单明细表，记录每个订单包含的产品';
COMMENT ON COLUMN order_items.id IS '订单明细ID，主键';
COMMENT ON COLUMN order_items.order_id IS '订单ID，外键，关联orders表';
COMMENT ON COLUMN order_items.product_id IS '产品ID，外键，关联products表';
COMMENT ON COLUMN order_items.quantity IS '购买数量';
COMMENT ON COLUMN order_items.unit_price IS '成交单价';
COMMENT ON COLUMN order_items.amount IS '小计金额';

-- categories 表及字段注释
COMMENT ON TABLE categories IS '产品类别表';
COMMENT ON COLUMN categories.id IS '类别ID，主键';
COMMENT ON COLUMN categories.name IS '类别名称';
COMMENT ON COLUMN categories.parent_id IS '父类别ID';

-- sales 表及字段注释
COMMENT ON TABLE sales IS '产品销售记录表';
COMMENT ON COLUMN sales.id IS '销售记录ID，主键';
COMMENT ON COLUMN sales.product_id IS '产品ID';
COMMENT ON COLUMN sales.sale_date IS '销售日期';
COMMENT ON COLUMN sales.quantity IS '销售数量';
COMMENT ON COLUMN sales.revenue IS '销售收入';

-- staff 表及字段注释
COMMENT ON TABLE staff IS '员工信息表';
COMMENT ON COLUMN staff.id IS '员工ID，主键';
COMMENT ON COLUMN staff.name IS '员工姓名';
COMMENT ON COLUMN staff.position IS '职位名称';
COMMENT ON COLUMN staff.phone IS '联系电话';
COMMENT ON COLUMN staff.email IS '电子邮件';

-- store 表及字段注释
COMMENT ON TABLE store IS '门店信息表';
COMMENT ON COLUMN store.id IS '门店ID，主键';
COMMENT ON COLUMN store.name IS '门店名称';
COMMENT ON COLUMN store.location IS '门店位置';
COMMENT ON COLUMN store.manager_id IS '门店经理ID，关联staff表';

-- inventory 表及字段注释
COMMENT ON TABLE inventory IS '库存信息表，按门店统计库存';
COMMENT ON COLUMN inventory.id IS '库存ID，主键';
COMMENT ON COLUMN inventory.store_id IS '门店ID';
COMMENT ON COLUMN inventory.product_id IS '产品ID';
COMMENT ON COLUMN inventory.stock IS '库存数量';
COMMENT ON COLUMN inventory.last_update IS '最后更新时间';

-- payments 表及字段注释
COMMENT ON TABLE payments IS '订单支付信息表';
COMMENT ON COLUMN payments.id IS '支付ID，主键';
COMMENT ON COLUMN payments.order_id IS '订单ID，外键';
COMMENT ON COLUMN payments.payment_date IS '支付日期';
COMMENT ON COLUMN payments.method IS '支付方式';
COMMENT ON COLUMN payments.amount IS '支付金额';