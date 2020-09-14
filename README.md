## 1. boip

Boiler Plateの略でboipです。  
コードを書くときのテンプレートを元に、いくつかの質問の答えからコードを生成するライブラリです。  
私がテクニカルアーティストなので、追加するtemplateはMaya関連などのコード生成が多めです。  


## 2. 使い方
### 2.1. pip installする
```bash
python -m pip install boip
```

### 2.2. CLIでboipを実行する
```bash
python -m boip
```

### 2.3. テンプレートを配置したいフォルダに移動する
```bash
cd "テンプレートを配置したいフォルダパス"
```

### 2.4. テンプレートを選び質問に答える

[![Image from Gyazo](https://i.gyazo.com/b3127fecbe5af7ea40fdce9a09e86c25.gif)](https://gyazo.com/b3127fecbe5af7ea40fdce9a09e86c25)

### 生成されたフォルダを確認する
最後のフォルダ名でカレントディレクトリ以下にコピーされています。  
今回は「MayaQt-MVC」を選びましたので、Maya+Qt+MVCパターンのテンプレートが生成されてます。  

[![Image from Gyazo](https://i.gyazo.com/fc49047b094d2d9dfe305da46ad30f0a.gif)](https://gyazo.com/fc49047b094d2d9dfe305da46ad30f0a)



## 3. 自分のテンプレートを追加する
あらかじめコードひな形(BoipSet)を用意し、-sフラグでBoipSetがあるフォルダパスを指定してください。
```
python -m boip -s "対象のフォルダパス"
```

### 3.1. BoipSetとは
下記の2つをセットでBoipSetとしています。  
・質問後、置き換えに使う「template」という名前のフォルダ  
・boip.yamlという名前の設定ファイルが必要です。  
  
参考は[こちら](https://github.com/InTack2/boip/tree/master/src/boip/preset)  

#### 3.1.1. boip.yamlの書き方
``` yaml
title: MayaQt-MVC # テンプレート名
convertExtensions: # 変更前の拡張子:　変更後の拡張子(同じ拡張子でもOK.)
  py: py
  ui: ui
question: # 質問リスト(１つの質問で可)
  - name: tool_name # 置き換えに使う名前. ひな形のコードには{名前}で記載する
    message: "Tool name?" # 質問
    default: sampleWindow # 既存の値

  - name: maya_version
    message: "What version of Maya are you using?"
    default: 2020
```

#### 3.1.2. templateの作り方
template以下のフォルダが丸々コピーされ{name}内が質問の答えで変換されます。  
未来的には自動生成を入れる想定ですが、現状は手動です。  

例)上記の「MayaQt-MVC」の場合  
質問が{tool_name}と{maya_version}の2つがあります。

・テンプレート
```python:sample.py
import sys

print("{tool_name}")
print("{maya_version}")
```

・質問に答える
```bash
Tool name? > sampleWindow
What version of Maya are you using? > 2020
```

・生成後
質問の答えで変換されて下記になります。
```python:sample.py
import sys

print("sampleWindow")
print("2020")
```
