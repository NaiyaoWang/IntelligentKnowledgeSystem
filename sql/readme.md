### postgres install
docker run -d   --name postgres-container   -e POSTGRES_USER=admin   -e POSTGRES_PASSWORD=secret   -e POSTGRES_DB=mydatabase   -p 8432:5432  --name postgres_sqlbot postgres

### SQLBot install
docker run -d \
    --name sqlbot \
    --restart unless-stopped \
    -p 8000:8000 \
    -p 8001:8001 \
    -v ./data/sqlbot/excel:/opt/sqlbot/data/excel \
    -v ./data/sqlbot/images:/opt/sqlbot/images \
    -v ./data/sqlbot/logs:/opt/sqlbot/logs \
    -v ./data/postgresql:/var/lib/postgresql/data \
    --privileged=true \
    dataease/sqlbot

### Simulate Data

run create_table.sql, 这句不是代码，手动跑即可

python insert_sql.py
python insert_data.py

### 参考资料
https://dataease.cn/sqlbot/v1/installation/online_installtion/#3