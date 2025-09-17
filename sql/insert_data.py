import psycopg2
import logging
from tqdm import tqdm

# 日志配置
logging.basicConfig(
    filename='sql_exec_progress.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    encoding='utf-8'
)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

def execute_sql_file(filename, conn):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    total = len(lines)
    cur = conn.cursor()
    success, failed = 0, 0
    for idx, line in tqdm(enumerate(lines, start=1)):
        sql = line.strip()
        if not sql or sql.startswith('--'):
            continue
        try:
            cur.execute(sql)
            conn.commit()
            success += 1
            # 可调整展示频率，有日志文件也便于追踪后台进度
            if idx % 100 == 0 or idx == total:
                logging.info(f"已执行 {idx}/{total} 条SQL (成功:{success}, 失败:{failed})")
        except Exception as e:
            conn.rollback()
            failed += 1
            logging.error(f"第{idx}条SQL执行失败: {e}\nSQL: {sql}")

    logging.info(f"SQL执行完毕。总计:{total}，成功:{success}，失败:{failed}")
    cur.close()

if __name__ == '__main__':
    host = '192.168.0.25'
    port = 8432
    user = 'admin'
    password = 'secret'
    dbname = 'mydatabase'
    sql_file = 'insert_all_tables.sql'  # 刚才生成的大 SQL 文件

    logging.info(f"连接数据库 {host}:{port} 用户:{user}")
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            dbname=dbname
        )
        logging.info("数据库连接成功，准备执行SQL文件...")
        execute_sql_file(sql_file, conn)
        conn.close()
        logging.info("数据库连接关闭。")
    except Exception as e:
        logging.error(f"数据库连接失败: {e}")

