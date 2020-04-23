# topic (channel)


# broker
## MQTT
- 사물인터넷(라즈베리파이 실무용), 파이선가능
    - 온실하우스 온도계가 서버로 MQTT를 통해 전달
    - 적정온도 유지 가능
- 데이터 통신 + 백엔드DB에 통신내역 저장
- 배달의 민족(고객-라이더1km 이내의)
    - 한국 토픽 / 부산 토픽 / 동래구 토픽 / 장전동 토픽
    - 메세지queue 형태
    - 다음은 배달이 되기까지의 통신과정 설명임

    클라이언트|토픽|설명
    --|--|--|--
    Customer|없음<br>('Producer'는<br>'Consumer'의<br>토픽을 정하여 이용)|1단계 :<br> 고객이 배달의 민족앱에서 어떤 매장의(토픽선택)<br>음식을 장바구니에 담아 결제하고 주문서 전송<br>`producer.send(store/pusan/051-000-0001, 순살반반)`
    Restaurant|store/pusan/<br>051-000-0001|2단계 :<br>"배달의 민족, 쭈문" 알림음과 함께 근방의 고객으로부터 주문서를 받아<br>`consumer.subscribe([client/pusan/*])`<br>음식조리 및 근방의 라이더에게 배달요청서 전송<br>`producer.send(rider/pusan/jangjeon/*, 출발-도착주소)`
    Deliever|rider/pusan/<br>jangjeon/<br>010-0000-1000|3단계 :<br>근방의 매장으로부터 라이더들은 주문뜨면 광클해서 배달건확보<br>`consumer.subscribe([store/pusan/jangjeon/*])`
    Restaurant|store/pusan/<br>051-000-0001|4단계 :<br>해당매장이 배달소요시간(ETA)을 주문고객에게 전달<br>`producer.send(client/pusan/010-xxx-xxxx, ETA)`
    Customer|client/pusan/<br>010-xxx-xxxx|5단계 :<br>주문고객이 해당 매장으로 부터 메세지 받음<br>`consumer.subscribe([store/pusan/051-000-0001])`


- facebook
## kafka
- 서버, 브로커
### Zookeeper
- 전화국
- 서버에 여러대의 zookeeper 들어감
- 백엔드DB 역할을 Zookeeper가 대신함

## XMPP
- kakaotalk
## rabbitMQ
