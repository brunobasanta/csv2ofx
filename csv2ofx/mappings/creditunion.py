from __future__ import absolute_import, division, print_function, unicode_literals

from operator import itemgetter

mapping = {
    "has_header": True,
    "is_split": False,
    "bank": "Credit Union",
    "currency": "USD",
    "account": "Credit Union",
    "date": itemgetter("Date"),
    "amount": itemgetter("Amount"),
    "payee": itemgetter("Description"),
    "notes": itemgetter("Comments"),
    "check_num": itemgetter("Check Number"),
}
