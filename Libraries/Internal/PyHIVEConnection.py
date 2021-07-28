# conn = hive.Connection(host=host_name, port=port, username=user, password=password,
#                            database=database, auth='CUSTOM')
#     cur = conn.cursor()
#     cur.execute('select item_sk,reason_sk, account_credit from returns limit 5')
#     result = cur.fetchall()