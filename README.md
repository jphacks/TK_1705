# あ、居なかったんでここに置いときますね。
 

[![Product Name](/image/samne.png)](https://youtu.be/SxLu6f-hn-4)

## 製品概要
### 物流 X Tech


### 背景（製品開発のきっかけ、課題等）
2017年4月7日に宅配大手のヤマト運輸が，Web通販サービスのアマゾン・ジャパンの「当日配達サービス」からの撤退を検討しているというニュースがあり大変話題を呼んだ。この騒動のあとも各企業がこぞってサービス維持のための値上げを行ったり国内大手オークションサイトであるヤフオクが配送サービスである。

「はこBOON」の一時的なサービス休止を行うなど，宅配業界が過剰なまでの社会からの要求にこたえきれず，サービスを制限したり望まない値上げを行うことを余儀なくされている。
この原因として，不在配達による再配達のための経済的損失が大きいことがあげられる．ヤマト運輸，佐川急便，日本郵便の3社が実施した調査によると再配達率は平均で全配達率の19.6%であり，国土交通省の昨年の宅配データから算出するにおおよそ8億回もの再配達が行われていたことになる。

### 製品説明（具体的な製品の説明）
宅配業務の増加により，ドローンを用いた配達が計画されておりアメリカや日本の離島などでは実験的に導入されているが，普及までにはかなりの時間がかかると予想される。
そこで，それまでの応急処置として不在時に再配達をせずに済むシステムを提案する。

それは，商品受け取り時，不在だった場合，商品を入れ，玄関先においておけるケースを企業側が持つことである。
ケースには盗難防止のため位置情報や近くにいる人などの情報をリアルタイムで商品受け取り側の通信端末に送信される。
そして，商品を受け取ったユーザーがその箱を最寄りのコンビニや設置された回収所に持っていき一括回収するというシステムを実現する製品である

### 特長
![System Image](https://github.com/jphacks/TK_1705/blob/master/image/jphacks2017_tk1705_01.png)

使用していない際にはケースは折りたたむことのできるようにしておくので，低コスト，低電力，小型のモジュールを組み込む必要がある。

Raspberry Piを用いて実装されている。Raspberry Piには人感センサ，カメラモジュール，GPSモジュールが取り付けられている。
これは商品の盗難を防ぐためのものである。
図で示してあるように，人感センサで人を感知すると写真を撮影し，AWSサーバに写真と位置情報を送る。そしてサーバからユーザー側の通信端末にメールが送られる。ユーザー側はAWSサーバーから常に現在の荷物の位置情報等を確認できる。

#### 1. 特長1
Raspberry Piを用いているので電源はUSB供給でよい。
#### 2. 特長2
さらに電力消費を抑えるため，人感センサで人がいることを検知すると写真を撮るシステム（無駄に電力やデータメモリを消費しない）
#### 3. 特長3
クラウドを使用する有用性として，即効性が求められているので，いちいちサーバーを組み立てる必要がない点や，ドローンを用いた配達等の別の手法が主流になった際，容易に撤退できる製品となっている。

### 解決出来ること
この製品を使用したシステムを用いれば，再配達件数を確実に減らすことができ，運送会社の社員の残業時間を大幅に軽減することが可能である。
また，このシステムは運送会社だけではなくコンビニの業務も減らすことができる。コンビニ受け取りに比べ，コンビニが個人情報を扱う必要がなく，ケースを受け取るだけでよくなる。


### 今後の展望

今後の展望としてNECのAPIでの顔認証を用いたキーロック解除が行えるようにしてきたい。

そして，残っている問題はまず，Raspberry Piの充電が切れる可能性の問題がある。充電が切れてしまった時点でセキュリティが効かなくなってしまうので充電がどれくらいかという情報をユーザー側に送る必要がある。
今回の実装では，屋内での実装であったことと，GPSモジュールが比較的古いものであったことが原因で，通信の際GPSからの位置情報がnullとなってしまった。そこで，サンプルデータをいれてデモンストレーションを行った。

また，可能性としてケースを企業側ではなくユーザー側が持つということも考えられる。この場合，充電切れの問題がなくなりWi-Fiにつないでもらえればアップデートも容易にできる。
具体的には，ケースがいつも固定された位置に置かれているのでGPSで受け取った位置情報がそこからずれた場合，ユーザー側の端末に警告のメール、位置情報をおくる機能をつければよい。しかし，この方法は玄関先に常に大幅な場所をとってしまう問題がある。


## 開発内容・開発技術
今回の開発では，GPS情報を取得するため，Raspberry PiとGPSのモジュールをシリアル通信で接続した。
# 活用した技術
#### API・データ
* AWSをサーバーとして使用

#### フレームワーク・ライブラリ・モジュール

* カメラモジュール
* 人感センサ
* GPSモジュール

#### デバイス

* Raspberry Pi3
* ケース

### 研究内容・事前開発プロダクト（任意）

* 
* 


### 独自開発技術（Hack Dayで開発したもの
#### 2日間に開発した独自の機能・技術
* Raspberry PiにGPSセンサーをつけて，位置情報をAWSにあげてiOSで確認できるようにした。
* Raspberry Piから人感センサに反応があった時に，写真をメールで送るようにした。
