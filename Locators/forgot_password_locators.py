class forgot_password_locators:
    send_code_cta = "//button[text()='Send code']"
    code_fields = "//h2[text()='Enter Code']/parent::div/descendant::input"
    verify_cta = "//button[text()='Verify Code']"

class reset_password_locators:
    confirm_password_field = "confirm_password"
    reset_cta = "//button[text()='Reset Now']"