SELECT * FROM clients;


SELECT clients.first_name, clients.last_name, billing.amount, billing.charged_datetime
FROM clients
JOIN billing ON clients.id = billing.clients_id;

SELECT sites.domain_name, leads.first_name, leads.last_name
FROM sites
JOIN leads ON sites.id = leads.sites_id;


SELECT clients.first_name AS clients_first, clients.last_name, sites.domain_name AS url, leads.first_name
FROM clients
JOIN sites ON clients.id = sites.clients_id
JOIN leads ON sites.id = leads.sites_id;

SELECT clients.first_name, clients.last_name, SUM(billing.amount) AS Total
FROM clients
JOIN billing ON clients.id = billing.clients_id
GROUP BY clients.id;

SELECT clients.first_name, clients.last_name, MAX(billing.amount) , leads.email
FROM clients
JOIN billing ON clients.id = billing.clients_id
JOIN sites ON sites.clients_id = clients.id
JOIN leads ON sites.id = leads.sites_id
GROUP BY clients.id;

SELECT GROUP_CONCAT('  ',sites.domain_name), clients.first_name, clients.last_name
FROM clients
JOIN sites ON clients.id = sites.clients_id
GROUP BY clients.id; 

SELECT (leads.id), sites.domain_name, leads.email
FROM sites
JOIN leads ON sites.id = leads.sites_id
GROUP BY sites.id;



