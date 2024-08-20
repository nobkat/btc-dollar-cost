# btc-dollar-cost
ドルコスト平均法でBTCを積み立てる

## 環境構築

ryeを利用。rye syncで必要なパッケージがインストールされる

## しくみ

- [bitflyerのAPI](https://lightning.bitflyer.com/Developer)をつかう。「資産残高を取得」と「新規注文を出す」の２つが有効になっていれば良い
- API keyとsecretはGitHub の secretに保存しておき、環境変数として呼び出す。
- GitHub Actionsで定期実行する。購入金額を変更するには`.github/workflows/weekly.yaml`を変更する。
- 結果をLINEへ通知する。[LINE Notify](https://notify-bot.line.me/my/)を使用
