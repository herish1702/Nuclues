from Data.Static_Data import static_data

class queries:
    get_otp_query = f"SELECT otp FROM user_info WHERE user_info.email = '{static_data.email}' ORDER BY created_at DESC LIMIT 1;"
