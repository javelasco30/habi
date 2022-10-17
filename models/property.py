from database import ConnectorDB


class Property():
    def get_result_execute(self, sql, params):
        connect = ConnectorDB()
        result = connect.execute_sql(sql, params)
        return result

    def get_select_sql(self):
        select = "SELECT p.address, p.city, s.label, p.price, p.description "
        return select

    def get_from_sql(self):
        from_sql = (" FROM status_history AS sh "
                    " INNER JOIN property AS p ON p.id = sh.property_id"
                    " INNER JOIN status AS s ON s.id = sh.status_id")
        return from_sql

    def get_where_sql(self):
        where = " WHERE s.name = %s "
        return where

    def get_property_by_state(self, params):
        params_sql = []
        if not params.get('status', False):
            return {}

        select = self.get_select_sql()
        from_sql = self.get_from_sql()
        where = self.get_where_sql()
        params_sql += params.get('status', False)

        if params.get('city', False):
            params_sql += params.get('city', False)
            where += "AND city= %s"

        if params.get('city', False):
            params_sql += params.get('city', False)
            where += "AND city= %s"

        if params.get('year_build', False):
            params_sql += params.get('year_build', False)
            where += "AND year= %s"

        results = self.get_result_execute(select+from_sql+where, params_sql)
        return results
