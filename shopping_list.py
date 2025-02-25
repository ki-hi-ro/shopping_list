import os
import json


def load_shopping_list(filepath):
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            items = [line.strip() for line in f.readlines()]
        print("前回の買い物リストを読み込みました。")
    else:
        items = []
    return items


def save_shopping_list(filepath, items):
    with open(filepath, "w", encoding="utf-8") as f:
        for item in items:
            f.write(f"{item}\n")
    print(f"買い物リストを保存しました → {filepath}")


def main():
    # shopping_list.txtを保存したいパスをconfig.jsonに記入して読み込む
    with open("/Users/hiroki/Downloads/Python/shopping_list/config.json", "r", encoding="utf-8") as f:
      config = json.load(f)

    filepath = config["shopping_list_path"]

    items = load_shopping_list(filepath)

    if not items:
        # 初回登録モード
        print("買うものを入力してください（改行で区切る、終了は空行）:")
        while True:
            item = input()
            if item == "":
                break
            items.append(item)
        save_shopping_list(filepath, items)
        print("リスト作成が完了しました。また必要になったら起動してください。")
        return

    while True:
        print("\n現在の買い物リスト：")
        for i, item in enumerate(items):
            print(f"{i + 1}. {item}")

        print("\n1. 新しく追加する")
        print("2. 買ったものを削除する")
        print("3. 終了")

        choice = input("選択: ")

        if choice == "1":
            # 商品追加モード
            print("\n追加する商品を改行で入力してください（終了は空行）:")
            while True:
                new_item = input()
                if new_item == "":
                    break
                items.append(new_item)

            save_shopping_list(filepath, items)

        elif choice == "2":
            # 買ったもの削除モード
            indexes_to_delete = []
            print("\n買ったものがあれば番号を改行で入力してください（終了は空行）:")
            while True:
                number = input()
                if number == "":
                    break
                try:
                    index = int(number) - 1
                    if 0 <= index < len(items):
                        indexes_to_delete.append(index)
                    else:
                        print(f"{number} は無効な番号です")
                except ValueError:
                    print("番号を入力してください")

            # 後ろから削除
            for i in sorted(indexes_to_delete, reverse=True):
                del items[i]

            save_shopping_list(filepath, items)

            if not items:
                print("すべて購入済みになりました。")
                break

        elif choice == "3":
            print("終了します")
            break

        else:
            print("無効な選択です。1〜3を入力してください。")


if __name__ == "__main__":
    main()