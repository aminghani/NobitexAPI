import requests


class Nobitex:
    '''python package for nobitex api'''

    __BASE_URL = 'https://api.nobitex.ir/'

    def __init__(self, username, password):
        self.token = self.__auth(username, password)

    def __auth(self, username, password, remember=False):
        url = self.__BASE_URL + "auth/login/"

        payload = {'username': username,
                   'password': password,
                   'captcha': 'api',
                   'remember': 'yes' if remember is True else 'no'}

        respond = requests.request("POST", url, data=payload)

        return respond.json()['key']

    def order_book(self, symbol):
        """برای دریافت لیست سفارشات از این نوع درخواست استفاده نمایید"""

        url = self.__BASE_URL + 'v2/orderbook'

        payload = {'symbol': symbol}

        response = requests.request("POST", url, data=payload)

        return response.json()

    def trades(self, symbol):
        """برای دریافت لیست معاملات از این نوع درخواست استفاده نمایید"""

        url = self.__BASE_URL + 'v2/trades'

        payload = {'symbol': symbol}

        response = requests.request("POST", url, data=payload)

        return response.json()

    def market_stats(self, src_currency, dst_currency):
        """برای دریافت آخرین آمار بازار نوبیتکس از این نوع درخواست استفاده نمایید"""

        url = self.__BASE_URL + 'market/stats'

        payload = {'srcCurrency': src_currency,
                   'dstCurrency': dst_currency
                   }

        response = requests.request("POST", url, data=payload)

        return response.json()

    def ohlc(self, symbol, from_date, to_date, resolution='D'):
        """برای دریافت آمار OHLC نوبیتکس از این نوع درخواست استفاده نمایید"""

        url = self.__BASE_URL + 'market/udf/history'

        payload = {'symbol': symbol,
                   'resolution': resolution,
                   'from': from_date,
                   'to': to_date
                   }

        response = requests.request("GET", url, data=payload)

        return response.json()

    def global_market_stats(self):
        """برای دریافت آمار بازارهای جهانی از این نوع درخواست استفاده نمایید"""

        url = self.__BASE_URL + 'market/global-stats'

        response = requests.request("POST", url)

        return response.json()

    def user_profile(self):
        """برای دریافت پروفایل کاربر از این نوع درخواست استفاده نمایید"""

        url = self.__BASE_URL + 'users/profile'

        headers = {
            'Authorization': 'Token ' + self.token
        }

        response = requests.request("GET", url, headers=headers)

        return response.json()

    def login_attempts(self):
        """برای دریافت سابقه ورود از این نوع درخواست استفاده نمایید"""

        url = self.__BASE_URL + 'users/login-attempts'

        headers = {
            'Authorization': 'Token ' + self.token
        }

        response = requests.request("GET", url, headers=headers)

        return response.json()

    def referral_code(self):
        url = self.__BASE_URL + 'users/get-referral-code'

        headers = {
            'Authorization': 'Token ' + self.token
        }

        response = requests.request("GET", url, headers=headers)

        return response.json()

    def add_card(self, number, bank):
        """برای افزودن کارت بانکی جدید از این نوع درخواست استفاده نمایید"""

        url = self.__BASE_URL + 'users/cards-add'

        payload = {'number': number,
                   'bank': bank}

        headers = {
            'Authorization': 'Token ' + self.token
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()

    def add_account(self, number, shaba, bank):
        """برای افزودن حساب بانکی جدید از این نوع درخواست استفاده نمایید"""

        url = self.__BASE_URL + 'users/accounts-add'

        payload = {'number': number,
                   'shaba': shaba,
                   'bank': bank}

        headers = {
            'Authorization': 'Token ' + self.token
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()

    def user_limit(self):
        """برای دریافت محدودیت های کاربر از این نوع درخواست استفاده نمایید"""

        url = self.__BASE_URL + 'users/limitations'

        headers = {
            'Authorization': 'Token ' + self.token
        }

        response = requests.request("POST", url, headers=headers)

        return response.json()

    def wallet_list(self):
        """برای دریافت لیست کیف پول های کاربر از این نوع درخواست استفاده نمایید"""

        url = self.__BASE_URL + 'users/wallets/list'

        headers = {
            'Authorization': 'Token ' + self.token
        }

        response = requests.request("POST", url, headers=headers)

        return response.json()

    def balance(self, currency):
        """برای دریافت موجودی کیف پول های خود در نوبیتکس (شامل کیف پول ریالی و کیف پول های رمز ارزی) از این نوع
        درخواست استفاده نمایید """

        url = self.__BASE_URL + 'users/wallets/balance'

        payload = {'currency': currency}

        headers = {
            'Authorization': 'Token ' + self.token
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()

    def transaction_list(self, wallet):
        """برای دریافت لیست تراکنش های کیف پولتان از این تابع استفاده کنید"""

        url = self.__BASE_URL + 'users/wallets/transactions/list'

        payload = {'wallet': wallet}

        headers = {
            'Authorization': 'Token ' + self.token
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()

    def wallet_info(self, wallet):
        """برای دریافت لیست واریزها و برداشت‌ها از این نوع درخواست استفاده نمایید"""

        url = self.__BASE_URL + 'users/wallets/deposits/list'

        payload = {'wallet': wallet}

        headers = {
            'Authorization': 'Token ' + self.token
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()

    def generate_address(self, wallet):
        """برای تولید آدرس بلاکچین از این نوع درخواست استفاده نمایید"""

        url = self.__BASE_URL + 'users/wallets/generate-address'

        payload = {'wallet': wallet}

        headers = {
            'Authorization': 'Token ' + self.token
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()

    def add_order(self, type, execution, src_currency, dst_currency, amount, price):
        """برای ثبت سفارش معامله در بازار نوبیتکس از این درخواست استفاده نمایید.
        ثبت سفارش الزاماً به معنی انجام معامله نیست و بسته به نوع و قیمت سفارش و وضعیت لحظه‌ای بازار ممکن است معامله انجام
شود یا نشود. با درخواست «وضعیت سفارش» می‌توانید از وضعیت سفارش خود مطلع شوید.
سفارش‌ها پس از ثبت، پیش از ورود به دفتر معاملاتی و انجام معامله، مجدداً از نظر اعتبار مورد بررسی قرار گرفته و در صورت
        نامعتبر بودن، به وضعیت «رد شده» برده خواهند شد. به همین علت در صورتی که سفارش‌های شما ثبت می‌شود ولی بلافاصله به
        وضعیت «رد شده» تغییر حالت پیدا می‌کنند، پارامترهای ارسالی خود به ویژه مقدار و قیمت سفارش و موجودی حساب خود را دقیق‌تر
        بررسی نمایید """

        url = self.__BASE_URL + 'market/orders/add'

        payload = {'type': type,
                   'execution': execution,
                   'srcCurrency': src_currency,
                   'dstCurrency': dst_currency,
                   'amount': amount,
                   'price': price
                   }

        headers = {
            'Authorization': 'Token ' + self.token
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()

    def order_status(self, id):
        """برای دریافت وضعیت سفارش از این نوع درخواست استفاده نمایید"""

        url = self.__BASE_URL + 'market/orders/status'

        payload = {'id': id}

        headers = {
            'Authorization': 'Token ' + self.token
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()

    def orders_list(self, status, type, src_currency, dst_currency, details):
        """برای دریافت فهرست سفارش‌های خود، از این درخواست استفاده نمایید"""

        url = self.__BASE_URL + 'market/orders/list'

        payload = {'status': status,
                   'type': type,
                   'srcCurrency': src_currency,
                   'dstCurrency': dst_currency,
                   'details': details
                   }

        headers = {
            'Authorization': 'Token ' + self.token
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()

    def update_status(self, order, status):
        """برای به روزرسانی سفارش از این تابع استفاده کنید"""

        url = self.__BASE_URL + 'market/orders/update-status'

        payload = {'order': order,
                   'status': status}

        headers = {
            'Authorization': 'Token ' + self.token
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()

    def cancel_order(self, hours, execution, src_currency, dst_currency):
        """برای لغو سفارش از این تابع استفاده کنید"""

        url = self.__BASE_URL + 'market/orders/cancel-old'

        payload = {'hours': hours,
                   'execution': execution,
                   'srcCurrency': src_currency,
                   'dstCurrency': dst_currency}

        headers = {
            'Authorization': 'Token ' + self.token
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()

    def link_lists(self, links):
        """برای دریافت فهرست کد های دعوت از این تابع استفاده کنید"""

        url = self.__BASE_URL + 'users/referral/links-list'

        payload = {'links': links}

        headers = {
            'Authorization': 'Token ' + self.token
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()

    def link_add(self, friend_share):
        """برای ایجاد یک کد دعوت جدید برای کاربر، از «ایجاد کد دعوت» استفاده نمایید"""

        url = self.__BASE_URL + 'users/referral/links-add'

        payload = {'links': friend_share}

        headers = {
            'Authorization': 'Token ' + self.token
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()

    def referral_status(self, has_referrer):
        """برای اطلاع از این که کاربر فعلی توسط کاربر دیگری به نوبیتکس دعوت شده است یا خیر، از «وضعیت دعوت کاربر»
        استفاده نمایید """

        url = self.__BASE_URL + 'users/referral/referral-status'

        payload = {'links': has_referrer}

        headers = {
            'Authorization': 'Token ' + self.token
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()

    def set_referrer(self, referrer_code):
        """کد دعوت باید در زمان ثبت‌نام توسط کاربر وارد شده یا با استفاده از پیوند دعوت به صورت خودکار پر شود. با این
        حال تا ۲۴ ساعت پس از ثبت‌نام نیز امکان ثبت معرف توسط کاربر با استفاده از این NobitexAPI وجود دارد. منظور از کاربر
        معرف، کاربری است که کاربر فعلی را دعوت نموده است """

        url = self.__BASE_URL + 'users/referral/set-referrer'

        payload = {'links': referrer_code}

        headers = {
            'Authorization': 'Token ' + self.token
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()

