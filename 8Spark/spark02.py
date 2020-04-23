# 다음은 우분투 쥬피터에서 카프카를 실행한 후 실행시킨다
####################################

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
        # auto_offset_reset : latest, earliest
        consumer = KafkaConsumer( bootstrap_servers='192.168.0.15'
                    , auto_offset_reset='latest', consumer_timeout_ms=1000 )
        consumer.subscribe(['testTopic2']) # list:즉, 다양한곳에서부터 받을 수 있음
        while not self.stop_event.is_set():
            for msg in consumer:
                # str = msg.value # 기본 한글안됨 버전
                str = (msg.value).decode('utf-8')
                print(str)

                if self.stop_event.is_set():
                    break
        consumer.close()

class Producer(threading.Thread): #=multiprocessing.Process
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()

    def stop(self):
        self.stop_event.set()

    def run(self): 
        producer = KafkaProducer( bootstrap_servers='192.168.0.15:9092' ) # 15

        while not self.stop_event.is_set():
            str = input('send msg : ')
            #string to byte, senable only to 1 of topic
            producer.send( 'testTopic2', str.encode() ) 
            time.sleep(0.1)
            
        producer.close() 

def main():
    tasks=[Consumer(), Producer()]

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