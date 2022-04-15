import mysql.connector
from auth import MYSQL_credentials as cred


class custom_SQL:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(**cred)
        except mysql.connector.Error as err:
            return(err)
    
    def select(self,Q,table,conditions,where=False):
        cur = self.con.cursor(buffered=True)
        statement = f'SELECT {Q} FROM {table}'
        if where:
            features = []
            matches = []
            for key in conditions:
                features.append(key)
                matches.append(conditions[key])

            statement += ' WHERE {}=%s'.format(features[0])
            if len(conditions.keys())>1:
                for feat in features[1:]:
                    statement += ' AND {}=%s'.format(feat)
            print(statement)
            cur.execute(statement,(*matches,))
        else:
            cur.execute(statement,(Q,table))
        # result = cur.fetchall()
        column_names = [c[0] for c in cur.description]
        data_dict = dict()
        for name in column_names:
            data_dict[name] = []
        results = [cur.fetchall()]
        # print(results)
        for row in results[0]:
            # print(row)
            for i, col in enumerate(row):
                data_dict[column_names[i]].append(col)
        
        print(data_dict)
        cur.close()

        return data_dict

    def insert(self,table,columns,values,close=True):
        cur = self.con.cursor(buffered=True)
        statement = 'INSERT INTO %s %s VALUES %s'
        cur.execute(statement,(table,columns,values))
        last_id = cur.lastrowid
        if close:
            cur.close()
        return last_id

    def close(self):
        self.con.close()





