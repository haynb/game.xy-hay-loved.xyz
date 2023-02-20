import pymysql
from flask import Flask, jsonify, request

app = Flask(__name__)

connection = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '8848',
    db = 'game',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)


@app.route('/api/id_info',methods=['GET'])
def get_id_info():
    connection.ping(reconnect=True)
    game_id = request.args.get("game_id")
    if request.remote_addr != '127.0.0.1':
        return 'ip不被允许\n您的IP为：' + str(request.remote_addr), 403
    with connection.cursor() as cursor:
        sql = 'SELECT * FROM game WHERE game_id = %s'
        cursor.execute(sql,(int(game_id),))
        game_info = cursor.fetchall()
    if len(game_info) == 0:
        return 'None'
    return jsonify(game_info[0])



@app.route('/api/game_list',methods=['GET'])
def get_gameList():
    connection.ping(reconnect=True)
    currentPage = request.args.get("currentPage")
    pageSize = request.args.get("pageSize")
    if request.remote_addr != '127.0.0.1':
        return 'ip不被允许\n您的IP为：' + str(request.remote_addr), 403
    with connection.cursor() as cursor:
        sql = 'SELECT game_id,game_name,game_t_img FROM game WHERE game_id BETWEEN %s AND %s;'
        cursor.execute(sql,((int(currentPage)-1)*int(pageSize) + 1,(int(currentPage)-1)*int(pageSize) + int(pageSize)))
        game_currentPage = cursor.fetchall()
        sql = 'SELECT COUNT(*) FROM game;'
        cursor.execute(sql)
        total = cursor.fetchone()
        if len(game_currentPage) == 0:
            return jsonify(None)
        return jsonify(rows = game_currentPage,total = total["COUNT(*)"])
    

@app.route('/api/search/searchKeyword',methods=['GET'])
def get_Keyword():
    connection.ping(reconnect=True)
    keyword = request.args.get("keyword")
    if request.remote_addr != '127.0.0.1':
        return 'ip不被允许\n您的IP为：' + str(request.remote_addr), 403
    with connection.cursor() as cursor:
        sql = "SELECT game_id,game_name FROM game WHERE game_name LIKE %s LIMIT 5;"
        cursor.execute(sql,('%'+str(keyword)+'%',))
        result = cursor.fetchall()
        return jsonify(result)


@app.route('/api/search/result',methods=['GET'])
def search():
    connection.ping(reconnect=True)
    keyword = request.args.get("keyword")
    if request.remote_addr != '127.0.0.1':
        return 'ip不被允许\n您的IP为：' + str(request.remote_addr), 403
    with connection.cursor() as cursor:
        sql = "SELECT game_id,game_name,game_t_img FROM game WHERE game_name LIKE %s;"
        cursor.execute(sql,('%'+str(keyword)+'%',))
        result = cursor.fetchall()
        return jsonify(result)



@app.route('/api/update_list',methods=['GET'])
def update_list():
    connection.ping(reconnect=True)
    if request.remote_addr != '127.0.0.1':
        return 'ip不被允许\n您的IP为：' + str(request.remote_addr), 403
    with connection.cursor() as cursor:
        sql = "SELECT game_id,game_name,game_t_img FROM game ORDER BY game_id DESC LIMIT 10;"
        cursor.execute(sql)
        result = cursor.fetchall()
        return jsonify(result)


@app.route('/api/test',methods=['GET'])
def test():
    return jsonify('test success')

if __name__ == '__main__':
    app.run(debug=True)

