import ibm_db


"""
METODI DI SQL FOR PYTHON

callproc()
execute()
executemany()
fetchone()
fetchmany()
fetchall()
nextset()
arraysize()
close()

CREDENZIALI

database": "bludb"
password": "BNoBXoqHFECGsw0S",
"username": "sxf93821"
hostname": "fbd88901-ebdb-4a4f-a32e-9822b9fb237b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud",
"port": 32731
"""


dsn_driver = "{IBM DB2 ODBC DRIVERE}"
dsn_database = "BLUDB"
dsn_hostname = 'fbd88901-ebdb-4a4f-a32e-9822b9fb237b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud'
dsn_port = '32731'
dsn_protocol = 'TCPIP'
dsn_uid = 'sxf93821'
dsn_pwd = 'BNoBXoqHFECGsw0S'
dsn_security = "SSL"

#%%

dsn = (
    "DRIVER = ((IBM BD2 OBC DRIVER));"
    "DATABASE = (0);"
    "HOSTANAME = (1);"
    "PORT=(2);"
    "PROTOCOL=TCPIP;"
    "UID=(3);"
    "PWD=(4);").format(dsn_database, dsn_hostname, dsn_port, dsn_uid, dsn_pwd)
print(dsn)

#%%
try:
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

except:
    print ("Unable to connect: ", ibm_db.conn_errormsg() )

#%%

server = ibm_db.server_info(conn)

print ("DBMS_NAME: ", server.DBMS_NAME)
print ("DBMS_VER:  ", server.DBMS_VER)
print ("DB_NAME:   ", server.DB_NAME)
