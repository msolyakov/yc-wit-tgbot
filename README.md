# Summary

Теlegram Bot uses Wit and Yandex Cloud Functions.

# References

Types and helpers for telegram API were used from https://github.com/eternnoir/pyTelegramBotAPI

##### Before you start

Before getting started, you should have the following installed and running:

- [X] Python 3.7 32bit
- [X] Pipenv - [instructions] pip install pipenv
- [X] Wit.ai SDK - [instructions] pipenv install wit

* Setup virtual environment, install dependencies, and activate it:

	```
	$ pipenv install --dev
	$ pipenv shell
	```

## Setup and run

- [*] Create a new Telegram Bot (for example, using @BotFather);
- [*] Create a new Cloud Function and make it public - https://cloud.yandex.ru/docs/functions/ ;
- [*] Link new Telegram bot to Cloud function as a webHook:

```
$ curl -F "url=https://functions.yandexcloud.net/{secret_function_id}" 
	https://api.telegram.org/bot{secret_bot_key}/setWebhook
```

Then you can try it.
