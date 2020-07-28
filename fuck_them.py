from fk import *
import requests
import os
import random
import string
from datetime import datetime

if __name__ == "__main__":
    input = int(input('Hoe hard wil je hem fucken?'))

    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    random.seed = (os.urandom(1024))

    url = 'https://bitcoin-revolution-appsapp.com/api/v1/register_view'


    for x in range(input):

        first_name = generate_voornaam()
        last_name = generate_achternaam()
        email = generate_email(first_name,last_name)
        phone_number = generate_phone()
        password = generate_password()
        origin_id = generate_origin_id()
        id = genereate_id()

        requests.post(url, allow_redirects=False, data={
            'first_name': first_name,
            'last_name': last_name,
            'email' : generate_email(first_name, last_name),
            'phone_number' : generate_phone(),
            'password' : generate_password(),
            'origin_id' : generate_origin_id(),
            'id' : genereate_id(),

            'broker_name' : "winngroup",
            'country' : "Belgium",
            'currency' : 'EUR',

            # 'subcampaign_id': '40_1416'_ 10239e6fcd74acebd4a3e4dcd1f5a9,
            'activated': random.randint(0,1),
            'amount': '25',
            'was_activated': random.randint(0,1),
            'logged_on': random.randint(0,1),
            'launch': 'bitcoin - revolution - apps',
            'reg_time': str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            'is_new': random.randint(0,1),
            'strategy_id': random.randint(0,10),
            'trades_open': random.randint(0,1000),
            'whiteouted': '1',
            'positions_updated': '',
            'recovery_time': '0000-00-00 00:00:00',
            'product_type': random.randint(0,10),
            'deposit_time': '0000-00-00 00:00:00',
            'deposit_request_limit': '',
            'ftd': '0',
            'demo_mode': '0',
            'demo_mode_date': '0000-00-00 00:00:00',
            'test_action':'',
            'push_date':'',
            'regStatus': 'Active',
            'balance': random.randint(0,9999999),
            'upsellToken': fake.password(length=40, special_chars=False, upper_case=False),
            'currencySign': '€',
            'real_country': 'BE',
            'has_signals': '0',
            'brokerObject[id]': '258',
            'brokerObject[name]': 'winngroup',
            'brokerObject[display_name]': 'WinnGroup',
            'brokerObject[login_url]': 'https: // bots.trafficon.co / api / v1 / login - service?action = auto - login & vendor = winngroup',
            'brokerObject[redirect_param]': 'extRedir',
            'brokerObject[deposit_url]': 'https: // winngroupltd.com / deposit',                                                                                                                                                                              'brokerObject[alternative_deposit_url]': '',
            'brokerObject[trade_url]': '',
            'brokerObject[regulated_status]': '',
            'brokerObject[api_support]': '0',
            'brokerObject[min_deposit_validation]': '250',
            'brokerObject[api_support_us]': '0',
            'brokerObject[login_support_https]': '1',
            'brokerObject[product_type]': '5',
            'brokerObject[sportsbook]': 'false'
            })

        print(f'Sending the fucker {first_name}, {last_name}, {email}')

