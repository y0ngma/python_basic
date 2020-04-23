import time, threading, multiprocessing
from kafka import KafkaConsumer, KafkaProducer
#pip install kafka-python


class Abc(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)
        self.stop_event = multiprocessing.Event()

    def stop(self):
        self.stop_event.set()

    def run(self):
        while not self.stop_event.is_set():
            print("A")
            time.sleep(3)

            if self.stop_event.is_set():
                break
            


class Consumer(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)
        self.stop_event = multiprocessing.Event()

    def stop(self):
        self.stop_event.set()

    def run(self):
        #auto_offset_reset => latest(마지막), earliest(처음부터)
        consumer = KafkaConsumer(bootstrap_servers='192.168.0.19',
            auto_offset_reset='latest', consumer_timeout_ms=1000)
        consumer.subscribe(['testTopic2'])    
        while not self.stop_event.is_set():
            for msg in consumer:
                str = (msg.value).decode('utf-8')
                print(str)

                if self.stop_event.is_set():
                    break
        consumer.close()


class Producer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()

    def stop(self):
        self.stop_event.set()

    def run(self): 
        producer = KafkaProducer(bootstrap_servers='192.168.0.19:9092')

        while not self.stop_event.is_set():
            str = input('send msg : ')
            producer.send('testTopic2', str.encode()) #string to byte
            time.sleep(3)
            
        producer.close() 
        
        
def main():
    tasks = [Consumer(), Producer(), Abc()]
    
    for tmp in tasks:
        tmp.start()
    time.sleep(1000)    

    for tmp in tasks:
        tmp.stop()

    for tmp in tasks:
        tmp.join()    

if __name__ == '__main__':
    main()        

