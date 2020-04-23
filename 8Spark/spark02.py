# pip install kafka-python
import time, threading, multiprocessing
from kafka import KafkaConsumer, KafkaProducer
# threading이 필요한 이유는 Consumer의 무한루프에서 print()으로
# 받은 메세지를 출력하는데 가령 10초 단위로 하고자 하면서 동시에
# Producer로 메세지를 보내기도 해야 하는 동시 운영 상황에서 필요
class Consumer(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)
        self.stop_event = multiprocessing.Event()

    def stop(self):
        self.stop_event.set()

    def run(self):
        consumer = KafkaConsumer(
             bootstrap_servers='192.168.0.15'
            , auto_offset_reset='latest'
            , consumer_timeout_ms=1000 )
        consumer.subscribe(['testTopic2'])
        while not self.stop_event.is_set():
            for msg in consumer:
                str=msg.value
                print(str)

                if self.stop_event.is_set():
                    break
        consumer.close()

def main():
    tasks=[Consumer()]

    for tmp in tasks:
        tmp.start()
        time.sleep(1000)

    # 안전하게 종료해주는 코드
    for tmp in tasks:
        tmp.stop()

    for tmp in tasks:
        tmp.join()

if __name__ == "__main__":
    main()