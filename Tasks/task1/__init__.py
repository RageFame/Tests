def optimize_service_center_db(technic):
    customers = {}
    for item in technic:
        tech_name, price, owner_name, phone_number = item
        key = owner_name + ' ' + phone_number
        if key in customers:
            customers[key][tech_name] = price
        else:
            customers[key] = {tech_name: price}

    for key, value in customers.items():
        technic_list = '; '.join([f'{k} - {v}' for k, v in value.items()])
        print(f'{key}: {technic_list}')
