# PracticeTelegramBot
## All English Quizzes, Current Affairs, Professional IT Knowledge sets are managed by this bot.

You need Python3 (3.6 works fine, 3.5 will crash randomly).

Install dependencies by running this command:

    pip install -r requirements.txt

(If you want faster downloading-uploading, then install `cryptg` and its dependencies)

Warning: If you get a `File size too large message`, check the version of Telethon library you are using. Old versions have got a 1.5Gb file size limit.


Obtain your own api id: https://core.telegram.org/api/obtaining_api_id

# Usage

Rename file `.envs` to `.env` and add required values into it or
add these values to your config variable sections in cloud platform:

| Environment Variable     | Command Line argument | Description                                                  
|--------------------------|:-----------------------:|---------------------------------------------------------------|

| `TOKEN`                    | `--TOKEN`             | Telegram bot TOKEN      |  Get from @botfather  

| `CHAT_ID`                   | `--channel_id`        | Your Channel id 1   |      Get from @userbot         | 

