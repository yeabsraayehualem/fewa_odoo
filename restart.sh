clear
docker compose down && docker compose up -d --build
sleep 2
docker exec -it fewa_odoo tail -f /etc/odoo/odoo-server.log