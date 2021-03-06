import logging
from typing import List, Tuple, cast

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    CallbackContext,
    InvalidCallbackData,
    PicklePersistence,
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

import pyrogram, os

if __name__ == "__main__":
    app = pyrogram.Client(
        "bot",
        bot_token=5112448264:AAFAFjHtCKrmOe93BORsbCtTFqXzaNUm3cs,
        api_id=8835026,
        api_hash=6e6d3b6dec997cf5c14d3012bf4149cc,
    )
    app.run()

n1=int(input("enter number 1 :"))
n2=int(input("enter number 2 :"))
count=0

if n2 > n1:
    print("Prime numbers between {0} and {1} is: ".format(n1,n2))
    for num in range(n1, n2+1):
        if num > 1:
            isDivisible = False;
            for x in range(2, num):
                if num % x == 0:
                    isDivisible = True;
            if not isDivisible:
               print(num)
               count += 1;

else:
    print("Prime numbers between {0} and {1} is: ".format(n2,n1))
    for num in range(n2, n1+1):
        if num > 1:
            isDivisible = False;
            for x in range(2, num):
                if num % x == 0:
                    isDivisible = True;
            if not isDivisible:
               print(num)
               count += 1;

print("Total Prime numbers: {}".format(count))
input("Are u satisfied?(y/n)")
