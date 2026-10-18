from flask import Flask, request, jsonify
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def total_echo():
    connection_info = {
        "real_client_ip": request.remote_addr,
        "request_method": request.method,
        "request_url": request.url,
        "query_parameters": request.args.to_dict()
    }
    
    headers_received = dict(request.headers)
    json_body = request.get_json(silent=True) or {}
    
    return jsonify({
        "connection": connection_info,
        "headers": headers_received,
        "body": json_body
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
  
