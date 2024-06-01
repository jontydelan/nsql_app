# import vanna
from vanna.remote import VannaDefault


def get_vanna_rep(question):
    """example :- 'What are the top 10 artists by sales?'"""
    vn = VannaDefault(model="chinook", api_key="e00f12176f754dd6b5fd0f53fe90ca4a")
    # vn.connect_to_sqlite("https://vanna.ai/Chinook.sqlite")
    vn.connect_to_sqlite("./Chinook.sqlite")
    return vn.generate_sql(question)
