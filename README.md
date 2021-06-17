# 90724e315a7f18ff327bfe54f9b7c9c0

**Superuser**: admin
**Password**: admin

**User**: guest
**Password**: guest

## Restore DB  
cat *dump_2021-06-17_16_50_32.sql* | docker exec -i *your-db-container* psql -U *your-db-user* -d *your-db-name*