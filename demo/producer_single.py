import pika
from datetime import datetime
from settings import URI


# params = pika.ConnectionParameters('localhost')
params = pika.URLParameters(URI)
conn = pika.BlockingConnection(params)
channel = conn.channel()

channel.queue_declare(queue="test_q")




if __name__ == "__main__":
    now = datetime.now()
    current_time = now.strftime("%d.%m.%Y %H:%M:%S.%f")[:-4]  # берем только сотые
    
    channel.basic_publish(
        exchange="",
        routing_key="test_q",
        body=f"Hello, SYSDB-32! - {current_time}",
    )
