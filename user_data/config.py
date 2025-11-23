# maximum number of retry attempts on errors
max_retries = 5

# mobile proxy for interaction with aztecscan and dashtec to avoid rate limits
# you can buy mobile/residential proxies here: https://proxyshard.com?ref=cyberomanov
# if you don't want to use proxy, you can leave this setting as is or fill with empty string
mobile_proxy = "socks5://m903669_gmail_com-country-de-type-mobile-ipv4-true-sid-5d9df5b4ac4c4-ttl-1m-filter-medium:kq0sgdiyjn@gate.nodemaven.com:1080"
# mobile_proxy = "http://log:pass@ip:port"
# mobile_proxy = ""

# sleep in seconds between account checks
sleep_between_accs = (60, 100)
# sleep in seconds between cycles
sleep_between_loop = (600, 1000)

# telegram notifications: True / False
enable_telegram_notifications = True
# telegram bot API key
bot_api_key = "8518995444:AAEKvdg24Ac4-4kLYSV3pi_e_oHhpnV-7Vs"
# chat ID where to send notifications for critical metrics
alarm_chat_id = "257319019"

# minimum required attestation success rate (%).
# if the rate falls below this threshold, an alarm will be triggered.
attestation_success_threshold = 100# copy and configure parameters from example: 'user_data/config-example.py'.
# do not modify 'user_data/config-example.py' file to avoid issues with software version updates.
