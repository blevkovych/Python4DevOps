import sqlite3, sys

#Task: There is some SQLite database example.db. Create program that sets in database ports (ServerPorts.port_number)
# to 443 for all servers apache (ServerTypes.type_name is 'apache') in project 'Project3'.
#Command:python hw5.py /home/usr/example.db.

conn = sqlite3.connect(sys.argv[1])
c = conn.cursor()

def change_ports():
    c.execute("SELECT * FROM ServerTypes WHERE type_name = 'apache'")
    server_type = c.fetchone()
    c.execute('SELECT * FROM Servers WHERE servertypes_id = ?', (server_type[0],))
    servers = c.fetchall()

    c.execute("SELECT * FROM Projects WHERE proj_name = 'Project3'")
    project = c.fetchone()
    c.execute('SELECT * FROM ServerProjects WHERE projects_id = ?', (project[0],))
    serverprojects = c.fetchall()

    for servid in serverprojects:
        for serverid in servers:
            if servid[1] == serverid[0]:
                c.execute("UPDATE ServerPorts SET port_number = 80 WHERE servers_id = ?", (servid[1], ))
                conn.commit()

change_ports()
c.close()
conn.close()

