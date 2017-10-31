# サンプル（プロダクト名）

[![Product Name](https://raw.github.com/GabLeRoux/WebMole/master/ressources/WebMole_Youtube_Video.png)](https://www.youtube.com/channel/UC4PtjOfZTbVp9DwtJv82Lzg)

## 製品概要
### 物流 X Tech

### 背景（製品開発のきっかけ、課題等）
2017年4月7日に宅配大手のヤマト運輸が，Web通販サービスのアマゾン・ジャパンの
「当日配達サービス」からの撤退を検討しているというニュースがあり大変話題を呼んだ．
この騒動のあとも各企業がこぞってサービス維持のための値上げを行ったり国内大手オークションサイトであるヤフオクが配送サービスである
「はこBOON」の一時的なサービス休止を行うなど，宅配業界が過剰なまでの社会からの要求にこたえきれず，サービスを制限したり望まない値上げを行うことを余儀なくされている．
この原因として，不在配達による再配達のための経済的損失が大きいことがあげられる．ヤマト運輸，佐川急便，日本郵便の3社が実施した調査によると再配達率は平均で全配達率の19.6%であり，
国土交通省の昨年の宅配データから算出するにおおよそ8億回もの再配達が行われていたことになる．


### 製品説明（具体的な製品の説明）
宅配荷物を入れるケースにRaspberry Piを搭載して現時刻におけるケースの位置情報やセキュリティのために写真をメールで送信することができる．


### 特長

#### 1. 特長1
Raspberry Piを用いているので電源はUSB供給でよい。
#### 2. 特長2
人感センサで人がいることを検知すると写真を撮るシステム（無駄に電力やデータメモリを消費しない）
#### 3. 特長3
セキュリティ強化のため，ユーザがもつ端末からデバイスの位置情報がリアルタイムでわかる。
また，ユーザの顔を登録しておけば，NECのAPIで顔認証を行いユーザの顔であると判断した際はメールを送らないシステムにした。


### 解決出来ること
再配達を減らすことで，効率の良い物流を行うことができ，これが運送会社の残業時間の削減につながる。
ラズパイを積んだ箱の回収については，コンビニ等で一括して回収を行えば，再配達に比べてかなり効率的なシステムになる。
さらにこのシステムを用いれば，コンビニは顧客の個人情報を扱う必要がなくなるので，コンビニの業務負担を大きく減らすことが可能である。


### 今後の展望
このシステムはセキュリティの問題が発生する。箱を簡単には壊せないものにするなどの方法があるが，今回はGPSを用いて受け取り側が荷物の位置情報を常に確認できるようにしようとした。
しかし，屋内での実装であったことと，GPSモジュールが比較的古いものであったことが原因で，通信の際GPSからの位置情報がnullとなってしまった。
したがって，モジュール全体を金属でおおわれてしまった場合は位置情報が読み取れない問題がある。（静電遮蔽）

今後の展望としてNECのAPIでの顔認証を用いたキーロック解除が行えるようにしてきたい。
また，USB充電がどれくらい持つかの検証を行う。より小型で省電力の組み込みができればさらに良い。


## 開発内容・開発技術
### 活用した技術
#### API・データ
今回スポンサーから提供されたAPI、製品などの外部技術があれば記述をして下さい。

* NEC
* AWS
* 

#### フレームワーク・ライブラリ・モジュール
* 
* カメラモジュール
* 人感センサ
* 

#### デバイス
* Raspberry Pi3
* 

### 研究内容・事前開発プロダクト（任意）
ご自身やチームの研究内容や、事前に持ち込みをしたプロダクトがある場合は、こちらに実績なども含め記載をして下さい。

* 
* 


### 独自開発技術（Hack Dayで開発したもの）
#### 2日間に開発した独自の機能・技術
* Raspberry PiにGPSセンサーをつけて，位置情報をAWSにあげてiOSで確認できるようにした．
* Raspberry Piから人感センサに反応があった時に，写真をメールで送るようにした．
