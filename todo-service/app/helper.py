import sqlite3

DB_PATH = './todo.db'
NOTSTARTED = 'Not Started'
INPROGRESS = 'In Progress'
COMPLETED = 'Completed'

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = dict_factory
    return conn

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def add_to_list(item):
    try:
        conn = get_connection()
        c = conn.cursor()
        c.execute('insert into items(item, status) values(?,?)', (item, NOTSTARTED))
        conn.commit()
        return {"item": item, "status": NOTSTARTED}
    except Exception as e:
        print('Error: ', e)
        return None

todo_list = {}

def get_all_items():
    try:
        conn = get_connection()

        c = conn.cursor()
        c.execute('select * from items')
        rows = c.fetchall()
        return { "count": len(rows), "items": rows }
    except Exception as e:
        print('Error: ', e)
        return None

def get_item(id):
    try:
        conn = get_connection()

        c = conn.cursor()
        c.execute("select * from items where id='%s'" % id)
        item = c.fetchone()
        print(item)
        return item
    except Exception as e:
        print('Error: ', e)
        return None
    
def update_status(id, status):
    #Check if the passed status is a valid value
    if(status.lower().strip() == 'not started'):
        status = NOTSTARTED
    elif(status.lower().strip() == 'in progress'):
        status = INPROGRESS
    elif(status.lower().strip() == 'completed'):
        status = COMPLETED
    else:
        print("Invalid Status - " + status)
        return None
    
    try:
        conn = get_connection()
        c = conn.cursor()
        c.execute('update items set status=? where id=?', (status, id))
        conn.commit()
        return {id: status}
    except Exception as e:
        print('Error: ', e)
        return None

def delete_item(id):
    try:
        conn = get_connection()
        c = conn.cursor()
        c.execute('delete from items where id=?', (id,))
        conn.commit()
        return {'item': id}
    except Exception as e:
        print('Error: ', e)
        return None