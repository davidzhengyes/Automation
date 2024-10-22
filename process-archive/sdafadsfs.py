from seleniumbase import SB

with SB(uc=True) as sb:
    sb.driver.uc_open_with_reconnect(
        "https://visa.vfsglobal.com/are/en/fra/login",
        reconnect_time=12
    )

print("DRIVER RECON")