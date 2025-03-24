from Data.Dynamic_Data import dynamic_data


class tenant_locators:
    add_tenant_cta = "//button[text()='Tenant']"

class create_new_tenant_locators:
    tenant_name = "//input[@placeholder='Tenant Name']"
    tenant_prefix = "//input[@placeholder='Tenant Prefix']"
    company_name = "//input[@placeholder='Company Name']" 
    email = "//input[@placeholder='Email Address']"
    address = "//input[@placeholder='Address']"
    appartment = "//input[@placeholder='Flat / Apartment / Suite']"
    country_drop_down = "country"
    country_option = f"//option[text()='{dynamic_data.country}']"
    state_drop_down = "state"
    state_option = f"//option[text()='{dynamic_data.state}']"
    zip_code = "//input[@placeholder='Zip Code']"
    status_drop_down = "status"
    status_option = "//option[text()='NEW']" 
    profile_field = "//input[@name='file']"
    create_cta = "//button[text()='Create New']"
    reset_cta = "//button[text()='Reset']"

