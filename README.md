# 90724e315a7f18ff327bfe54f9b7c9c0

## Build and run  
docker-compose build --no-cache  
docker-compose up

## Restore DB  
cat *dump_2021-06-17_16_50_32.sql* | docker exec -i *test-task_db_1* psql -U *postgres* -d *postgres*

## User info  
**Superuser**: admin
**Password**: admin

**User**: guest
**Password**: guest
