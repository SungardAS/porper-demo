
class Demo:

    def __init__(self, connection):
        self.connection = connection

    def create(self, params):
        sql = "INSERT INTO demo (id, name, description) VALUES ('%s', '%s', '%s')" % (params['id'], params['name'], params['description'])
        print sql
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
        return params['id']

    def find(self, params):
        sql = "SELECT * FROM demo"
        if params.get('id'):
            sql += " WHERE id = " + params['id']
        elif params.get('name'):
            sql += " WHERE name = '" + params['name'] + "'"
        print sql
        rows = []
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            for row in cursor:
                rows.append({'id':row[0], 'name':row[1], 'description':row[2]})
        return rows
